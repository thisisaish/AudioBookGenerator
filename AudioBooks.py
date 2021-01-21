# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:32:52 2021

@author: Aishwarya Murali
"""

from gtts import gTTS
import codecs

file = codecs.open("The case of natty nat.txt","r","utf-8")
#print(file.read())
content = file.read()
#content = "Hello, there!"
tts = gTTS(content, lang='en')
tts.save('my audio book.mp3')
print("Cheers!!! your audio book for \'The case of natty nat\' has been created successfully.")