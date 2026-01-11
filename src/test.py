import sys
print(sys.path)
from anotherPackage import something
from app import hello
import another.test2

if __name__=="__main__":
    something.module_test()
    hello.greetings("from app/hello.py")
