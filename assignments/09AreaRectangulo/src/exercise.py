def area (x,y):
    return x*y
def main():
    #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    a=float(input("Dame la altura: "))
    ar=area(b,a)
    print("El área del rectángulo es: "+str(ar))
    pass

if __name__=='__main__':
    main()
