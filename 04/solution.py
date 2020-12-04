import re

class Passport:
    def __init__(self, **kwargs):
        self.byr = kwargs.get('byr','')
        self.iyr = kwargs.get('iyr','')
        self.eyr = kwargs.get('eyr','')
        self.hgt = kwargs.get('hgt','')
        self.hcl = kwargs.get('hcl','')
        self.ecl = kwargs.get('ecl','')
        self.pid = kwargs.get('pid','')
        self.cid = kwargs.get('cid','')
    
    def is_weakly_valid(self):
        return bool(
            self.byr and 
            self.iyr and 
            self.eyr and 
            self.hgt and 
            self.hcl and 
            self.ecl and 
            self.pid
        )
            
    def is_strictly_valid(self):
        return bool(
            self.validate_byr() and
            self.validate_iyr() and
            self.validate_eyr() and
            self.validate_hgt() and
            self.validate_hcl() and
            self.validate_ecl() and
            self.validate_pid() and
            self.validate_cid()
        )

    def validate_byr(self):
        if not re.match(r'^\d{4}$', self.byr):
            return False
        return 1920 <= int(self.byr) <= 2002

    def validate_iyr(self):
        if not re.match(r'^\d{4}$', self.iyr):
            return False
        return 2010 <= int(self.iyr) <= 2020
    
    def validate_eyr(self):
        if not re.match(r'^\d{4}$', self.eyr):
            return False
        return 2020 <= int(self.eyr) <= 2030
        
    def validate_hgt(self):
        if not re.match(r'^\d{3}cm$|^\d{2}in$', self.hgt):
            return False
        if 'cm' in self.hgt:
            return 150 <= int(self.hgt[:3]) <= 193
        if 'in' in self.hgt:
            return 59 <= int(self.hgt[:2]) <= 76

    def validate_hcl(self):
        return re.match(r'^#[0-9A-Fa-f]{6}$', self.hcl)

    def validate_ecl(self):
        return self.ecl in (
            'amb',
            'blu', 
            'brn', 
            'gry', 
            'grn', 
            'hzl', 
            'oth'
        )
    
    def validate_pid(self):
        return re.match(r'^\d{9}$', self.pid)

    def validate_cid(self):
        return True

def parse_pp_string(pp_string):
    pp_arr = pp_string.replace('\n', ' ').replace(':',' ').split(' ')
    pp_obj = {}
    while pp_arr:
        k = pp_arr.pop(0)
        v = pp_arr.pop(0)
        pp_obj[k] = v
    return Passport(**pp_obj)

with open('input.txt','r') as f:
    pp_strings = f.read().split("\n\n")

passports = [parse_pp_string(x) for x in pp_strings]

print("Part 1: ", sum(x.is_weakly_valid() for x in passports))
print("Part 2: ", sum(x.is_strictly_valid() for x in passports))