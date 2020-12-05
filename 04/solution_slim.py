import re
from collections import defaultdict

def has_valid_keys(pp):
    return all(x in pp.keys() for x in (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
     ))

def has_valid_values(pp):
    return all((
        re.match(r'^19[2-9][0-9]$|^200[0-2]$', pp['byr']),
        re.match(r'^201[0-9]$|^2020$', pp['iyr']),
        re.match(r'^202[0-9]$|^2030$', pp['eyr']),
        validate_hgt(pp['hgt']),
        re.match(r'^#[0-9a-f$]{6}', pp['hcl']),
        pp['ecl'] in ('amb','blu','brn','gry','grn','hzl','oth'),
        re.match(r'^\d{9}$', pp['pid'])
    ))

def validate_hgt(v):
    if not re.match(r'^\d{3}cm$|^\d{2}in$', v):
        return False
    if 'cm' in v:
        return 150 <= int(v[:3]) <= 193
    if 'in' in v:
        return 59 <= int(v[:2]) <= 76


with open('input.txt','r') as f:
    pp_strings = f.read().split("\n\n")

def parse(pp_string):
    passport = defaultdict(lambda:'')
    for k, v in re.findall(r'(\w+):(#?\w*\d*)', pp_string):
        passport[k] = v
    return passport

passports = [parse(s) for s in pp_strings]

print("Part 1: ", sum(has_valid_keys(pp) for pp in passports))
print("Part 2: ", sum(has_valid_values(pp) for pp in passports))
