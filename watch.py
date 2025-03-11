#!/path/to/venv/bin/python3.12
import re
import csv
from io import StringIO
import sys
import yaml
import subprocess
import os

import logging
from systemd import journal

log = logging.getLogger(os.path.basename(__file__))
log.addHandler(journal.JournaldLogHandler())
log.setLevel(logging.INFO)

try:
    config_file = sys.argv[1]
except IndexError as e:
    print("Required argument not specified")
    sys.exit(1)
try: 
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
except FileNotFoundError as e:
    print(f"Config file not found: {config_file}")
    sys.exit(1)
for line in sys.stdin:
    reader = csv.reader(StringIO(line))
    for row in reader:
        d = row[0]
        e = row[1].split(",")
        f = row[2]
    if 'CLOSE_WRITE' in e:
        for rule in config['actions']['updated']:
            if re.search(rule['pattern'], f):
                log.info(f"file: {os.path.join(d,f)} cmd:{rule['command']}")
                p = subprocess.run([rule['command']],input=os.path.join(d,f).encode(), capture_output=True)
                log.info(p.stdout.decode())


