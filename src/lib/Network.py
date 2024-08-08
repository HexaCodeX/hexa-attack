import requests, random, chalk, math, urllib, socket, time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from src.utils.functions import loop, xhr, checkValidUrl, get_proxies, get_admin_pathnames, random_str, random_id, random_ip, random_user_agent, get_element_from_selector, check_list_index, test_ping
from src.utils.io import log, question, confirm
from src.constants.paths import PATH_PROGRAM
from src.constants.config import config

class Network:
    @staticmethod
    def ip_reverse () -> None:
        url = question ("input target url")
        if not checkValidUrl(url):
            Network.ip_reverse()
        
        urlParsed = urllib.parse.urlparse(url)
        hostname = urlParsed.hostname
        ipAddress = socket.gethostbyname(hostname)
        
        ipAddressUrl = urlParsed._replace(netloc=ipAddress).geturl()
        log("success", f"{ chalk.yellow(url) } => { chalk.cyan(ipAddressUrl) }")
        
        if confirm ("want try again ?"):
            Network.ip_reverse()
        else:
            return False
    
    @staticmethod
    def update_proxies () -> None:
        providers = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
            "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
            "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt"
        ]

        start = perf_counter()
        
        log("info", "getting proxies ...")
        content = ""

        def runner (provider):
            try:
                log("info", f"fetching { provider } ...")
                content = requests.get(provider).text
                with open(f"{ PATH_PROGRAM }/proxies.txt", "a") as file:
                    file.write(content)
                    file.close()
            except:
                log("error", f"provider { provider } is can't be reached!")
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(runner, providers)
        
        stop = perf_counter()
        log("info", f"done in { math.floor(stop - start) }s")
        log("success", "proxies updated successfully !")
        time.sleep(2)
    
    @staticmethod
    def test_proxies () -> None:
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        url = question ("test target url") #f"https://google.com/"
        
        if not checkValidUrl(url):
            Network.test_proxies()
        
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
                
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, proxies)
        
        with open(f"{ PATH_PROGRAM }/proxies.txt", "w") as file:
            content = "\n".join(proxies)
            file.write(content)
            file.close()
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def admin_finder () -> None:
        start = perf_counter()
        proxies = get_proxies(f"{ PATH_PROGRAM }/proxies.txt")
        target = question ("target url")
        pathnames = get_admin_pathnames()
        
        if not checkValidUrl(target):
            Network.admin_finder()
        
        def func (pathname):
            methods = ["get"]
            
            try:
                proxy = {
                  "http": random.choice(proxies)
                }
                url = urljoin(target, pathname)
                for method in methods:
                    response = xhr(method, url, proxies=proxy, mode="return")
                    
                    if not response:
                       log("error", f"| failed | [{ chalk.red('???') }] | { pathname }")
                    else:
                        if response.status_code in range(200, 499):
                            log("info", f"| found | [{ chalk.green(response.status_code) }] | { pathname }")
                        else:
                            log("info", f"| failed | [{ chalk.red(response.status_code) }] | { pathname }")
                            
            except Exception as err:
                log("error", str(err))
        
        with ThreadPoolExecutor(max_workers=config.workers) as executor:
            executor.map(func, pathnames)
        
        with open(f"{ PATH_PROGRAM }/proxies.txt", "w") as file:
            content = "\n".join(proxies)
            file.write(content)
            file.close()
            
        stop = perf_counter()
        log("info", f"time taken { stop - start }")
    
    @staticmethod
    def port_scanner () -> None:
        url = question("target host")
        if not checkValidUrl(url):
            Network.port_scanner()
        
        start_port = question("start port", transform=int)
        end_port = question("end port", transform=int)
        
        try:
            def scan_port (port):
                urlParsed = urllib.parse.urlparse(url)
                hostname = urlParsed.hostname
                ipAddressUrl = socket.gethostbyname(hostname)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                conn = sock.connect_ex(( ipAddressUrl, port ))
                try:
                    service_name = socket.getservbyport(port)
                    
                    log("info", f"{ service_name } | { port } | { 'open' if not conn else 'closed' }")
                except Exception:
                    pass
                    # log("error", f"error while connecting to port { port }")  
            
            with ThreadPoolExecutor(max_workers=config.workers) as executor:
                executor.map(scan_port, range(start_port, end_port + 1))
            
            if confirm ("want try again ?"):
                Network.port_scanner()
            else:
                return False
        except Exception as err:
            log("error", str(err))

    @staticmethod
    def who_is () -> None:
        domain = question("input target domain")
        isUseSSL = confirm("use SSL (https)")
        targetUrl = f"http{ 's' if isUseSSL else '' }://{ domain }"
        whoIsUrl = f"https://who.is/whois/{ domain }"
        
        if test_ping (targetUrl) and checkValidUrl(targetUrl):
            html = xhr("get", whoIsUrl, mode="return").text
            element = BeautifulSoup(html, "html.parser")
            
            domainStatus = element.find(id="siteStatusStatus").get_text() 
            queryResponseHeaders = element.find_all(class_="queryResponseHeader")
            queryResponseBodies = element.find_all(class_="queryResponseBodyRow")
            
            data = {}
            i = 0
            
            for responseBody in queryResponseBodies:
                if not check_list_index(i, queryResponseBodies):
                    continue
                
                key = responseBody.find(class_="queryResponseBodyKey").get_text() if responseBody.find(class_="queryResponseBodyKey") else responseBody.find_parent(class_="row").find_previous(class_="row").get_text()
                values = responseBody.find_all(class_="queryResponseBodyValue")
                
                if len(values) > 1:
                    data[key] = []
                    
                    for value in values:
                        data[key].append(value.get_text())
                else:
                    data[key] = values[0].get_text()
                i += 1
            output = ""
            
            for key in data:
                item = data[key]
                
                output += key
                
                if type(item) == list:
                    for x in item:
                        output += x + "\n"
                else:
                    output += item
            output = "\n".join(map(lambda line: f"[{ chalk.blue('@') }]: { line }", output.split("\n")))
            print (output)
        else:
            Network.who_is()
    
