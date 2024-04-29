import re
import requests
import quiz28 as q28

def get_flag_url():
    d = q28.remove_markups()['国旗画像']
    url = 'https://www.mediawiki.org/w/api.php'
    params = {'action': 'query',
              'titles': f'File:{d}',
              'format': 'json',
              'prop': 'imageinfo',
              'iiprop': 'url'}
    res = requests.get(url, params)

    return res.json()['query']['pages']['-1']['imageinfo'][0]['url']



if __name__ == "__main__":
    text = get_flag_url()
    print(text)