import json_lines
import time

with open('nguoiduatin_phapluat.json', 'rb') as f:
    for item in json_lines.reader(f):
        print(item['content'])
        time.sleep(5)


