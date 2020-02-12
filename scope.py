a = 5  # global variable, could be read anywhere, but not write everywhere


def function_one():
    global a  # claim no local variable named "a"
    print("In funciton_one, a starts {}".format(a))
    a = 13
    print("In funciton_one, a is {}".format(a))
    
    return a


def funciton_two():
    print("In funciton_two, a is {}".format(a))


def main():
    function_one()
    funciton_two()
    print("In main function, a is {}".format(a))


if __name__ == "__main__":
    main()