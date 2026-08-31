
gTTS Text-to-Speech Project
A simple Python project that converts text into speech using gTTS (Google Text-to-Speech).

1. Create Virtual Environment
py -3.13 -m venv .venv
alt text

2. Activate the Environment
.venv\Scripts\Activate.ps1
You should see (.venv) in the terminal.

alt text
3. Install gTTS
python -m pip install --upgrade pip
python -m pip install gTTS
alt text alt text
4. Create main.py
from gtts import gTTS

text = ("Long live Verventech.Hello, welcome to my Python project!")

tts = gTTS(text=text, lang="en")
tts.save("hello.mp3")

print("Audio created successfully!")
alt text

5. Run the Project
python main.py
Output
Audio created successfully!
The program will create an audio file:

hello.mp3
alt text
Project Structure
gtts-project/
│
├── .venv/
├── main.py
├── hello.mp3
└── README.md


