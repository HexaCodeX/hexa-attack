import os
class File:
    @staticmethod
    def save (content, dest):
        directory = os.path.dirname(dest)
        if os.path.exists(directory) is False:
            os.makedirs(directory)
        else:
            pass
        
        # save file
        if os.path.exists(dest) is False:
            with open (dest, "x") as file:
                file.write(content)
                file.close()
        else:
            pass