import datetime, gtts, bs4, random
import speech_recognition as sr

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    text = f"The current time is {time_str}."
    tts = gtts.gTTS(text, lang=lang)
    tts.save(filename)
    
def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!"
    ]
    joke = random.choice(jokes)
    tts = gtts.gTTS(joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    now = datetime.datetime.now()
    day_str = now.strftime("%A, %B %d, %Y")
    text = f"Today is {day_str}."
    tts = gtts.gTTS(text, lang=lang)
    tts.save(audiofile)
    calendar_url = f"https://www.calendar.com/{now.year}/{now.month}"
    return calendar_url

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language=lang)
            print(f"Command received: {command}")

            if "time" in command.lower():
                what_time_is_it(lang, filename)
            elif "day" in command.lower():
                what_day_is_it(lang, filename)
            elif "joke" in command.lower():
                tell_me_a_joke(lang, filename)
            else:
                print("I didn't understand that command.")
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
