import sys
print(sys.path)
from app import hello

def from_test():
    print("from main")

if __name__=="__main__":
    hello.main_thread()