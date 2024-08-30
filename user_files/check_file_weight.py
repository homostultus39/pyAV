import os

from docker_sandbox.hshsumm.sign_paths import mdb, hdb
from itertools import chain
import re

with open(mdb, 'r') as mdb_signatures, open(hdb, 'r') as hdb_signatures:
    mdb_content = mdb_signatures.readlines()
    hdb_content = hdb_signatures.readlines()


def check_signature_file_weight(file_path: str):

    matched_signature_dict = {}

    virus_pattern = re.compile(fr':{str(os.path.getsize(file_path))}:')

    content = chain(hdb_content, mdb_content)

    for data in enumerate(content):
        if re.search(virus_pattern, data[1]):
            content_of_virus_data = data[1].strip().split(":")
            matched_signature_dict[content_of_virus_data[2]] = content_of_virus_data[0]

    if matched_signature_dict:
        return matched_signature_dict
    else:
        return False