import gtts

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
    except Exception as e:
        print(f'An error occurred: {e}')

import homework12, librosa, IPython, importlib
importlib.reload(homework12)

homework12.synthesize("This is speech synthesis!","en","english.mp3")
y, sr = librosa.load("english.mp3")
IPython.display.Audio(data=y, rate=sr)
