#!/usr/bin/env python3

from yaml import safe_load
from sys import argv
from os import path as op
from os import readlink

dictName = 'vegeo-dict.yml'
fullDictName = op.join(op.dirname(readlink(argv[0])), dictName)

vDict = safe_load(open(fullDictName))

if len(argv) == 2:
    abb = argv[1].upper()
else:
    raise ValueError('ERROR: this script needs exactly one argument')

if abb in vDict:
    print(vDict[abb])
else:
    print(f'Sorry, {abb} is contained in this dictionary.')

