def area (b,a):
    return b*a
def vol (rectangulo,pr):
    return ar*pr
def main():
    #escribe tu código abajo de esta línea
    base=float(input("Dame la base: "))
    altura=float(input("Dame la altura: "))
    profundidad=float(input("Dame la profundidad: "))
    ar=area(base,altura)
    volumen=vol(ar,profundidad)
    print("El volumen del prisma es: "+str(volumen)
  
if __name__=='__main__':
    main()
