#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

def get_entry(key,fname='all_bib.bib'):
   com = f"grep -iA 50 {key} {fname}"
   ret = os.popen(com).read()
   try: return '@'+ret.split('@')[1].strip()
   except IndexError: 
      print(f'Entry {key} Not found')
      return None  #XXX raise

def get_url(key,fname='all_bib.bib'):
   entry = get_entry(key,fname=fname)
   if entry != None:
      for l in entry.splitlines():
         if ' url ' in l.lower() or l.lower().startswith('url'):
            return l.strip()
      print('URL not found')
      return None
   else: return None

com = 'grep "\\\cite" */*.tex'
cites = []
all_cites = os.popen(com).read().strip().splitlines()
for line in all_cites:
   if 'graphene_vacancy/vacancy_' in line: continue
   line = line.split('%')[0]
   for L in line.split('\cite')[1:]:
      cites_line = L.split('{')[1].split('}')[0]
      cites += [c.strip() for c in cites_line.split(',')]

cites = list(set(cites))
cites = [c for c in cites if len(c)>0]
articles = []
for c in cites:
   entry = get_entry(c)
   if '@article' in entry:
      articles.append(c)

cont = 0
for cite in articles:
   url = get_url(cite)
   if not 'arxiv' in url:
      print('\nDoing',cite)
      print(url)
      cont += 1

print(f'\n\n{cont} papers without arxiv')
