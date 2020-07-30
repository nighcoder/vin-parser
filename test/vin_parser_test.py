import sys, os
#os.chdir("./vin_parser")
sys.path.append(".")

import vin_parser as vp
from datetime import date

def assertion (func):
    def wrapped ():
        try:
            return func()
        except AssertionError as e:
            print(f"Test {func.__name__} failed at assertion: {e}")
    return wrapped

@assertion
def vin1 ():
    vin = "3C6LD5AT8CG295248"

    cont = vp.continent(vin)
    assert cont == "North America", f"continent({vin}) == North America, got {cont}"
    count = vp.country(vin)
    assert count == "Mexico", f"country({vin}) == Mexico. Got {count}"
    year = vp.year(vin)
    assert year == 2012, f"year({vin}) == 2012. Got {year}"
    manuf = vp.manuf(vin)
    assert manuf == "Chrysler Mexico", f"manuf({vin}) == Chrysler Mexico. Got {manuf}"
    wmi = vp.wmi(vin)
    assert wmi == "3C6", f"wmi({vin}) == 3C6. Got {wmi}"
    vis = vp.vis(vin)
    assert vis == "CG295248", f"vis({vin}) == CG295248. Got {vis}"
    assert vp.is_valid(vin), f"is_valid({vin})"

    return True

@assertion
def vin2():
    vin = "WAUAH74FX8N034074"

    cont = vp.continent(vin)
    assert cont == "Europe", f"continent({vin}) == Europe. Got {cont}"
    count = vp.country(vin)
    assert count == "Germany", f"country({vin}) == Germany. Got {count}"
    year = vp.year(vin)
    assert year == 2008, f"year({vin}) == 2008. Got {year}"
    manuf = vp.manuf(vin)
    assert manuf == "Audi", f"manuf({vin}) == Audi. Got {manuf}"
    wmi = vp.wmi(vin)
    assert wmi == "WAU", f"wmi({vin}) == WAU. Got {wmi}"
    vis = vp.vis(vin)
    assert vis == "8N034074", f"vis({vin}) == 8N034074. Got {vis}"
    assert vp.is_valid(vin), f"isvalid({vin})"

    return True

@assertion
def vin3 ():
    vin = "NM0KS9BN2CT099422"

    cont = vp.continent(vin)
    assert cont == "Asia", f"continent({vin}) == Europe. Got {cont}"
    count = vp.country(vin)
    assert count == "Turkey", f"country({vin}) == Turkey. Got {count}"
    year = vp.year(vin)
    assert year == 2012, f"year({vin}) == 2012. Got {year}"
    manuf = vp.manuf(vin)
    assert manuf == "Ford Turkey", f"manuf({vin}) == Ford Turkey. Got {manuf}"
    wmi = vp.wmi(vin)
    assert wmi == "NM0", f"wmi({vin}) == NM0. Got {wmi}"
    vis = vp.vis(vin)
    assert vis == "CT099422", f"vis({vin}) == CT099422. Got {vis}"
    assert vp.is_valid(vin), f"is_valid({vin})"

    return True

@assertion
def vin4 ():
    vin = "5TFRY5F16BX110655"
    rez = { 'check_no': '6',
            'check_valid': True,
            'continent': "North America",
            'country': "United States",
            'manufacturer': "Toyota USA - trucks",
            'seq_no': "110655",
            'small_manuf': False,
            'vds': "RY5F16",
            'vis': "BX110655",
            'wmi': "5TF",
            'year': 2011 }

    assert rez == vp.parse(vin), f"{vp.parse(vin)}"

    return True

@assertion
def years ():
    vinl = ["1GKKRNED9EJ262581", "2A4GP54L16R805929", "JM1BL1M72C1587426", "1FTEW1CM9BFA74557",
            "1FAFP34P63W132895", "1J4GL48K05W616251", "3VWDX7AJ2BM339496", "5LMJJ3J57EEL08671",
            "WMWMF7C56ATZ69847", "JTDKN3DU9F0421684", "3C3CFFAR2CT212308", "KNMCSHLMS6P600875",
            "Y7A6135B660801530", "TRUZZZSNZY1063363"]
    yearsl = [2014, 2006, 2012, 2011,
              2003, 2005, 2011, 2014,
              2010, 2015, 2012, 2006,
              2006, 2000]

    cur_year = date.today().year
    yearl = [vp.year(v) for v in vinl]

    assert max(yearl) <= cur_year, f"Model year is in the future"
    assert yearl == yearsl, f"Year list failed: {yearl} != {yearsl}"

    return True

def manufs ():
    vinl = ["1GKKRNED9EJ262581", "2A4GP54L16R805929", "JM1BL1M72C1587426", "1FTEW1CM9BFA74557",
            "1FAFP34P63W132895", "1J4GL48K05W616251", "3VWDX7AJ2BM339496", "5LMJJ3J57EEL08671",
            "WMWMF7C56ATZ69847", "JTDKN3DU9F0421684", "3C3CFFAR2CT212308", "KNMCSHLMS6P600875",
            "Y7A6135B660801530", "TRUZZZSNZY1063363"]
    resl = ["General Motors USA", "Chrysler Canada", "Mazda", "Ford Motor Company",
            "Ford Motor Company", "Jeep", "Volkswagen Mexico", "Lincoln", "MINI", "Toyota",
            "Chrysler Mexico", "Kia", "Kraz", "Audi Hungary"]

    for v in zip(vinl, resl):
        assert vp.manuf(v[0]) == v[1], f"Manuf({v[0]}) == {v[1]}"

    return True

def invalid ():
    vinl = ["", "AAA", "JM1BL1M72C158742", "1FTEW1CM9BFA745571",
            "VIN6135B660801530", "IOQZZZSNZY1063363"]

    for vin in vinl:

        cont = vp.continent(vin)
        assert cont == False, f"continent({vin}) == False. Got {cont}"
        count = vp.country(vin)
        assert count == False, f"country({vin}) == False. Got {count}"
        year = vp.year(vin)
        assert year == False, f"year({vin}) == False. False {year}"
        manuf = vp.manuf(vin)
        assert manuf == False, f"manuf({vin}) == False. Got {manuf}"
        wmi = vp.wmi(vin)
        assert wmi == False, f"wmi({vin}) == False. Got {wmi}"
        vis = vp.vis(vin)
        assert vis == False, f"vis({vin}) == False. Got {vis}"
        assert vp.is_valid(vin) == False, f"is_valid({vin})"
    return True
if __name__ == "__main__":
    ALL_TESTS = [vin1, vin2, vin3, vin4, years, manufs, invalid]
    i = 0
    for t in ALL_TESTS:
        if not t():
            i += 1
    if i == 0:
        print("All tests passed successfully")
    elif i == 1:
        print("One test failed")
    else:
        print(f"{i} tests failed")
    exit(min(i, 255))
