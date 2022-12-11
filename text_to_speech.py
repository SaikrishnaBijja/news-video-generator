import pyttsx3
from pydub import AudioSegment

def text_to_speech(texter, audio_file_name):
    engine = pyttsx3.init() # object creation

    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 170)     # setting up new voice rate

    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',0.9)    # setting up volume level  between 0 and 1

    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.save_to_file(texter, f'Audio/{audio_file_name}')
    engine.runAndWait()


def combine_audio(audio_file_name):
    bg="base_files/bg.wav"
    sound1 = AudioSegment.from_file(bg)
    sound2 = AudioSegment.from_file(audio_file_name)
    combined = sound2.overlay(sound1)

    combined.export(audio_file_name, format='wav')

def merge_audio(audio1, audio2, outpath):
    import wave
    import soundfile

    infiles = [f"Audio/{audio1}", f"Audio/{audio2}"]
    outfile = f"Audio/{outpath}"
    
    for file in infiles:
        data, samplerate = soundfile.read(file)
        soundfile.write(file, data, samplerate)

    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
        
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()


