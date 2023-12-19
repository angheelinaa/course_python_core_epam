from contextlib import ContextDecorator
from datetime import datetime


class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a")
        self.start_exec = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_exec = datetime.now()
        self.file.write(f"Start: {self.start_exec} | "
                        f"Run: {self.end_exec - self.start_exec} |  "
                        f"An error occurred: {exc_val}\n")
        self.file.close()

        if exc_type is not None:
            raise exc_type(exc_val).with_traceback(exc_tb)
