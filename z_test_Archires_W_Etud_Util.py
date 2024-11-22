# -*- coding: utf-8 -*- 
import os
from dotenv import load_dotenv
from cl_Archires_W_Etud_Util import Archires_W_Etud_Util
from pymarc import Record, MARCReader
load_dotenv()

reader = MARCReader(open(os.getenv("ARCHIRES_W_ETUD_UTIL_RECORD_TEST"), 'rb'), to_unicode=True, force_utf8=True) # DON'T FORGET ME
ARCHIRES_W_ETUD_UTIL = Archires_W_Etud_Util(os.getenv("W_ETUD_PATH"), os.getenv("W_ETUD_RENAME_PATH"), os.getenv("OLD_SCHOOL_TO_NEW_SCHOOL_PATH"), os.getenv("SCHOOL_NAME_FROM_CODE_PATH"), os.getenv("SCHOOL_CODE_FROM_CITY_PATH"), os.getenv("SCHOOL_CODE_FROM_OTHERWORD_PATH"))
print(ARCHIRES_W_ETUD_UTIL.get_w_etud_name("TPFE"))
print(ARCHIRES_W_ETUD_UTIL.get_new_w_etud_code_from_old_one("TE"))
print(ARCHIRES_W_ETUD_UTIL.get_new_school_code_from_old_one("DEFS"))
print(ARCHIRES_W_ETUD_UTIL.get_school_name("PLVT"))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_city("Talence", normalize=True))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_city("Talence", normalize=False))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_other_word("BELLEVILLE", normalize=True))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_other_word("BELLEVILLE", normalize=False))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_text("VAL-DE-MARNE", normalize=False))
print(ARCHIRES_W_ETUD_UTIL.get_school_code_from_text("St-Étienne", normalize=True))

for index, record in enumerate(reader):
    bibnb = record.get("001").data
    need_328 = ARCHIRES_W_ETUD_UTIL.record_needs_328(record)
    print(f"{bibnb}\t\t : need 328 : {need_328}")