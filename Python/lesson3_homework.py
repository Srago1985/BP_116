# chapter 1
nis = float(input("Enter amount in NIS→"))
rate_euro = float(input("Enter the exchange rate (NIS to euros)→"))
comission = float(input("Enter commission percentage (as a percentage)→")) / 100
euros_after_comission = nis / rate_euro * (1 - comission)
print(f"The amount in euros after commission is {euros_after_comission:.2f}")

# chapter 2

def f1():
    print("name", end=" ")
    
def f2():
    print("My", end=" ")
    
def f3():
    print("is", end=" ")

def f4():
    print("Mikhail")
    
f2()
f1()
f3()
f4()

# chapter 3

def f1():
    print("be", end="")

def f2():
    print("to", end=" ")
    
def f3():
    print("\n\tor", end=" ")

def f4():
    print("not", end="\n\t\t")

def f5():
    print("?")

f2()
f1()
f3()
f4()
f2()
f1()
f5()