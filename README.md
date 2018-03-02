# baidutts
change text into mp3 file by sending requests to baidu_tts through python

example:

----------


from baidu_tts import baiduTTS

baiduTTS(text='the text you want to change to mp3 file').save_file('filename.mp3')

---------


By running the example code above in python , you can get the mp3 file which would speak 'the text you want to change to mp3 file' 
when playing

----------


from baidu_tts import baiduTTS

baiduTTS(text='the text you want to change to mp3 file').say()

-----------


By running the example code above in python , you can hear some words from the speaker in your computer 

more parameter could be found in source code
