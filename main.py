import pyttsx3

# Force Windows Speech API (avoids espeak issues)
engine = pyttsx3.init('sapi5')

print("Hello, I am Robo Speaker. How can I help you?")

while True:
    text = input("Enter the sentence you want me to speak (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        engine.say("Goodbye! Have a nice day.")
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()
