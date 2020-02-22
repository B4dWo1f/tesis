#!/usr/bin/python3
# -*- coding: UTF-8 -*-

fname = 'all_bib.bib'

entries = open(fname,'r').read().strip()

entries = entries.split('@')
entries = ['@'+E.strip() for E in entries]
entries = [E for E in entries if len(E)>1]

for E in entries:
   print(E)
   exit()
