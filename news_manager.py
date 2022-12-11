import requests
from is_exist import is_exit, to_enter

def get_news(catagory, count):
    def news_info(x, response):
        new_data=[]
        new_data.append(response["articles"][x]["title"])
        new_data.append(response["articles"][x]['url'])
        new_data.append(response["articles"][x]['urlToImage'])
        try:
            new_data.append(response["articles"][x]['content'].split("[")[0])
        except AttributeError:
            new_data.append(response["articles"][x]['content'])
        return new_data
    news_api="bf2fed53a8ce42ba97ec24892cd35ea9"
    end_point="https://newsapi.org/v2/top-headlines"
    headers={
        "X-Api-Key": news_api
    }

    params={
        "language":"en",
        "category":catagory,
        "pageSize":99
    }
    response = requests.get(end_point, headers=headers, params=params)
    response = response.json()
    for count in range(99):
        try:
            if len(response["articles"][count]["title"]) > 15 and len(response["articles"][count]['url']) > 15 and len(response["articles"][count]['urlToImage']) > 15 and len(response["articles"][count]['content']) > 15:
                if is_exit(response["articles"][count]["title"]):
                    return news_info(count, response)
        except TypeError:
            pass


def split_string(text, title):
    if title == "title":
        count=31
    else:
        count=38   
    for x in range(1, len(text)):
        try: 
            if x % count == 0:
                if text[x] == " " or text[x] == ",":
                    text = list(text)
                    text[x] = '\n'
                    text = ''.join(text)
                else:
                    do_again=True
                    for z in range(5):
                        if text[x+z] == " ":
                            text = list(text)
                            text[x+z] = '\n'
                            text = ''.join(text)
                            do_again=False
                            break
                    if do_again:
                        for k in range(5):
                            if text[x-k] == " ":
                                text = list(text)
                                text[x-k] = '\n'
                                text = ''.join(text)
                                break            
        except IndexError:
            pass
    texts = text.split("\n")
    return texts


