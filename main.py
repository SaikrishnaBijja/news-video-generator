from datetime import datetime
from uuid import uuid4
import time
from image_manager import text_on_image,image_on_image,image_size_changer, download_image
from news_manager import get_news
from text_to_speech import  combine_audio, text_to_speech, merge_audio
from video_manager import add_static_image_to_audio, combine_videos
from telegram import send_telegram
import os
from keep_me_alive import keep_alive
from is_exist import to_enter
# news_catagory=['business','entertainment','general','health','science' ,'sports','technology']

from tiktok import tiktok_text_to_speech

# news_catagory=['sports','technolog', 'general', 'entertainment']
news_catagory=['sports']


def main(catagory, count):
    image_name=datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())+".png"
    audio_name=image_name.replace(".png", ".wav")
    video_name=image_name.replace(".png", ".mp4")
    title_audio_name=f"title_{audio_name}"
    content_audio_name=f"content_{audio_name}"

    news_data=get_news(catagory, count)
    print("Got the News Data")
    time.sleep(1)
    
    download_image(image_name, news_data)
    print("Downloaded image")
    time.sleep(1)

    tiktok_text_to_speech(text=str(news_data[0]), file_path=f'Audio/{title_audio_name}')
    tiktok_text_to_speech(text=str(news_data[3]), file_path=f'Audio/{content_audio_name}')
    # text_to_speech(to_read, audio_name)
    print("Audios Created")
    time.sleep(1)

    image_size_changer(image_name)
    print("Image Sized Changed")

    image_on_image(image_name, f'{catagory}_bg.jpg')
    print("Added Image to News")

    text_on_image(news_data, image_name)
    print("Text is written on image")
    
    merge_audio(title_audio_name, content_audio_name, audio_name)
    print("Merged Audio Of Tile and Content")
    
    combine_audio(f'Audio/{audio_name}')
    print("Combined Audios")
    
    add_static_image_to_audio(image_name, audio_name, video_name)
    print("News video created")
    time.sleep(1)

    combine_videos(video_name, f"base_files\{catagory}_subscribe.mp4")
    print("Final video Created")
    time.sleep(1)

    description=f'Thank you for watcing \nLink to article {news_data[1]} \nCopyrights 2022 https://newsapi.org'
    title=news_data[0]
    send_telegram(video_name, title, description, catagory)
    print("Video upload to Telegram")

    to_enter(news_data[0])

for x in range(1,7):
    for cat in news_catagory:
        main(cat, x)
    time.sleep(2)
    videos=os.listdir("Videos/")
    images=os.listdir("images/")
    audio=os.listdir("Audio/")

    # for x in videos:
    #     try:
    #         os.remove(f"Videos/{x}")
    #     except FileNotFoundError:
    #         pass
    # for y in images:
    #     try:
    #         os.remove(f"images/{y}")
    #     except FileNotFoundError:
    #         pass
    # for y in audio:
    #     try:
    #         os.remove(f"Audio/{y}")
    #     except FileNotFoundError:
    #         pass
    # time.sleep(8)