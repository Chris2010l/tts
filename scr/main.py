from gtts import gTTS
import os
from pathlib import Path


current_file = Path(__file__).resolve()
root_dir = current_file.parent.parent


class Sound:
    def __init__(self): # Gets prompt from txt file
        prompt_file = root_dir / "config" / "prompt.txt"
        print(prompt_file)
        print(root_dir)
        if prompt_file.exists():
            self.prompt = prompt_file.read_text()
        else:
            self.prompt = "DEFAULT"

    def create_output(self):
        tts = gTTS(text=self.prompt, lang="de", slow=False)
        tts.save(str( root_dir / "_output.mp3"))

    def repeat_output(self, amount: int):
        for i in range(amount):
            print(f"amount: {i + 1}")
            os.system("play -q _output.mp3") #Linux -> sox


sound = Sound()
sound.create_output()
sound.repeat_output(1)
