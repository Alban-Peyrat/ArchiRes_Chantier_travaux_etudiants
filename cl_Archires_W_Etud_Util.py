# -*- coding: utf-8 -*- 

# external imports
import os
import csv
import re
from unidecode import unidecode
from pymarc import Field, Indicators, Subfield, Record
from typing import Dict, List
import unicodedata
from datetime import datetime

REGEX_328A = [
    r"^[^:]* : [^:]* : [^:]* : [^:]* : \d*$",
    r"^[^:]* : [^:]* : [^:]* : \d*$",
    r"^[^:]* : [^:]* : \d*$",
    r"^[^/]* / [^,]*, \d*$",
    r"^[^:]*:[^:]*:\d*$",
    r"^[^/]*/[^,]*,\d*$",
    r"^[^:]*:[^:]*:[^:]*:\d*$",
    r"^[^\.]*\. [^\.]*\. [^\.]*\. \d*$",
    r"^[^\.]*\. [^\.]*\. \d*$",
    r"^[^-]* - [^,]*, \d*$",
    r"^\s*Travail personnel de fin d['|’]études.*",
    r"^\s*Travaux de fin d['|’]études.*",
    r"^\s*Projet\s*de fin d['|’]études.*",
    r"^\s*M[é|e]moire.*",
    r"^\s*Mast[e|è]r.*",
    r"^\s*MES.*",
    r"^\s*PFE.*",
    r"^\s*TPFE.*",
    r"^\s*HMONP.*",
    r"^\s*DEA.*",
    r"^\s*DESS.*",
    r"^\s*DPEA.*",
    r"^[^:]*: Th[è|e]se.*",
    r"^\s*\(?Th[è|e]se.*",
    r"^\s*\(?Th\..*",
    r"^\s*Doctorat.*",
    r"^\s*M[é|e]m\..*",
    r"^\s*Travail personnel d'étude et de recherche en paysage.*"
]

def prep_string_for_search(_str):
    """Returns a string without punctuation, multispaces, diacritics stripped and in upper case.

    Takes as arguments :
        - _str : the string to edit
    """
    # remove noise
    noise_list = [".", ",", "?", "!", ";","/",":","="]
    for car in noise_list:
        _str = _str.replace(car, " ")
    # remove multiple whtespace
    _str = re.sub(r"\s+", " ", _str).strip()
    # remove diacritics
    _str = unidecode(_str)
    return _str.strip().upper()

