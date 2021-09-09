def es_bisiesto (x):
    if (x%4)==0 and (x%100)!=0:
        return True
    else:
        return False
def main():
    #escribe tu código abajo de esta línea
    year=int(input())
    bis=es_bisiesto(year)
    print(str(bis))
    pass

if __name__=='__main__':
    main()
