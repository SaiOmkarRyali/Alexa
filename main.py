import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('    I am your Alexa')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def send_email(recevier,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('saiomkar.rali@gmail.com', 'ifqgygrhahvdkspp')
    email = EmailMessage()
    email['From'] = 'saiomkar.rali@gmail.com'
    email['To'] = recevier
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'ashrif':'ashrif210700@gmail.com',
    'alisha':'alishashaik360@gmail.com',
    'lalli':'sailalithajyothit@gmail.com',
    'pawan':'varma.penmetsa1789@gmail.com',
    'omkar':'saiomkar2001@gmail.com',
    'teju':'stejasri129@gmail.com'

}

def get_email_info():
    talk('To Whom You Want to Send Email')
    name = take_command()
    receiver = email_list[name]
    print(receiver)
    talk('what is the Subject of your email')
    subject = take_command()
    print(subject)
    talk('Tell me the text in your email')
    message = take_command()
    print(message)

    send_email(receiver,subject,message)

def run_alexa():
    command = take_command()
    print(command)
    if 'play ' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    if 'show me about' in command:
        keyword = command.replace('show me about', '')
        talk(' displaying' + keyword)
        pywhatkit.search(keyword)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info1 = wikipedia.summary(person, 3)
        print(info1)
        talk(info1)
    elif 'date' in command:
        talk('yes,i am waiting for this moment')
    elif 'message' in command:
        if 'daddy' in command:
            pywhatkit.sendwhatmsg('+919247857883', 'hiiiiii', 22,44)
        elif 'amma' in command:
            pywhatkit.sendwhatmsg('+919966486661', 'hiiiiii', 22, 44)
        else:
            pass
    elif 'love' in command:
        talk('i love u 3000')
        print('i love u 3000')
    elif 'are you single' in command:
        talk('yeah...waiting to mingle with u')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'mail' in command:
        get_email_info()

    else:
        talk('Please say the command again.')


while True:
    run_alexa()