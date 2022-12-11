from moviepy.editor import AudioFileClip, ImageClip
from moviepy.editor import *

def add_static_image_to_audio(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(f'Audio/{audio_path}')

    image_clip = ImageClip(f'images/{image_path}')

    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    video_clip.write_videofile(f'Videos/{output_path}')


def combine_videos(video1, video2):
    clip = VideoFileClip(f'Videos/{video1}')
    clipx = VideoFileClip(video2)
    clips = [clip, clipx]
    final = concatenate_videoclips(clips)
    final.write_videofile(f'Videos/{video1}')

