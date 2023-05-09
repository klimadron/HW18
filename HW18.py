import requests
def get_status(sites):
    for x in sites:
        try:
            response = requests.get(x)
            response.raise_for_status()
            if response.status_code == 200:
                continue
        except:print(x,"Not 200")
urls = ["http://google.com","https://youtufdbe.com", "https://ukr.net/21312", "http://google.com/404", "httdsp://youtube.com" ,"http://google.com", "http://google.com", "http://google.codsadam/sdsad"]
get_status(urls)