import os

filepaths = {}

for root, dirs, files in os.walk('yararules'):
    for file in files:
        filepaths[file] = os.path.join(root, file)