import requests
from time import sleep


# Request library
def request(username):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = (f'https://www.instagram.com/{username}/channel/?__a=1')
    r = requests.get(url, headers=headers)
    print(str(r.status_code) + " " + username)
    if r.status_code == 404:
        # Free
        return True
    if r.status_code == 200:
        # Taken
        return False


fileName = 'generated2.txt'
with open(fileName, 'r') as f:
    print(f'Text file reached! ({fileName})')
    for line in f:
        username = request(str(line[:-1]))
        if username is True:
            sleep(1)
            pass
