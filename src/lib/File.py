import os
from src.constants.paths import PATH_PROGRAM

class File:
    @staticmethod
    def save (content, dest):
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