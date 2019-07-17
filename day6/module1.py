def foo():
    print("hello world in module1")


def main():
    print(__name__, "this is module1.py")
    # add your test code here
    # and it will not work with from in other py files


if __name__ == '__main__':
    main()
