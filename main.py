from random import randint

def main():
    size = int(input("Size: "))

    generate_file(size)

def generate_file(size):

    fp = open("file.txt", "w")
    
    for line in range(size):
        fp.write(str(randint(0, 100)))
        fp.write("\n")

    fp.close()

if __name__ == "__main__":
    main()
