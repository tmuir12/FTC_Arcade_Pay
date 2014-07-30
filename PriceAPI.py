import requests
    #gets the number of FTC required for 1 credit based on Fiat Cost in main.py
def toFTC(c,v,j='0'):
    payload = {'output': 'ftc'+c, 'amount': v, 'json': j}
    to_ftc_url = 'http://api.feathercoin.com/'
    ftotal=-1
    try:
        r = requests.get(to_ftc_url, params=payload)
        
        if r.status_code == 200:
            ftotal = round(float(r.text) ,4)
    except:
        pass
    return ftotal
