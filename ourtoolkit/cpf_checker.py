import re
import sys


## This function verify if a given string is in
## the format XXX.XXX.XXX-XX

def cpf_checker(cpf: str) -> bool:
    rexp = re.compile(r'\d{3}.\d{3}.\d{3}-\d{2}')
    if rexp.match(cpf) and len(cpf) == 14:
        return True
    return False