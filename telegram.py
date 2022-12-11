import requests
import urllib3
import time

api='5055046495:AAHuvPRrZuCvxM7IHrGNrPDqROu8QZNvLl8'
chat_ids={
    "business":"1001666970594",
    'entertainment':'1001844605747',
    'general':'1001886846036',
    'health':'1001195131350',
    'science':'1001818078907',
    'sports':'1001536598729',
    'technology':'1001703209615'
}

def send_telegram(video, title, discription, catagory):
    file={"video":open(f'Videos/{video}', 'rb')}
    divider='●▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬●'
    try:
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={divider}')
        requests.post(f'https://api.telegram.org/bot{api}/sendVideo?chat_id=-{chat_ids[catagory]}', files=file)
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={title}')
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={discription}')

    except (urllib3.exceptions.MaxRetryError, requests.exceptions.SSLError):
        time.sleep(19)
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={divider}')
        requests.post(f'https://api.telegram.org/bot{api}/sendVideo?chat_id=-{chat_ids[catagory]}', files=file)
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={title}')
        requests.get(f'https://api.telegram.org/bot{api}/sendMessage?chat_id=-{chat_ids[catagory]}&text={discription}')
