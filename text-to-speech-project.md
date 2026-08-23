# gTTS Text-to-Speech Project

A simple Python project that converts text into speech using **gTTS (Google Text-to-Speech)**.

## 1. Create Virtual Environment

```bash
py -3.13 -m venv .venv
```
![alt text](<Screenshot (591).png>)

---

## 2. Activate the Environment

```powershell
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` in the terminal.

![alt text](<Screenshot (592).png>)
---

## 3. Install gTTS

```powershell
python -m pip install --upgrade pip
python -m pip install gTTS
```

![alt text](<Screenshot (594).png>)
![alt text](<Screenshot (595).png>)
---

## 4. Create `main.py`

```python
from gtts import gTTS

text = ("Long live Verventech.Hello, welcome to my Python project!")

tts = gTTS(text=text, lang="en")
tts.save("hello.mp3")

print("Audio created successfully!")
```

![alt text](<Screenshot (596).png>)

---

## 5. Run the Project

```powershell
python main.py
```

### Output

```text
Audio created successfully!
```

The program will create an audio file:

```text
hello.mp3
```

![alt text](<Screenshot (597)-1.png>)
---

## Project Structure

```text
gtts-project/
│
├── .venv/
├── main.py
├── hello.mp3
└── README.md
```
