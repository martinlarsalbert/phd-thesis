"""
Module that cleans a bibtex file as a last option to fix it.
"""

import re
import logging
import bibtexparser
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


with open('library_raw.bib',mode='r', encoding='utf8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

def remove(id, field):
    if field in bib_database.entries_dict[id]:
        bib_database.entries_dict[id].pop(field)

logger.info(f'Remove note for all')
for id in bib_database.entries_dict.keys():
    remove(id, 'note')

logger.info(f'Remove publisher, except for books') 
for id,item in bib_database.entries_dict.items():
    if item['ENTRYTYPE']!='book':
        remove(id, 'publisher')

with open(r'library.bib',mode='w', encoding='utf8') as bibtex_file:
    bib_database = bibtexparser.dump(bib_database, bibtex_file)


"""
Lower case titles
Ex:
title = {Dynamics of a {Rigid} {Ship} - with applications}
change to:
title = {Dynamics of a {rigid} {ship} - with applications}
"""
with open('library.bib', mode='r', encoding='utf8') as file:
    s = file.read()
for result in re.finditer(r"title *= *\{(.*)\}", s):
    old = result.group(1)
    new = old[0].upper() + old[1:].lower()
    s = s.replace(old,new)

with open('library.bib', mode='w', encoding='utf8') as file:
    file.write(s)