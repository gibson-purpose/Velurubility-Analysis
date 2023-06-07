#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib

def scan_file(file_path):
    # Open the file and calculate its SHA-256 hash
    with open(file_path, 'rb') as f:
        data = f.read()
        file_hash = hashlib.sha256(data).hexdigest()

    # Compare the file's hash against a database of known malicious hashes
    if file_hash in malicious_hashes:
        print(f'{file_path} is infected with a virus!')
    else:
        print(f'{file_path} is clean.')

# Usage
scan_file('example.exe')

