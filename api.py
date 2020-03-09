VERSION = "0.0.1-beta.1"
LANGUAGE = "python"
PROJECT = "babble"

API = {"babble.generate_phrase" : {"arguments" : ("length int", ),
                                   "keywords" : {"_list" : "list"},
                                   "returns" : "str",
                                   "exceptions" : ("ValueError", "IOError")},
       "babble.load_list" : {"keywords" : {"filename" : "str"},
                             "returns" : ("list", )}
       }
