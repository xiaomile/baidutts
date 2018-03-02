#author:X-mile
from baidu_tts import baiduTTS
import os
tts = baiduTTS()
tts.save_file()
os.system(tts.filename)

