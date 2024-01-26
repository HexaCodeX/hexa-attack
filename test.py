from src.utils.functions import url_port_join
from src.constants.ports import ports

print (url_port_join("https://example.com/path/to/file.txt", 3306))
print (list(ports.values()))