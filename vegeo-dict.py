#!/usr/bin/env python3

import yaml
import sys
import os

dictName = 'vegeo-dict.yml'
fullDictName = os.path.join(os.path.dirname(os.readlink(sys.argv[0])), dictName)

vDict = yaml.safe_load(open(fullDictName))

if len(sys.argv) == 2:
    abb = sys.argv[1].upper()
else:
    raise ValueError('ERROR: this script needs exactly one argument')

if abb in vDict:
    print(vDict[abb])
else:
    print(f'Sorry, {abb} is contained in this dictionary.')

