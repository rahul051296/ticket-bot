import multiprocessing


def a(a):
    return "1"

def b():
    print("B")


if __name__ == "__main__":
    p = multiprocessing.Process(target=a, args=("1"))
    print(p.start())
    p.join()
