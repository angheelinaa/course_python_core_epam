import os


class Cd:
    def __init__(self, dir_name):
        if not os.path.isdir(dir_name) or not os.path.exists(dir_name):
            raise ValueError
        self.dir_name = dir_name

    def __enter__(self):
        self.home_path = os.getcwd()
        os.chdir(self.dir_name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.home_path)
