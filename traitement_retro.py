# -*- coding: utf-8 -*- 

# external imports
import os
import dotenv
import json
import logging
import pymarc
import re
from datetime import datetime

# internal imports
import logs

# Need the file REGEX_328A in same same folder with the var REGEX_328A
# Containg a list of regular expressions
# Env var used :
#   FILE_IN : marc file with records to edit
#   FILE_OUT : name of the new marc file
#   ERRORS_FILE : name of the csv file for errors
#   W_ETUD_MAPPING : mapping in json
#   LOGS_FOLDER : folder for the .log file


# Load paramaters
dotenv.load_dotenv()

# ----------------- Functions definition -----------------

def show_datafield(field):
    """Returns the field as a string because pymarc doesn't work"""
    output =  field.tag + " " + "".join(field.indicators)
    for index, str in enumerate(field.subfields):
        # On even, is the subfield code
        if index % 2 == 0:
            output += "$" + str
        else:
            output += str            
    return output

def get_years(record, tag, code):
    """Returns a list of ints containing the first 4 consecutive numbers in the specified field-subfield.
    
    Takes as argument :
        - record : the record object
        - tag {str}
        - code {str}"""
    
    dates = []
    for field in record.get_fields(tag):
        for subfield in field.get_subfields(code):
            years = re.findall("\d{4}", subfield)
            if len(years) > 0:
                dates.append(int(years[0]))
    return dates

def is_old_school(item):
    """Returns the school based on the presence or not of an old school in $8.
    
    Takes as an argument an item field"""
    
    if item["8"]:
        if item["8"] in OLD_SCHOOLS_MAPPING:
            return item["8"]
    
    return item["b"]

def new_field_328(record, current_typedoc, date):
    """Generates a new MARC field 328, returns a tupple with the field and a bool (true = error).
    
    Takes as argument :
        - record : the record object
        - current_typedoc {str} : code of the previous typedoc
        - date {int} : the date previously found"""
    
    field_328 = pymarc.field.Field(tag="328", indicators=[" ", "0"])
    
    # $b
    field_328.add_subfield("b", W_ETUD_MAPPING[current_typedoc])

    # $c
    field_328.add_subfield("c", "Architecture")
    
    # $e
    univ = None
    for field in record.get_fields("214"):
        if field.get_subfields("c"):
            univ = field.get_subfields("c")[0]
            break
    if not univ:
        for field in record.get_fields("210"):
            if field.get_subfields("c"):
                univ = field.get_subfields("c")[0]
                break
    if not univ:
        return None, True
    field_328.add_subfield("e", univ)

    # $d
    field_328.add_subfield("d", str(date))

    return field_328, False

# ----------------- Mappings -----------------

with open(os.getenv("W_ETUD_MAPPING"), "r", encoding="utf-8") as f:
    data = json.load(f)
    W_ETUD_MAPPING = data["W_ETUD_MAPPING"]
    W_ETUD_RENAME = data["W_ETUD_RENAME"]
    OLD_SCHOOLS_MAPPING = data["OLD_SCHOOLS_MAPPING"]

from REGEX_328A import REGEX_328A

ERRORS = {
    "chunk_err":"Chunk error : check logs",
    "no_date":"No publication year",
    "no_item":"No item",
    "mult_328":"Already has multiple 328",
    "no_328ab":"328 has no $a or $b",
    "no_inst":"No institution",
    "no_typedoc":"No typedoc"
}

# ----------------- Preparing Main -----------------

# Open in and out files
# BINARY is mandatory for MARC files
reader = pymarc.MARCReader(
    open(os.getenv("FILE_IN"), 'rb'),
    to_unicode=True,
    force_utf8=True) # DON'T FORGET ME
writer = open(os.getenv("FILE_OUT"), "wb") # DON'T FORGET ME
errors_file = open(os.getenv("ERRORS_FILE"), "w", encoding="utf-8") # DON'T FORGET ME

# Init logger
service = "W_etud_Traitement_retro"
logs.init_logs(os.getenv("LOGS_FOLDER"), service,'INFO')
logger = logging.getLogger(service)

# ----------------- Main -----------------

logger.info("Starting main function...")

errors_file.write("record_nb;bibnb;error\n")

