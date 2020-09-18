VERSION = "0.0.1-beta.2"
LANGUAGE = "python"
PROJECT = "babble"

API = {"babble.generate_phrase" : {"arguments" : ("length int", ),
                                   "keywords" : {"_list" : "list"},
                                   "returns" : "str",
                                   "exceptions" : ("ValueError", "IOError")}       
       }
