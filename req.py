import requests
headers = {'User-Agent': 'Mozilla/5.0'}
def request(username): 
    url = f'https://www.instagram.com/{username}/channel/?__a=1'
    r = requests.get(url, headers=headers)
    print(r.text)
    if r.text == '{}':
        return True
    else:
        False