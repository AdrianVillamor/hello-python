def sayhello (name,school = "ADNU"):
    print("Hello, {} from {}.".format(name,school))

sayhello("Adrian")
sayhello("Adrian Villamor", "ADNU")
sayhello(name = "Adrian Villamor",  school = "CSNHS")
sayhello(school = "MSN", name = "Adrian Villamor")