# Loop through records
for index, record in enumerate(reader):
    logger.info(f"--- Starting Record {index}")

    # If record is invalid
    if record is None:
        logger.error(f"Current chunk: {reader.current_chunk} was ignored because the following exception raised: {reader.current_exception}")
        errors_file.write(f"{index};;{ERRORS['chunk_err']}\n")
        continue

    logger.debug("Record is valid")

    # ---------- Record ----------

    # Clear previous iteration field
    field_029 = None
    field_099 = None
    field_328 = None

    # Get the biblionumber
    # Bibnb has to be in the record has the data comes from Koha
    bibnb = record["001"].data
    logger.debug(f"Biblionumber : {bibnb}")

    # Get current typedoc
    # Typedoc has to be in the record as the SQL query is based on it
    # Yup so I was wrong :)
    field_099 = record["099"]
    if not field_099["t"]:
        logger.error(ERRORS["no_typedoc"])
        errors_file.write(f"{index};{bibnb};{ERRORS['no_typedoc']}\n")
        continue
    current_typedoc = field_099["t"]
    # --- If this type was renamed
    if current_typedoc in W_ETUD_RENAME:
        current_typedoc = W_ETUD_RENAME[current_typedoc]

    # Rewrites with typedoc
    field_099["t"] = "TE"

    # Get publication year
    dates = get_years(record, "214", "d")
    if len(dates) == 0:
        dates = get_years(record, "210", "d")
    if len(dates) == 0:
        logger.error(ERRORS["no_date"])
        errors_file.write(f"{index};{bibnb};{ERRORS['no_date']}\n")
        continue
    else:
        dates.sort()

    # Get the school
    item_date = None
    school = None
    for item in record.get_fields("995"):
        if not item_date:
            item_date = item["5"]
            school = is_old_school(item)
        else:
            if item_date and item["5"]:# prevents error if no date on item 
                if min(
                    item_date, item["5"],
                    key=lambda x: datetime.strptime(x, "%Y-%m-%d")
                    ) == item["5"]:
                    school = is_old_school(item)

    if not school:
        logger.error(ERRORS["no_item"])
        errors_file.write(f"{index};{bibnb};{ERRORS['no_item']}\n")
        continue

    # Generates disss number
    diss_nb = f"{str(dates[0])}_{current_typedoc}_{school}_{bibnb}"
    logger.debug(f"Diss nb = {diss_nb}")

    # Generates new 029
    field_029 = pymarc.field.Field(tag="029", indicators=[" ", " "])
    field_029.add_subfield("a", "FR")
    field_029.add_subfield("m", diss_nb)
    record.add_field(field_029)

    # Checks if a new 328 is needed
    all_328 = record.get_fields("328")
    if len(all_328) > 1:
        logger.error(ERRORS["mult_328"])
        errors_file.write(f"{index};{bibnb};{ERRORS['mult_328']}\n")
        continue
    elif len(all_328) == 0:
        field_328, err_328 = new_field_328(record, current_typedoc, dates[0])
    elif len(all_328) == 1:
        if all_328[0]["b"]:
            # skip if 328$b is already there
            logger.debug(f"Does not require a new 328 : $b already there")
        elif not all_328[0]["a"]:
            logger.error(ERRORS["no_328ab"])
            errors_file.write(f"{index};{bibnb};{ERRORS['no_328ab']}\n")
            continue
        else:
            for regexp in REGEX_328A:
                if re.search(rf"{regexp}", all_328[0]["a"], re.IGNORECASE): #rf"{}" to read the regexp raw (without double bacslashes)
                    logger.debug(f"Does not require a new 328 : $a matched {rf'{regexp}'}")
                    break
            else:
                field_328, err_328 = new_field_328(record, current_typedoc, dates[0])
    
    # Add the 328
    if field_328:
        record.add_field(field_328)
        logger.debug(show_datafield(field_328))
    elif not(field_328) and err_328:
        logger.error(ERRORS['no_inst'])
        errors_file.write(f"{index};{bibnb};{ERRORS['no_inst']}\n")
        continue
   
    logger.info("Record fully processed")

    # Writes the record
    writer.write(record.as_marc())

logger.info("Main function just ended")

# Close in and out files
reader.close()
writer.close()
errors_file.close()

logger.info("<(^-^)> <(^-^)> Script fully executed without errors <(^-^)> <(^-^)>")