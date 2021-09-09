def cartas(pli,plu):
    x=pli*12
    y=plu*35
    if x<y:
       return x
    elif y<x:
        return y
def main():
    #escribe tu código abajo de esta línea
    papel=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    tarjetas=cartas(papel,plumones)
    print("El número máximo de tarjetas que se pueden hacer es: "+str(tarjetas))

    pass

if __name__=='__main__':
    main()
