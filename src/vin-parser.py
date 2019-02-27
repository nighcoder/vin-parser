# VIN parser - library to parse VIN strings
from functools import reduce
from operator import add

CHARS = "ABCDEFGHJKLMNPRSTUVWXYZ1234567890"

def vin_check (vin):
    vin = vin.upper()
    vals = {k:v for k, v in zip(CHARS, list(range(1,9)) + list(range(1,6)) + [7, 9] + list(range(2,10)) + list(range(1,10)) + [0])}
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    s = reduce(add, [vals[c] * w for c, w in zip(vin, weights)])
    check_digit = s % 11
    if check_digit == 10:
        check_digit = "X"
    return str(check_digit) == vin[8]

def continent (vin):
    x = vin[0].upper()
    if x in CHARS[:8]:  # "ABCDEFGH"
        return "Africa"
    elif x in CHARS[8:15]: # "JKLMNPR"
        return "Asia"
    elif x in CHARS[15:23]: # "STUVWXYZ"
        return "Europe"
    elif x in CHARS[23:28]: # "12345"
        return "North America"
    elif x in CHARS[28:30]: # "67"
        return"Oceania"
    elif x in CHARS[30:32]: # "89"
        return "South America"

def country (vin):
    vin = vin.upper()
    ch1 = vin[0]
    ch2 = vin[1]

    # Africa
    if ch1 == "A": 
        if ch2 in CHARS[:8]:
            return "South Africa"
        elif ch2 in CHARS[8:13]:
            return "Cote d'Ivoire"
        elif ch2 in CHARS[13:]:
            return "unassigned"
    elif ch1 == "B":
        if ch2 in CHARS[:5]:
            return "Angola"
        elif ch2 in CHARS[5:10]:
            return "Kenya"
        elif ch2 in CHARS[10:15]:
            return "Tanzania"
        elif ch2 in CHARS[15:]:
            return "unassigned"
    elif ch1 == "C":
        if ch2 in CHARS[:5]:
            return "Benin"
        elif ch2 in CHARS[5:10]:
            return "Madagascar"
        elif ch2 in CHARS[10:15]:
            return "Tunisia"
        elif ch2 in CHARS[15:]:
            return "unassigned"
    elif ch1 == "D":
        if ch2 in CHARS[:5]:
            return "Egypt"
        elif ch2 in CHARS[5:10]:
            return "Morocco"
        elif ch2 in CHARS[10:15]:
            return "Zambia"
        elif ch2 in CHARS[15:]:
            return "unassigned"
    elif ch1 == "E":
        if ch2 in CHARS[:5]:
            return "Ethiopia"
        elif ch2 in CHARS[5:10]:
            return "Mozambique"
        elif ch2 in CHARS[10:]:
            return "unassigned"
    elif ch1 == "F":
        if ch2 in CHARS[:5]:
            return "Ghana"
        elif ch2 in CHARS[5:10]:
            return "Nigeria"
        elif ch2 in CHARS[10:]:
            return "unassigned"
    elif ch1 in CHARS[6:8]:
        return "unassigned"
 
    # Asia
    elif ch1 == "J":
         return "Japan"
    elif ch1 == "K":
        if ch2 in CHARS[:5]:
            return "Sri Lanka"
        elif ch2 in CHARS[5:10]:
            return "Israel"
        elif ch2 in CHARS[10:15]:
            return "South Korea"
        elif ch2 in CHARS[15:]:
            return "Kazakhstan"
    elif ch1 == "L":
        return "China"
    elif ch1 == "M":
        if ch2 in CHARS[:5]:
            return "India"
        elif ch2 in CHARS[5:10]:
            return "Indonesia"
        elif ch2 in CHARS[10:15]:
            return "Thailand"
        elif ch2 in CHARS[15:]:
            return "Myanmar"
    elif ch1 == "N":
        if ch2 in CHARS[:5]:
            return "Iran"
        elif ch2 in CHARS[5:10]:
            return "Pakistan"
        elif ch2 in CHARS[10:15]:
            return "Turkey"
        elif ch2 in CHARS[15:]:
            return "unassigned"       
    elif ch1 == "P":
        if ch2 in CHARS[:5]:
            return "Philippines"
        elif ch2 in CHARS[5:10]:
            return "Singapore"
        elif ch2 in CHARS[10:15]:
            return "Malaysia"
        elif ch2 in CHARS[15:]:
            return "unassigned"        
    elif ch1 == "R":
        if ch2 in CHARS[:5]:
            return "United Arab Emirates"
        elif ch2 in CHARS[5:10]:
            return "Taiwan"
        elif ch2 in CHARS[10:15]:
            return "Vietnam"
        elif ch2 in CHARS[15:]:
            return "Saudi Arabia"        

    # Europe
    elif ch1 == "S":
        if ch2 in CHARS[:12]:
            return "United Kingdom"
        elif ch2 in CHARS[12:17]:
            return "Germany (East)" # Is it still in use?!
        elif ch2 in CHARS[17:23]:
            return "Poland"
        elif ch2 in CHARS[23:27]:
            return "Latvia"
        elif ch2 in CHARS[27:]:
            return "unassigned"
    elif ch1 == "T":
        if ch2 in CHARS[:8]:
            return "Switzerland"
        elif ch2 in CHARS[8:14]:
            return "Czech Republic"
        elif ch2 in CHARS[14:19]:
            return "Hungary"
        elif ch2 in CHARS[19:24]:
            return "Portugal"
        elif ch2 in CHARS[24:]:
            return "unassigned"
    elif ch1 == "U":
        if ch2 in CHARS[:7] or ch2 in CHARS[23:27] or ch2 in CHARS[30:]:
            return "unassigned"
        elif ch2 in CHARS[7:12]:
            return "Denmark"
        elif ch2 in CHARS[12:17]:
            return "Ireland"
        elif ch2 in CHARS[17:23]:
            return "Romania"
        elif ch2 in CHARS[27:30]:
            return "Slovakia"
    elif ch1 == "V":
        if ch2 in CHARS[:5]:
            return "Austria"
        elif ch2 in CHARS[5:15]:
            return "France"
        elif ch2 in CHARS[15:20]:
            return "Spain"
        elif ch2 in CHARS[20:25]:
            return "Serbia"
        elif ch2 in CHARS[25:28]:
            return "Croatia"
        elif ch2 in CHARS[28:]:
            return "Estonia"
    elif ch1 == "W":
        return "Germany"
    elif ch1 == "X":
        if ch2 in CHARS[:5]:
            return "Bulgaria"
        elif ch2 in CHARS[5:10]:
            return "Greece"
        elif ch2 in CHARS[10:15]:
            return "Netherlands"
        elif ch2 in CHARS[15:20] or ch2 in CHARS[25:]:
            return "Russia"
        elif ch2 in CHARS[20:25]:
            return "Luxembourg"
    elif ch1 == "Y":
        if ch2 in CHARS[:5]:
            return "Belgium"
        elif ch2 in CHARS[5:10]:
            return "Finland"
        elif ch2 in CHARS[10:15]:
            return "Malta"
        elif ch2 in CHARS[15:20]:
            return "Sweden"
        elif ch2 in CHARS[20:25]:
            return "Norway"
        elif ch2 in CHARS[25:28]:
            return "Belarus"
        elif ch2 in CHARS[28:]:
            return "Ukraine"
    elif ch1 == "Z":
        if ch2 in CHARS[:15]:
            return "Italy"
        elif ch2 in CHARS[15:20] or ch2 in CHARS[28:]:
            return "unassigned"
        elif ch2 in CHARS[20:25]:
            return "Slovenia"
        elif ch2 in CHARS[25:28]:
            return "Lithuania"

    # North America
    elif ch1 in "145":
        return "United States"
    elif ch1 == "2":
        return "Canada"
    elif ch1 == "3":
        if ch2 in CHARS[:20]:
            return "Mexico"
        elif ch2 in CHARS[20:30]:
            return "Costa Rica"
        elif ch2 in CHARS[30:32]:
            return "Cayman Islands"
        elif ch2 == "0":
            return "unassigned"

    # Oceania
    elif ch1 == "6":
        return "Australia"
    elif ch1 == "7":
        return "New Zealand"
    
    # South America
    elif ch1 == "8":
        if ch2 in CHARS[:5]:
            return "Argentina"
        elif ch2 in CHARS[5:10]:
            return "Chile"
        elif ch2 in CHARS[10:15]:
            return "Ecuador"
        elif ch2 in CHARS[15:20]:
            return "Peru"        
        elif ch2 in CHARS[20:25]:
            return "Venezuela"
        elif ch2 in CHARS[25:]:
            return "unassigned"
    elif ch1 == "9":
        if ch2 in CHARS[:5] or ch2 in CHARS[25:32]:
            return "Brazil"
        elif ch2 in CHARS[5:10]:
            return "Colombia"
        elif ch2 in CHARS[10:15]:
            return "Paraguay"
        elif ch2 in CHARS[15:20]:
            return "Uruguay"        
        elif ch2 in CHARS[20:25]:
            return "Trinidad & Tobago"
        elif ch2 == "0": 
            return "unassigned"

def year (vin):
    vin = vin.upper()
    year_ch = (c for c in CHARS if c not in "UZ0")
    if vin[6] in CHARS[:23]: # char 7 in VIN is a letter
        years = range(2010, 2040)
    else:
        years = range(1980, 2010)
    for c in zip(year_ch, years):
        if c[0] == vin[9]:
            return c[1]

def is_valid (vin):
    vin = vin.upper()
    return len(vin) == 17 and\
           vin[0] != "0" and\
           set(vin).issubset(set(CHARS)) and\
           vin[9] not in "ZU0" and\
           country(vin) != "unassigned"

def wmi (vin):
    vin = vin.upper()
    if vin[3] == "9":
        return vin[:2]
    else:
        return vin[:3]

def vis (vin):
    vin = vin.upper()
    return vin[9:]

def parse (vin):
    r = {}
    if is_valid(vin):
        r["continent"] = continent(vin)
        r["country"] = country(vin)
        r["year"] = year(vin)
        r["check"] = vin_check(vin)
        return r
    else:
        return None
