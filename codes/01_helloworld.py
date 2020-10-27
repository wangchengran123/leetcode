def main():
    sum = 0.0
    count = 0
    s = input("Enter number (Enter to quit):")
    while s != "":
        x = eval(s)
        sum = sum + 1
        count = count + 1
        s = input ("Enter a number")
    print("The average is", sum/count)
main()
