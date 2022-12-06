import pyttsx3
import os.path
import keyboard

path = str(input("Enter the name of the file: "))
book = f"{path}.txt"
print(f"Reading file {book}")
bookopen = open(book)

if os.path.exists(f"{path}.txt"):
    print("Reading...")
else:
    print("Not found")
    
book_text = bookopen.readlines()
engine = pyttsx3.init()
newVoiceRate = 135

def read():
        for i in book_text:
            voice = engine.getProperty('voices')
            engine.setProperty('voice', voice[1].id) 
            engine.setProperty('rate',newVoiceRate)
            engine.say(i)
            engine.runAndWait()
            
read()
    
