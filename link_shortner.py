import requests

API_KEY = '7e243f3f38bafb75e656a253159b2210a3088'
BASE_url = 'https://cutt.ly/api/api.php'

long_url = input('What is the long URL you want to shorten?: ')
alias_url = input('What is the alias you want to use for your short URL (cutt.ly/alias)?: ')


def shorten_url(long_url, alias_url):
    
    params = {
        'key': API_KEY,
        'short': long_url,
        'name': alias_url
    }
    
    request = requests.get(BASE_url, params=params)
    data = request.json()
    
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print('Title: ', title)
        print('Short link: ', short_link)
    except:
        status = data['url']['status']
        if status == 3:
            status = 'Alias is already taken'
        print('Error Status: ', status)
        
shorten_url(long_url, alias_url)
    