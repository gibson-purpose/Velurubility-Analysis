#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import hashlib


# In[2]:


def get_file_hash(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        # read contents of the file
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex representation of hash
    return h.hexdigest()


# In[3]:


virus_hashes = ['8b1a9953c4611296a827abf8c47804d7', 'cc3a3e6d5c0a3c5a36dda3d73b7d4848']


# In[4]:


def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash in virus_hashes:
                print(f'Virus detected: {file_path}')


# In[5]:


scan_directory("C:\Data")


# In[ ]:




