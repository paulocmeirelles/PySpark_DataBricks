import re

def mask_local_part(string):
    times = string.index('@')
    return re.sub('(^[^@]*)',times*'*',string)