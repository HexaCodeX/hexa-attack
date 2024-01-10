import os, time
from .Thread import Thread
from .Network import Network
from src.constants.layouts import barrier, banner, menu, changeBanner
from src.constants.options import options
from src.utils.io import question, confirm, log
from src.utils.functions import checkValidUrl

class Program:
    def __init__(self):
        pass
    
    @staticmethod
    def mainTask():
        os.system("clear")
        print (banner)
        print (barrier)
        print (menu)
        print (barrier)
        
        choice = int(question("please select a option"))
        
        if not options.get(choice):
            log("warning", "please select a option")
            time.sleep(1)
            Program.start()
        
        option = options[choice].replace(" ", "_").strip()
        
        time.sleep(2)
        if option in ["exit"]:
            Program.exit()
        if option in ["test_proxies"]:
            Network.test_proxies()
        if option in ["ip_reverse"]:
            Network.ip_reverse()
        if option in ["update_proxies"]:
            Network.update_proxies()
        if option in ["admin_finder"]:
            Network.admin_finder()
        if option in ["ddos_all_requests"]:
            Thread.all_requests()
        if option in ["ddos_basic"]:
            Thread.basic()
        if option in ["spam_post"]:
            Thread.spam_post()
        
        Program.start()
    @staticmethod
    def start():
        try:
            Program.mainTask()
        except Exception as err:
            log("error", str(err))
            time.sleep(0.5 * len(str(err)))
            Program.start()
    
    @staticmethod
    def exit():
        if confirm ("are you sure ?"):
            log("info", "sayonara")
            exit()
        else:
            Program.start()
    
    @staticmethod
    def soon():
        log("info", "comming soon ..")
        time.sleep(1)
        Program.start()