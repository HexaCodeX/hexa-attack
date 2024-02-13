import os
from src.constants.paths import PATH_PROGRAM

class File:
    @staticmethod
    def read (pathfile: str, mode: str = "r") -> str:
        try:
            content = ""
            with open(pathfile, mode) as file:
                content = file.read()
                file.close()
            return content
        except Exception as err:
            raise (f"file at { pathfile } is doesn't exist !")
    
    @staticmethod
    def save (content: str, dest: str) -> None:
        dest = os.path.join(PATH_PROGRAM, dest)
        directory = os.path.dirname(dest)
        
        if os.path.exists(directory) is False:
            os.makedirs(directory)
        else:
            pass
        
        # save file
        if os.path.exists(dest) is False:
            with open (dest, "w") as file:
                file.write(content)
                file.close()
        else:
            raise Exception (f"file at '{ dest }' is doesn't exists !")