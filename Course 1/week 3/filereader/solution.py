class FileReader:
    def __init__(self, path_name):
        self.path_name = path_name
    
    def read(self):
        try:
            f = open(self.path_name, 'r')
            return f.read()
        except FileNotFoundError:
            return ""