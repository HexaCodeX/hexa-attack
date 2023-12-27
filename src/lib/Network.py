import requests, random, chalk, os, asyncio, math, urllib, socket, time
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from src.utils.functions import xhr, checkValidUrl, get_proxies, random_str, random_id, random_ip, random_user_agent
from src.utils.io import log, question, confirm
from src.constants.paths import PATH_PROGRAM

class Network:
    @staticmethod
    def ip_reverse ():
        url = question ("input target url")
        if not checkValidUrl(url):
            Thread.basic()
        urlParsed = urllib.parse.urlparse.urlparse(url)
        hostname = urlParsed.hostname
        ipAddress = socket.gethostbyname(hostname)
        
        ipAddressUrl = parsed._replace(netloc=ipaddress).geturl()
        log("success", f"{ url } => { ipAddressUrl }")
        
        if confirm ("want try again ?"):
            Network.ip_reverse()
        else:
            return False
    
    @staticmethod
    def update_proxies ():
        url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        start = perf_counter()
        
        log("info", "getting proxies ...")
        content = requests.get(url).text
        
        with open(f"{ PATH_PROGRAM }/proxies.txt", "w") as file:
            file.write(content)
            file.close()
        
        stop = perf_counter()
        log("info", f"done in { math.floor(stop - start) }s")
        log("success", "proxies updated successfully !")
        time.sleep(2)
    
    @staticmethod
    def test_proxies ():
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        url = question ("test target url") #f"https://google.com/"
        
        log("info", f"total proxies ({ chalk.cyan(len(proxies)) })")
        time.sleep(1)
        
        def func (proxy):
            methods = ["head"]
            
            try:
                for method in methods:
                    response = xhr(method, url=url, proxies={
                      "http": f"http://{proxy}",
                    }, mode="return")
                    stop = perf_counter()
                    
                    if not response:
                       proxies.remove(proxy)
                       log("error", f"| death | [{ chalk.red('???') }] | { proxy }")
                    else:
                        if response.status_code in range(200, 499):
                            log("info", f"| alive | [{ chalk.green(response.status_code) }] | { proxy }")
                        else:
                            proxies.remove(proxy)
                            log("info", f"| death | [{ chalk.red(response.status_code) }] | { proxy }")
                    
            except Exception as err:
                log("error", str(err))
                
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(func, proxies)
        
        with open(f"{ PATH_PROGRAM }/proxies.txt", "w") as file:
            content = "\n".join(proxies)
            file.write(content)
            file.close()
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    