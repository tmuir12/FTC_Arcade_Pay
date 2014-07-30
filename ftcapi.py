import requests
    #returns balance of feathercoin address
   
    
def toFTC( a,j='0'):
    payload = {'output': 'balance','address': a,'json': j}
    to_ftc_url = 'http://api.feathercoin.com/'
    ftotal=-1 # sets ftotal to -1 so it will return -1 an impossible balance
    #if API is offline
    try:
        r = requests.get(to_ftc_url, params=payload)

        if r.status_code == 200:
            ftotal = round(float(r.text) ,8)
    except:
        pass
    return ftotal
