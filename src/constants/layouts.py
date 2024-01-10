import chalk, math, os
from src.constants.config import config
from src.constants.options import options
from src.utils.functions import loop
from src.utils.colors import blue, white, green, yellow

total_options = len(options) - 1

banner = f"""
{ green }
_  _ ____ _  _ ____   ____ ___ ___ ____ ____ _  _ 
|__| |___  \/  |__|   |__|  |   |  |__| |    |_/  
|  | |___ _/\_ |  |   |  |  |   |  |  | |___ | \_ 
{ white }

Author          : { blue } { config.author } { white }
Github          : { blue } github.com/{ config.author } { white }
Repository      : { blue } github.com/{ config.author }/{ config.name } { white }
Version         : { blue } { config.version } { white }
Total Menu      : { blue } { total_options } { white }
"""

column = 2
row = math.ceil(len(options) / column)

iteration = 0
padding = 0
menu = "\n";

lines = loop("|", row).split("|")

# define padding
for key in options:
    item = options[key]
    text = f"[{blue}{ str(key).zfill(len(str(total_options))) }{white}]. { item.upper() }"
    
    if padding < len(text):
        padding = len(text) + 1

# generate options list
for i in range(column):
    for j in range(row):
        try:
          item = options[iteration]
          text = f"[{blue}{ str(iteration).zfill(len(str(total_options))) }{white}]. { item.upper() }"
          gap = loop(" ", padding - len(text))
          lines[j] += f"{ text }{gap}"
        except Exception as err:
          continue
        iteration += 1
          

# generate menu
for line in lines:
    if line:
        menu += f"{ line }\n"

# define barrier
barrier = loop(f"{yellow}={white}", 50)

def changeBanner (menu = "-"):
    os.system("clear")
    banner = f"""{ green }
_  _ ____ _  _ ____   ____ ___ ___ ____ ____ _  _ 
|__| |___  \/  |__|   |__|  |   |  |__| |    |_/  
|  | |___ _/\_ |  |   |  |  |   |  |  | |___ | \_ 
{ white }

Author          : { blue } { config.author } { white }
Github          : { blue } github.com/{ config.author } { white }
Repository      : { blue } github.com/{ config.author }/{ config.name } { white }
Version         : { blue } { config.version } { white }
Menu            : { blue } { menu } { white }"""
    print (barrier)
    print (banner)
    print (barrier)