import speedtest
from hurry.filesize import size,verbose
import pymsgbox
import winsound
from threading import Thread


winsound.Beep(2050,450)
servers = []

s = speedtest.Speedtest()
s.get_servers()
s.get_best_server()

def down():
    s.download()

def upl():
    s.upload()

thread_down = Thread(target = down)
thread_upl = Thread(target = upl)
thread_down.start()
thread_upl.start()
thread_down.join()
thread_upl.join()
s.results.share()

results_dict = s.results.dict()


pymsgbox.alert('Download: ' + str(size(round(results_dict['download'],0),system=verbose)) + '\n' + 'Upload: ' + str(size(round(results_dict['upload'],0),system=verbose)) + '\n' + 'Ping: ' + str(round(results_dict['ping'],0)) + ' ms')
