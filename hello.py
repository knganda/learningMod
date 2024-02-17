def main():
    number = get_num()
    meow(number)


def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
    
def meow(n):
    print("meow\n" * n, end="")
     
if __name__ == "__main__":
    main()