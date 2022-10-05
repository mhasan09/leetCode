class First(object):
    def __init__(self):
        print("first prologue")
        super(First, self).__init__()
        print("first epilogue")


class Second(First):
    def __init__(self):
        print("second prologue")
        super(Second, self).__init__()
        print("second epilogue")


class Third(First):
    def __init__(self):
        print("third prologue")
        super(Third, self).__init__()
        print("third epilogue")


class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print("that's it")


Fourth()
