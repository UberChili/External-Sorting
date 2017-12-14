def main():

    lin = []

    lin = [line.strip() for line in open("file.txt", "r")]

    for i in lin:
        print(i)

    print("hola")
    print(lin)
if __name__ == "__main__":
    main()
