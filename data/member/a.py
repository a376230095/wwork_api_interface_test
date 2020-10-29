import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if __name__=="__main__":
    print(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    print(BASE_PATH)