from random import randint
import math

def main():
    size = int(input("Size: "))

    generate_file(size)
    chop_sort(size)

def generate_file(size):

    fp = open("file.txt", "w")
    
    for line in range(size):
        fp.write(str(randint(0, 100)))
        fp.write("\n")

    fp.close()

def chop_sort(size):
    np = math.ceil(size/10)
    print(np)

    fp = open("file.txt", "r")

    fp.close()

if __name__ == "__main__":
    main()
