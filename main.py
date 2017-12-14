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
    nd = math.ceil(size/np)
    D = []

    fp = open("file.txt", "r")

    for i in range(np):
        nai = "file" + str(i + 1) + ".txt"
        outF = open(nai, "w")

        # Reads from file.txt and copies
        # lines into file#.txt
        for line in fp:
            outF.write(str(line))

        for line in fp:
            D.extend([line])

        for i in range(len(D)):
            print(D[i])

        outF.close()



    fp.close()

if __name__ == "__main__":
    main()
