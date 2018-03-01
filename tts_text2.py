#author:X-mile
from baidu_tts import baiduTTS
import win32com.client
tts = win32com.client.Dispatch('SAPI.SPVoice')
tts.SpeakStream(baiduTTS().stream)
