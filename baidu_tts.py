#author:X-mile
#Create at 2018-02-27
import requests
class baiduTTS(object):
    def __init__(self,lan='zh',pid=101,vol=9,ie='UTF-8',text='您好，您还未输入要转成语音的文本'):
        self.lan = lan
        self.pid = pid
        self.vol = vol
        self.ie = ie
        self.text = text
        self.chuck_size = 1024
        #self.url = "http://tts.baidu.com/text2audio?lan="+self.lan+"&pid="+self.pid+"&vol="+self.vol+"&ie="+self.ie+"&text="+self.text
        #self.response=requests.get(self.url,stream=True)
        self.url = 'http://tts.baidu.com/text2audio'
        self.response = requests.post(self.url,data={
            'lan' : self.lan,
            'pid' : self.pid,
            'vol' : self.vol,
            'ie' : self.ie,
            'text' : self.text
        },stream=True)
        self.stream = self.response.content
    def file_len(self):
        return len(self.response.content)

    def save_file(self,filename='baidutts.wav'):
        with open(filename,'wb') as file:
            for chunk in self.response.iter_content(self.chuck_size):
                if chunk:
                    file.write(chunk)

                



