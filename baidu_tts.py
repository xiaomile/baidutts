#author:X-mile
#Create at 2018-02-27
import requests
import pyaudio
import wave
from pydub import AudioSegment
import os

class baiduTTS(object):
    def __init__(self,lan='zh',pid=101,vol=9,ie='UTF-8',spd=5,text='您好，您还没有输入要转成语音的文本'):
        self.lan = lan
        self.pid = pid
        self.vol = vol
        self.ie = ie
        self.spd = spd
        self.text = text
        self.chuck_size = 1024
        #self.filename = ''
        #self.url = "http://tts.baidu.com/text2audio?lan="+self.lan+"&pid="+self.pid+"&vol="+self.vol+"&ie="+self.ie+"&text="+self.text
        #self.response=requests.get(self.url,stream=True)
        self.url = 'http://tts.baidu.com/text2audio'
        self.response = requests.post(self.url,data={
            'lan' : self.lan,
            'pid' : self.pid,
            'vol' : self.vol,
            'ie' : self.ie,
            'spd': self.spd,
            'text' : self.text
        },stream=True)
        self.stream = self.response.content
    def file_len(self):
        return len(self.response.content)

    def save_file(self,filename='baidutts.mp3'):
        self.filename = filename
        self.tempfile = False
        with open(filename,'wb') as file:
            for chunk in self.response.iter_content(self.chuck_size):
                if chunk:
                    file.write(chunk)

    def say(self,save_temp=False):
        self.save_file()
        #print('here')
        self.save_temp = save_temp
        song = AudioSegment.from_mp3(self.filename)
        song.export(self.filename.replace('.mp3','.wav'),format='wav')
        p = pyaudio.PyAudio()
        wf = wave.open(self.filename.replace('.mp3','.wav'),'rb')
        self.Format = p.get_format_from_width(wf.getsampwidth())
        #print('format:',Format)
        self.Channels = wf.getnchannels()
        #print('channel:',Channels)
        self.Rate = wf.getframerate()
        #print('rate:',Rate)
        self.chunk = 1024
        # 打开数据流
        stream = p.open(format=self.Format,
                channels=self.Channels,
                rate=self.Rate,
                output=True)

        # 读取数据
        data = wf.readframes(self.chunk)

        # 播放  
        while data != b'':
            stream.write(data)
            data = wf.readframes(self.chunk)

        # 停止数据流
        if not save_temp:
            os.remove(self.filename)
        stream.stop_stream()
        stream.close()

        # 关闭 PyAudio  
        p.terminate()
        wf.close()
        os.remove(self.filename.replace('.mp3','.wav'))

#baiduTTS(text='您好，你拨打的号码暂时无法接通，请稍后再拨').say()

                



