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

# Load paramaters
dotenv.load_dotenv()
# Env var used :
#   FILE_IN : marc file with records to edit
#   FILE_OUT : name of the new marc file
#   W_ETUD_MAPPING : mapping in json
#   W_ETUD_RENAME : rename mapping in json
#   LOGS_FOLDER : folder for the .log file

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

def add_subfield(field, code, value):
    """Adds the subfield to provided field or replace existing subfield"""
    if (field[code]):
        field[code] = value
    else:
        field.add_subfield(code, value)

def get_years(record, field, subfield):
    """Returns a list of ints containing the first 4 consecutive numbers in the specified field-subfield.
    
    Takes as argument :
        - record : the record object
        - field {str}
        - subfield {str}"""
    
    dates = []
    for field in record.get_fields("214"):
        for subfield in field.get_subfields("d"):
            years = re.findall("\d{4}", subfield)
            if len(years) > 0:
                dates.append(int(years[0]))
    return dates
# ----------------- Mappings -----------------

errors = {
    # "cell_nan":"At least one column has no value",
    # "no_file":"Provided file does not exist",
    # "get_item":"An error occured trying to get the item",
    # "wrong_bibnb":"The biblionumber provided is different from the one associated with the item",
    # "post_file":"An error occured trying to upload the file"
}

with open(os.getenv("W_ETUD_MAPPING"), "r+", encoding="utf-8") as f:
    data = json.load(f)
    W_ETUD_MAPPING = data["W_ETUD_MAPPING"]
    W_ETUD_RENAME = data["W_ETUD_RENAME"]
    OLD_SCHOOLS_MAPPING = data["OLD_SCHOOLS_MAPPING"]



# ----------------- Preparing Main -----------------

# Open in and out files
# BINARY is mandatory for MARC files
reader = pymarc.MARCReader(
    open(os.getenv("FILE_IN"), 'rb'),
    to_unicode=True,
    force_utf8=True) # DON'T FORGET ME
writer = open(os.getenv("FILE_OUT"), "wb") # DON'T FORGET ME

# Init logger
service = "W_etud_Traitement_retro"
logs.init_logs(os.getenv("LOGS_FOLDER"), service,'DEBUG')
logger = logging.getLogger(service)

# ----------------- Main -----------------

logger.info("Starting main function...")

# Loop through records
for index, record in enumerate(reader):
    logger.info(f"--- Starting Record {index}")

    # If record is invalid
    if record is None:
        logger.error(f"Current chunk: {reader.current_chunk} was ignored because the following exception raised: {reader.current_exception}")
        continue

    logger.info("Record is valid")

    # # do something with record
    # record["200"]["a"] = "[UPDATED] " + record["200"]["a"] # → unique field
    # print(record["200"]["a"])
    # for field in record.get_fields("995"): # → possible multiples fields
    #     print(field)
    # print(record["995"])
    
    # ---------- Record ----------

    # Get current typedoc
    field_099 = record["099"]
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
        logger.error("Record has no publication year")
    else:
        dates.sort()

    # Get the school
    item_date = None
    school = None
    for item in record.get_fields("995"):
        if not item_date:
            item_date = item["5"]
            school = item["b"]
        else:
            if min(
                item_date, item["5"],
                key=lambda x: datetime.strptime(x, "%Y-%m-%d")
                ) == item["5"]:
                school = item["b"]
        
        # Je sais pas ou mettre ça
        if item["8"]:
            if item["8"] in OLD_SCHOOLS_MAPPING:
                school = item["8"]


    # Get the biblionumber
    bibnb = record["001"].data

    # Generates disss number
    diss_nb = f"{dates[0]}_{current_typedoc}_{''}_{bibnb}"

    # Generates new 029
    field_029 = pymarc.field.Field(tag="029", indicators=[" ", " "])
    field_029.add_subfield("a", "FR")
    field_029.add_subfield("m", diss_nb)
    record.add_field(field_029)
    exit()
    
# logger.info(f"Field created : {show_datafield(field_801)}")

    # Edit 099
    for field in record.get_fields("099"):
        # Last Sudoc import
        field.delete_subfield("e")
        
        # Koha creation date
        add_subfield(field, "c", today)
        
        # Koha last edit date
        add_subfield(field, "d", today)
        
        # Converts item typedoc to record typedoc
        # ATM DOES NOT APPLY PRIORITY RULES 
        if (field["t"]):
            field.delete_subfield("t")
        for item in record.get_fields("995"):
            if not (item["r"]):
                logger.error(f"Item has no doctype : {show_datafield(item)}")
                continue
            if (item["r"] in TYPEDOC_mapping):
                # Adds priority
                # No 099$t : no need for priority
                if not (field["t"]): 
                    field.add_subfield("t", TYPEDOC_mapping[item["r"]])
                else:
                    if TYPEDOC_priority[TYPEDOC_mapping[item["r"]]] < TYPEDOC_priority[field["t"]]:
                        field.add_subfield("t", TYPEDOC_mapping[item["r"]])
                    else:
                        logger.info(f"Item TYPEDOC {item['r']} has less priority than {field['t']}")
            else:
                logger.error(f"Item TYPEDOC is not mapped : {item['r']}")
                continue 

    logger.info("Record fully processed")

    # Writes the record
    writer.write(record.as_marc())

logger.info("Main function just ended")

# Close in and out files
reader.close()
writer.close()

logger.info("<(^-^)> <(^-^)> Script fully executed without errors <(^-^)> <(^-^)>")