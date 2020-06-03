from subprocess import Popen
import time

while True:
    urls = ['https://www.youtube.com/watch?v=bCgLa25fDHM&t=3s','https://www.youtube.com/watch?v=bCgLa25fDHM&t=3s']

    for url in urls:
        Popen(['start', 'chrome' , url], shell=True)

    #currently, the sleep timer is set at 10 seconds for proof of functionality, change this to 3000 to accurately play the duration of the video
    time.sleep(10)

    Popen('taskkill /F /IM chrome.exe', shell=True)

