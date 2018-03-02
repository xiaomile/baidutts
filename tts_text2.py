#author:X-mile
from baidu_tts import baiduTTS
import pyaudio
import wave
from pydub import AudioSegment
import os

tts = baiduTTS()

tts.save_file()
#print('here')
song = AudioSegment.from_mp3(tts.filename)
song.export(tts.filename.replace('.mp3','.wav'),format='wav')

p = pyaudio.PyAudio()
wf = wave.open(tts.filename.replace('.mp3','.wav'),'rb')
Format = p.get_format_from_width(wf.getsampwidth())
print('format:',Format)
Channels = wf.getnchannels()
print('channel:',Channels)
Rate = wf.getframerate()
print('rate:',Rate)
chunk = 1024
# 打开数据流
stream = p.open(format=Format,
                channels=Channels,
                rate=Rate,
                output=True)

# 读取数据
data = wf.readframes(chunk)

# 播放  
while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)

# 停止数据流
if tts.tempfile:
    os.remove(tts.filename)
stream.stop_stream()
stream.close()

# 关闭 PyAudio  
p.terminate()
wf.close()
os.remove(tts.filename.replace('.mp3','.wav'))
