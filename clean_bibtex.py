import re
import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

with open('library_raw.bib', mode='r', encoding='utf8') as file:
    s = file.read()

removes = ['publisher','note']

for remove in removes:
    logger.info(f'remove {remove}')
    s = re.sub(remove + r' *= .*\{.+\}','',s)

with open('library.bib', mode='w', encoding='utf8') as file:
    file.write(s)