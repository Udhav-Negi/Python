# Shoutouts to Everyone 
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
lst = ["first", "second", "third", "fourth"]
for item in lst:
    speaker.Speak(item)