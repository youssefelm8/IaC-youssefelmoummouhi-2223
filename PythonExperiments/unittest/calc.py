def add(n1,n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
     return n1*n2  

def divide(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return ("Error: Division by Zero")

def main():
    print (add(1000,10))
    print (subtract(1000,10))
    print (multiply(1000,10))
    print (divide(1000,10))

if __name__ == "__main__":
    main()