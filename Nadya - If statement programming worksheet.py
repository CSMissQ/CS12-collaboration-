def main():
    task=int(input("Enter the task number: "))
    if task==1:
        task1()
    elif task==2:
        task2()
    elif task==3:
        task3()

def task1():
    number=int(input("Enter a whole number: "))
    if number%2==1:
        print("Number is odd.")
    else:
        lol=number%2
        print(lol)
        print("Number is even.")
    main()

def task2():
    age=int(input("Enter your age: "))
    test=input("Have you passed your driving test? (Y/N)")
    if age<21 or test.lower()!="y":
        print("You are not allowed to drive the minibus.")
    else:
        print("You are allowed to drive the minibus.")
    main()

def task3():
    names=input("Enter the 3 names, separated by spaces.")
    ordered=sorted(names.split())
    print((" ".join(ordered)+"\nSorted!"))
    main()

main()