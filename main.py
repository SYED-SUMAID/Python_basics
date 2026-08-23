from gtts import gTTS

text = "Long live Verventech. Welcome to my Python project."

tts = gTTS(text=text, lang="en")
tts.save("hello.mp3")

print("Audio created successfully!")