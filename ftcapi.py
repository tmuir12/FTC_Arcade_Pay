import requests
    #returns balance of feathercoin address
   
    
def toFTC( v='6oQqqYYPvnPRukPp2qiEWVzMkHnqCx2VKn',j='0'): #insert your feathercoin address here
    payload = {'output': 'balance','address': v,'json': j}
    to_ftc_url = 'http://api.feathercoin.com/'
    ftotal=-1 
    try:
        r = requests.get(to_ftc_url, params=payload)

        if r.status_code == 200:
            ftotal = round(float(r.text) ,8)
    except:
        pass
    return ftotal
