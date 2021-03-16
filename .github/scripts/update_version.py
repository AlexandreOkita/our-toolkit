import subprocess
import re
import fileinput

with open('../../setup.py') as f:
    lines = f.readlines()
    version_line = lines[0]
    version = float(''.join(re.findall("'(.*?)'", version_line)))

lines[0] = f"VERSION = '{(version + 0.01):.2f}'\n"

with open('../../setup.py', 'w') as f:
    f.writelines(lines)