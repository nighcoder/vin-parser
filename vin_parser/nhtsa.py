import requests as req

def lookup(vin, timeout=2):
    '''Queries the vin on NHTSA Vehicle API database.
    Returns a dict with the details or None'''
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/" + vin + "?format=json"
    try:
        r = req.get(url, timeout)
    except req.Timeout:
        print("Connection timeout")
        return None

    data = r.json()
    if data.get("Results"):
        res = data["Results"][0]
        return {k: res[k] for k in res.keys() if res[k]}
