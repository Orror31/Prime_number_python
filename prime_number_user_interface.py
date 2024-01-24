#user interface and menu face
primes=[]
choice=""
while choice!="F":
    print("_"*40)
    print("-"*10, "Prime Numbers","-"*10)
    print("_"*40)
    print("\n")
    print("OPTIONS")
    print("A: Add new prime number")
    print("B: Deleate the prime number")
    print("C: Edit the prime number")
    print("D: Shaw all the primes number")
    print("E: define prime numbers smallest to larger")
    print("F: Exit the program")
    choice=input("Write your choice ->")

    if choice=="A":
        print("-"*8, "Adding new primes number","-"*8)
        print("_"*30)
        new=input("Enter new prime number : ")
        primes.append(new)

    if choice=="B":
        stop=len(primes)
        print("-"*40)
        print("No  |","Prime Number |","Index number |")
        print("-"*40)
        for i in range(stop):
            print(i+1,primes[i],"\t"*2,i)

    if choice=="C":
        stop=len(primes)
        print("-"*40)
        print("No |", "Prime Number |", "Index number |")
        print("-"*40)
        for i in range(stop):
            print(i+1 ," |",primes[i], "\t"*2, "|",i)
        print("-"*10, "Prime Number Edit", "-"*10)
        i=int(input("Enter index number of prime number"))
        primes[i]=input("Enter prime number: ")
        print("Your prime number has been successfully edited!")

    if choice=="D":
        stop=len(primes)
        print("-"*40)
        print("These are the list of prime numbers")
        print("-"*40)
        print("No |", "Prime Number |", "Index number |")
        print("-"*40)
        for i in range(stop):
            print(i+1," |",primes[i], "\t"*2, "|",i)

    if choice=="E":
        primes.sort()
        stop=len(primes)
        print("-"*40)
        print("All prime numbers list")
        print("-"*40)
        print("No |", "Prime Number |","Index number |")
        for i in range(stop):
            print(i+1," |",primes[i], "\t"*2, "|",i)
        print("-"*40)
