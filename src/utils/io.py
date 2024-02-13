import chalk
from src.constants.config import config
from src.constants.icons import icons
from src.utils.colors import gray, white, green, purple

def question (text: str, transform = str) -> str:
    _input_ = input(f"[{ green }?{ white }]: {text}: ")
    
    try:
        _input_ = transform(_input_)
    except Exception:
        log("error", f"input must reference with { type(transform) }")
        return question(text, transform=transform)
    
    if _input_ == "":
        return question(text)
        
    return _input_

def confirm (text: str) -> bool:
    # skip confirm on development
    if config.environment in ["local", "development"]:
        return True
    
    _input_ = input(f"[{ purple }?{ white }]: {text} [y/n]: ")
    if _input_ in ["y", "yes"]:
        return True
    elif _input_ in ["n", "no"]:
        return False
    else:
        return confirm(text)

def log (key: str, text: str) -> None:
    icon_keys = list(icons.keys())
    if not key in icon_keys:
        raise Exception("danger", f"icon with label '{key}' is doesn't exists !")
    
    icon = icons[key]
    print (f"{ icon }: { text }")