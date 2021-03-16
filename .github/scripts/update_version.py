import re
import pathlib

current_path = str(pathlib.Path(__file__).parent.absolute())

with open(current_path+'/../../setup.py') as f:
    lines = f.readlines()
    version_line = lines[0]
    version = float(''.join(re.findall("'(.*?)'", version_line)))

lines[0] = f"VERSION = '{(version + 0.01):.2f}'\n"

with open(current_path+'/../../setup.py', 'w') as f:
    f.writelines(lines)

with open(current_path+'/version.env', 'w') as f:
    f.writelines(f"VERSION={(version + 0.01):.2f}")