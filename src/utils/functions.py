import json, re, os, chalk, requests, random, string, socket, struct
from requests import status_codes
from datetime import datetime
from urllib.parse import urlparse
from src.utils.io import log
from src.utils.colors import purple, white
from src.constants.icons import icons

def random_ip ():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def xhr (method, url, headers = None, data = None, proxies=None, json=None, files=None, timeout=3, mode="log"):
    func = getattr(requests, method)
    meta_URL = urlparse(url)
    response = None
    
    try:
        response = func(url, headers=headers, data=data, proxies=proxies, json=json, files=files, timeout=timeout)
        http_proxy = proxies["http"] if proxies else "-"
        
        if mode == "log":
            return f"| { chalk.green(status_codes._codes[response.status_code][0]) } | [{ chalk.yellow(method.upper()) }] [{purple}{ response.status_code }{white}] | { chalk.cyan(meta_URL.hostname) } | { chalk.white(http_proxy) }"
        if mode == "return":
            return response
        
    except Exception as err:
        if mode == "return":
            return False
        log("error", f"| { chalk.green(str(err)) } | [{ chalk.yellow(method.upper()) }] | { meta_URL.hostname } |")

def json_decode(pathfile):
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

def json_encode(data):
    try:
        return json.dumps(data)
    except Exception:
        raise "failed when convert to json"

def text_split(text):
    pattern = r"(\,|\|)"
    items = list( filter(lambda item: re.match(pattern, item) == None, list(map(lambda item: str(item).strip(), re.split(pattern, text)))) )
    return items

def url_join (domain, username):
    return f"https://{ domain }/{ username }"

def get_class_attribute (C, method):
    name = C.__name__
    registry = { f"{name}": C }
    return getattr(registry[name], method)

def now ():
    return datetime.now().strftime("%H:%M:%S")

def date ():
    time = datetime.now()
    return f"{ time.day }-{ time.month }-{ time.year }"

def user_input (text, icon):
    return input(f"{ icons[icon] } { text } : ")

def env (key, alternative = None):
    file = dotenv.find_dotenv()
    dotenv.load_dotenv(file)
    item = os.environ.get(key) if not os.environ.get(key) == None else alternative
    if item == None:
        os.environ[key] = user_input(f"input variabel { key }", "input")
        dotenv.set_key(file, key, os.environ[key])
        return os.environ[key]
    else:
        return item

def write (text, icon):
    print (f"{ icons[icon] } { text }")

def typeof (_any_):
    return type(_any_).__name__

def dict_show (items):
    for key in items:
        if key in items:
            if typeof(items[key]) != "dict":
                write(f"{key} : { chalk.cyan(items[key]) }", "info")
            else:
                dict_show(items[key])

def loop (char, each):
    if each < 1:
        return ""
    result = str(char)
    for x in range (each):
        result += char
    return result

def checkValidUrl (url):
    exp = r"^https?://[^\s\/$.?#].[^\s]*$"
    if not re.match(exp, url):
        log("warning", "please enter a valid url !")
        return False
    else:
        return True

def get_proxies (path):
    if os.path.exists(path):
        content = ""
        with open(path, "r") as file:
            content = file.read()
            file.close()
        return content.split("\n")
    else:
        raise Exception (f"path '{ path }' doesn't exists !")

def random_str (length = 8):
    characters = string.ascii_letters + string.digits  # You can customize this based on your requirements
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def random_id (length = 9):
    characters = string.digits  # You can customize this based on your requirements
    uid = ''.join(random.choice(characters) for _ in range(length))
    return uid

def random_user_agent ():
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
    random_browser = random.choice(browsers)
    
    # Generate a random version number (you can adjust the range as needed)
    version_major = random.randint(1, 15)
    version_minor = random.randint(0, 99)
    browser_version = f'{version_major}.{version_minor}'

    user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {random_browser}/{browser_version} Safari/537.3'
    return user_agent
