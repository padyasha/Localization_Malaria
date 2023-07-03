# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:34:47 2019

@author: pattanai
"""

import os, shutil

path_input="//PAT11383/BDD malaria/dataset"
path_output="M:/dataset"
root="KPJ0/G/RAW_0"
folders=os.listdir(os.path.join(path_input,root))
for folder in folders:
    if os.path.exists(os.path.join(path_output,root)) or 'tophat' in folder:
        pass
    else:
        shutil.copytree(os.path.join(path_input,root,folder), os.path.join(path_output, root, folder))