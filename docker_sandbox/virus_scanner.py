import yara
import os
import re
import hashlib
from itertools import chain
from hshsumm.sign_paths import mdb, hdb
from pars_yara_rules_filepath import filepaths


class FilesScan:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_extension = os.path.splitext(file_path)[1]
        self.file_weight = os.path.getsize(file_path)

    def check_signature_file_hash(self, matched_signature_dict: dict):

        with open(self.file_path, 'rb') as file:
            scanned_file = file.read()

        hash_scanned_file = hashlib.md5(scanned_file).hexdigest()

        if hash_scanned_file in matched_signature_dict.values():
            return next(
                name for name in matched_signature_dict.keys() if matched_signature_dict[name] == hash_scanned_file)

    def check_signature_file_yara(self):

        rules = yara.compile(filepaths=filepaths)

        with open(self.file_path, 'rb') as file:
            matches = rules.match(data=file.read())

        if matches:
            try:
                return matches[0].meta["malware_family"]
            except:
                return matches[0].meta["malware_type"] + " none family"