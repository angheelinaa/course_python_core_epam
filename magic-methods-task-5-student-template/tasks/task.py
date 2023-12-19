import os
import shutil
import random
import string


class TempDir:
    def __init__(self):
        self.dir_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
        self.home_path = os.getcwd()

    def __enter__(self):
        os.mkdir(self.dir_name)
        self.new_path = os.path.abspath(self.dir_name)
        os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.home_path)
        shutil.rmtree(self.new_path)
