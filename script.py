from subprocess import Popen
import time

while True:
    urls = ['https://www.youtube.com/watch?v=bCgLa25fDHM&t=3s','https://www.youtube.com/watch?v=bCgLa25fDHM&t=3s']

    for url in urls:
        Popen(['start', 'chrome' , url], shell=True)

    time.sleep(10)

    Popen('taskkill /F /IM chrome.exe', shell=True)

