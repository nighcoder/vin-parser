import sys, os
sys.path.append(os.getcwd() + "/vin_parser")
import vin_parser as vp

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

    assert vp.continent(vin) == "North America", f"continent({vin}) == North America"
    assert vp.country(vin) == "Mexico", f"country({vin}) == Mexico"
    assert vp.year(vin) == 2012, f"year({vin}) == 2012"
    assert vp.wmi(vin) == "3C6", f"wmi({vin}) == 3C6"
    assert vp.vis(vin) == "CG295248", f"vis({vin}) == CG295248"
    assert vp.is_valid(vin), f"is_valid({vin})"

    return True

if __name__ == "__main__":
    i = 0
    if not vin1():
        i += 1
    exit(min(i, 255))

