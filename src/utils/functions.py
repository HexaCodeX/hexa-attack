import json, re, os, chalk, requests, random, string, socket, struct, time
from bs4 import BeautifulSoup
from requests import status_codes
from datetime import datetime
from urllib.parse import urlparse
from src.utils.io import log, question, confirm
from src.utils.colors import purple, white
from src.constants.config import dict_config
from src.constants.icons import icons
from src.constants.paths import PATH_PROGRAM

def random_ip () -> str:
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def random_date (start_date: str = "2000-01-01", end_date: str = datetime.now().date()) -> str:
    start_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    end_date = datetime.strptime(str(end_date), "%Y-%m-%d")
    
    date_range = end_date - start_date
    random_days = random.randint(0, date_range.days)
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")

def xhr (method: str, url: str, headers: dict = {}, data = None, proxies = None, params = None, json = None, files = None, timeout: int = 3, mode: str = "log"):
    func = getattr(requests, method)
    meta_URL = urlparse(url)
    response = None
    proxies = proxies if dict_config["useProxy"] else None
    headers = {
        **headers,
        "user-agent": random_user_agent(),
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "expires": "0",
    }
    try:
        response = func(url, headers=headers, data=data, params=params, proxies=proxies, json=json, files=files, timeout=timeout)
        http_proxy = proxies["http"] if proxies else "-"
        
        if mode == "log":
            return f"| { chalk.green(status_codes._codes[response.status_code][0]) } | [{ chalk.yellow(method.upper()) }] [{purple}{ response.status_code }{white}] | { chalk.cyan(meta_URL.hostname) } | { chalk.white(http_proxy) }"
        if mode == "return":
            return response
        
    except Exception as err:
        log("error", f"| { chalk.green('timeout') } | [{ chalk.yellow(method.upper()) }] | { chalk.cyan(meta_URL.hostname) } |")
        if mode == "return":
            return False

def json_decode(pathfile: str):
    result = None
    try:
        with open(pathfile, "r") as file:
            try:
                result = json.loads(file.read())
                file.close()
            except Exception:
                print("invalid json file")
                return
    except IOError:
        print(f"file at { pathfile } doesn't exist")
        return
    
    return result

def json_encode(data, indent: int = 0) -> str:
    try:
        return json.dumps(data, indent=indent)
    except Exception:
        raise "failed when convert to json"

def text_split(text: str) -> str:
    pattern = r"(\,|\|)"
    items = list( filter(lambda item: re.match(pattern, item) == None, list(map(lambda item: str(item).strip(), re.split(pattern, text)))) )
    return items

def get_class_attribute (C, method: str):
    name = C.__name__
    registry = { f"{name}": C }
    return getattr(registry[name], method)

def now () -> str:
    return datetime.now().strftime("%H:%M:%S")

def date () -> str:
    time = datetime.now()
    return f"{ time.day }-{ time.month }-{ time.year }"

def user_input (text: str, icon: str) -> str:
    return input(f"{ icons[icon] } { text } : ")

def env (key: str, alternative = None) -> str:
    file = dotenv.find_dotenv()
    dotenv.load_dotenv(file)
    item = os.environ.get(key) if not os.environ.get(key) == None else alternative
    if item == None:
        os.environ[key] = user_input(f"input variabel { key }", "input")
        dotenv.set_key(file, key, os.environ[key])
        return os.environ[key]
    else:
        return item

def write (text: str, icon: str) -> None:
    print (f"{ icons[icon] } { text }")

def typeof (_any_) -> str:
    return type(_any_).__name__

def dict_show (items: dict) -> None:
    for key in items:
        if key in items:
            if typeof(items[key]) != "dict":
                write(f"{key} : { chalk.cyan(items[key]) }", "info")
            else:
                dict_show(items[key])

def loop (char: str, each: int = 3) -> str:
    if each < 1:
        return ""
    result = str(char)
    for x in range (each):
        result += char
    return result

def checkValidUrl (url: str) -> bool:
    url_pattern = re.compile(
      r'^(https?://)?'  # Match http or https
      r'((\d{1,3}\.){3}\d{1,3}|'  # IP address or
      r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # domain
      r'(:\d{1,5})?'  # Optional port
      r'(/[^\s]*)?$'  # Optional path
    )
    
    if not re.match(url_pattern, url):
        log("warning", "please enter a valid url !")
        return False
    else:
        return True

def get_proxies (path: str) -> list:
    if os.path.exists(path):
        content = ""
        with open(path, "r") as file:
            content = file.read()
            file.close()
        return content.split("\n")
    else:
        raise Exception (f"path '{ path }' doesn't exists !")

def random_str (length: int = 8) -> str:
    characters = string.ascii_letters + string.digits  # You can customize this based on your requirements
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def random_id (length: int = 9) -> str:
    characters = string.digits  # You can customize this based on your requirements
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid

def random_user_agent () -> str:
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
    random_browser = random.choice(browsers)
    
    # Generate a random version number (you can adjust the range as needed)
    version_major = random.randint(1, 15)
    version_minor = random.randint(0, 99)
    browser_version = f'{version_major}.{version_minor}'

    user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {random_browser}/{browser_version} Safari/537.3'
    return user_agent

def get_admin_pathnames () -> list:
    path = f"{ PATH_PROGRAM }/src/includes/admin_pathnames.txt"
    if os.path.exists(path):
        content = ""
        with open(path, "r") as file:
            content = file.read()
            file.close()
        return content.split("\n")
    else:
        raise Exception (f"path '{ path }' doesn't exists !")

def url_port_join (url: str, port: int = 443) -> str:
    parsed = urlparse(url)
    
    return url.replace(f"{ parsed.scheme }://{ parsed.netloc }", f"{ parsed.scheme }://{ parsed.netloc }:{ port }")

def get_element_from_selector (html: str):
    selector = question ("form element selector")
    soup = BeautifulSoup(html, 'html.parser')
    
    element = soup.select_one(selector)
    
    if element:
        lines = element.prettify().split("\n")
        lineNumber = 1
        for line in lines:
            print(f"[{ lineNumber }]:{ line }")
            lineNumber += 1
        
        if not confirm ("continue to spam"):
            raise Exception("spamming cancelled by user")
    else:
        log("warning", f"element with selector '{ selector }' is not found !")
    return get_element_from_selector(html) if not element else element

def check_list_index (index: any, items: list) -> bool:
    try:
        items[index]
        return True
    except IndexError:
        return False

def test_ping (url: str) -> bool:
    try:
        requests.get(url)
        return True
    except:
        return False
