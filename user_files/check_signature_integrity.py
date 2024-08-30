import hashlib
from docker_sandbox.hshsumm.sign_paths import mdb, hdb, info

info_dict = {}

with open(info, 'r') as info_file:
    content_info_file = info_file.readlines()

    for line in content_info_file:
        info_dict[line.strip().split(':')[0]] = line.strip().split(':')[2]


def check_signature_integrity_hash(mdb_filepath=mdb, hdb_filepath=hdb):
    with open(mdb_filepath, 'rb') as mdb, open(hdb_filepath, 'rb') as hdb:

        mdb_hash = hashlib.sha256(mdb.read()).hexdigest()
        hdb_hash = hashlib.sha256(hdb.read()).hexdigest()

        if (mdb_hash and hdb_hash) in info_dict.values():
            return True
        else:
            return False
