test = 0

def testing():
    test = 10

    def testing1():
        global test
        test = 20

    testing1()
    print(test)
    return test

test = testing()
print(test)