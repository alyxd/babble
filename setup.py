import os.path
from setuptools import setup

options = {"name" : "babble",
           "version" : "0.0.1",
           "description" : "Generates random phrases",
           "data_files" : [("./babble/", [os.path.join("babble", "wordlist.txt")])],
           "author" : "Ella Rose",
           "author_email" : "python_pride@protonmail.com",
           "packages" : ["babble"],
           "classifiers" : ["License :: OSI Approved :: MIT License"]
                            }

if __name__ == "__main__":
    setup(**options)