class Archires_W_Etud_Util(object):
    def __init__(self, w_etud_path:str, w_etud_rename_path:str, old_school_new_school_path:str, school_name_from_code_path:str, school_code_from_city_path:str, school_code_from_other_word_path:str):
        self.w_etud_path:str = os.path.normpath(w_etud_path)
        self.w_etud_rename_path:str = os.path.normpath(w_etud_rename_path)
        self.old_school_new_school_path:str = os.path.normpath(old_school_new_school_path)
        self.school_name_from_code_path:str = os.path.normpath(school_name_from_code_path)
        self.school_code_from_city_path:str = os.path.normpath(school_code_from_city_path)
        self.school_code_from_other_word_path:str = os.path.normpath(school_code_from_other_word_path)
        self.w_etud_name_index:Dict[str, str] = {}
        self.w_etud_rename_index:Dict[str, str] = {}
        self.old_school_to_new_school_index:Dict[str, str] = {}
        self.school_name_index:Dict[str, str] = {}
        self.school_code_from_city_index:Dict[str, str] = {}
        self.school_code_from_word_index:Dict[str, str] = {}
        
        # Load all indexes
        with open(self.w_etud_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.w_etud_name_index[line["code"].strip()] = line["name"].strip()
        with open(self.w_etud_rename_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.w_etud_rename_index[line["old"].strip()] = line["current"].strip()
        with open(self.old_school_new_school_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.old_school_to_new_school_index[line["old"].strip()] = line["current"].strip()
        with open(self.school_name_from_code_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.school_name_index[line["code"].strip()] = line["name"].strip()
        with open(self.school_code_from_city_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.school_code_from_city_index[line["city"].strip()] = line["code"].strip()
        with open(self.school_code_from_other_word_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for line in reader:
                self.school_code_from_word_index[line["word"].strip()] = line["code"].strip()

    # -------------------- Get data from mapping --------------------

    def get_w_etud_name(self, code:str) -> str|None:
        """Returns the W etud name from its code"""
        if not code.strip() in list(self.w_etud_name_index.keys()):
            return None
        return self.w_etud_name_index[code.strip()]
    
    def get_new_w_etud_code_from_old_one(self, code:str) -> str|None:
        """Returns the new W etud code from its old code"""
        if not code.strip() in list(self.w_etud_rename_index.keys()):
            return None
        return self.w_etud_rename_index[code.strip()]

    def is_old_school(self, code:str) -> bool:
        """Returns if the school code is a old school one"""
        return code.strip() in list(self.old_school_to_new_school_index.keys())

    def get_new_school_code_from_old_one(self, code:str) -> str|None:
        """Returns the new school code from its old code"""
        if not code.strip() in list(self.old_school_to_new_school_index.keys()):
            return None
        return self.old_school_to_new_school_index[code.strip()]

    def get_school_name(self, code:str) -> str|None:
        """Returns the school name from its code"""
        if not code.strip() in list(self.school_name_index.keys()):
            return None
        return self.school_name_index[code.strip()]
    
    def get_school_code_from_city(self, city:str, normalize:bool=True) -> str|None:
        """Returns the school code from a city name"""
        city = city.strip()
        if normalize:
            city = prep_string_for_search(city)
        if not city in list(self.school_code_from_city_index.keys()):
            return None
        return self.school_code_from_city_index[city]

    def get_school_code_from_other_word(self, word:str, normalize:bool=True) -> str|None:
        """Returns the school code from an expression"""
        word = word.strip()
        if normalize:
            word = prep_string_for_search(word)
        if not word in list(self.school_code_from_word_index.keys()):
            return None
        return self.school_code_from_word_index[word]
    
    def get_school_code_from_text(self, txt:str, normalize:bool=True) -> str|None:
        """Returns the school code from text, first checking if it's a city, then if it's a mapped other expression"""
        code = self.get_school_code_from_city(txt, normalize)
        if code != None:
            return code
        return self.get_school_code_from_other_word(txt, normalize)
        
    # -------------------- create content --------------------

    def generate_diss_nb(self, date:str|int, w_etud_code:str, school:str, bibnb:str|int) -> str:
        """Returns the disserattion number"""
        return f"{str(date)}_{w_etud_code}_{school}_{bibnb}"
    
    def generate_archires_029(self, date:str|int, w_etud_code:str, school:str, bibnb:str|int) -> Field:
        """Return a pymarc.Field 029 for ArchiRès"""
        field = Field("029", indicators=Indicators(" ", " "))
        field.add_subfield("a", "FR")
        field.add_subfield("m", self.generate_diss_nb(date, w_etud_code, school, bibnb))
        return field
    
    def generate_archires_328(self, record:Record, w_etud_code:str, date:int|str, school_code:str, theme:str="Architecture", is_date_unsure:bool=False) -> Field|None:
        """Return a new MARC field 328 for ArchiRès, returns a tupple with the field and a bool (true = error).
        
        Takes as argument :
            - record : the record object (for $e)
            - w_etud_code : code of the W etud
            - date : the date
            - [optional] theme : the theme for $c, defaults to Architecture
            - [optional] is_date_unsure : if the date is unsure, default to False"""
        
        new_field = Field("328", indicators=Indicators(" ", "0"))
        
        # $b
        w_etud_name = self.get_w_etud_name(w_etud_code)
        # Safety check
        if not w_etud_name:
            return None
        new_field.add_subfield("b", w_etud_name)

        # $c
        new_field.add_subfield("c", theme)
        
        # $e
        univ = None
        # try getting the university name from 214$c
        for field in record.get_fields("214"):
            if field.get_subfields("c"):
                univ = field.get_subfields("c")[0]
                break
        # try getting the university name from 210$c if no 214$c
        if not univ:
            for field in record.get_fields("210"):
                if field.get_subfields("c"):
                    univ = field.get_subfields("c")[0]
                    break
        # If neither 214$c or 210$c find something, generate it based on the school code
        if not univ:
            univ = self.get_school_name(school_code)
            # if nothing matches, leave
            if not univ:
                return None
            # if date is a str, checks if it's a valid date, leave if not
            if not re.search(r"^\d+$", date):
                return None
            # Rename the school name based on the date
            if 1985 <= int(date) and int(date) < 2005:
                univ = re.sub("^ENSAP*", "EA", univ)
            elif int(date) < 1985:
                univ = re.sub("^ENSAP*", "Unité pédagogique d'architecture", univ)
                univ = re.sub("^EA", "Unité pédagogique d'architecture", univ)
        # if still no university name, leave
        if not univ:
            return None
        new_field.add_subfield("e", univ)

        # $d
        if is_date_unsure:
            new_field.add_subfield("d",f"[{str(date)} ?]")
        else:    
            new_field.add_subfield("d", str(date))

        return new_field
    
    # -------------------- Get data from a record --------------------

    def record_needs_328(self, record:Record) -> bool|None:
        """Returns if a record needs a 328, returns None if there's no doctype"""
        # Check if doctype exists
        if not record.get("099"):
            return None
        if not record.get("099").get("t"):
            return None
        # Check if it's a W etud : if not, return False
        if record.get("099").get("t") != "TE":
            return False
        # get all the 328
        all_328 = record.get_fields("328")
        # If there's no 328, returns True
        if len(all_328) == 0:
            return True
        for field in all_328:
            # if at least a 328 has a $b, return False
            if field.get("b"):
                return False
            # If there's a $a, check its cotnent
            if field.get("a"):
                for regexp in REGEX_328A:
                    # if the $a matches one of the regexp, return False
                    if re.search(rf"{regexp}", unicodedata.normalize("NFC", field.get("a")), re.IGNORECASE): #rf"{}" to read the regexp raw (without double bacslashes)
                        return False
        # At this point, we can assume that all 328 that are ehre are incorect
        return True
    
    def get_school_code_from_record(self, record:Record) -> str|None:
        """Try getting a school code from the record"""
        item_date = None
        school = None
        # Check items first
        for item in record.get_fields("995"):
            # We have a date and a school
            if item_date and school:
                # Check if we have a date and a homebranch
                if item.get("5") and item.get("b"):
                    # if this one is newer, keep old one
                    if min(item_date, item.get("5"),
                        key=lambda x: datetime.strptime(x, "%Y-%m-%d")
                        ) == item.get("5"):
                        continue
                # get the date
                item_date = item.get("5")
                # get the collection
                if item.get("8"):
                    # if colelction = Old school, keep old shool as the school
                    if self.is_old_school(item.get("8")):
                        school = item.get("8")
                    # otherwise, take the school from homebranch
                    else:
                        school = item.get("b")
                # otherwise, take the school from homebranch (yes we need that twice)
                else:
                    school = item.get("b")
        # Now, if no school, get it from other part of the record
        strings_to_check = []
        for field in record.get_fields("214"):
            strings_to_check += field.subfields_as_dict()["c"]
        for field in record.get_fields("210"):
            strings_to_check += field.subfields_as_dict()["c"]
        for field in record.get_fields("214"):
            strings_to_check += field.subfields_as_dict()["a"]
        for field in record.get_fields("210"):
            strings_to_check += field.subfields_as_dict()["a"]
        for field in record.get_fields("710"):
            strings_to_check += field.subfields_as_dict()["a"]
        for field in record.get_fields("711"):
            strings_to_check += field.subfields_as_dict()["a"]
        for field in record.get_fields("712"):
            strings_to_check += field.subfields_as_dict()["a"]

        for txt in strings_to_check:
            if self.get_school_code_from_text(txt):
                return self.get_school_code_from_text(txt)
        # return None if no match
        return None