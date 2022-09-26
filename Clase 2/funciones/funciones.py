def suma(result, *args):
    for valor in  args:
        result= result + valor
    return result

def resta(result, *args):
    for valor in  args:
        result= result - valor
    return result

def multi(result, *args):
    for valor in  args:
        result= result * valor
    return result

def div(result, *args):
    for valor in  args:
        result= result / valor
    return result

def div_esac(result, *args):
    for valor in  args:
        result= result // valor
    return result

def sumatoria(num1,num2):
    dif = abs(num1 - num2)
    if dif%2==0:
        suma = (dif//2) * ((num1 + num2 )) + (num1 + num2)/2
    else:
        suma = ((dif//2) +1) * (num1 + num2 )
    return int(suma)

def multiplo(multiplo,numero):
    if multiplo % numero == 0:
        return True
    return False

def menu_multiplo():
    try:
        a=int(input("ingrese un numero :"))
        b=int(input("es multiplo de :"))
    except ValueError:
        menu_multiplo()
    if multiplo(a,b):
        print(a,"SI es multiplo de ",b)
    else:
        print(a," NO es multiplo de ",b)

_FACTORIALES={0:1,1:1}
def fac(n):
    if n in _FACTORIALES:
        return _FACTORIALES[n]
    elif n>0:
        nv=n*fac(n-1)
        _FACTORIALES[n]=nv
        return nv
    elif n<0:
        nv=n*fac(n+1)
        _FACTORIALES[n]=nv
        return nv

def raiz(n):
    x = n / 2
    while True:
        if x * x == n:
            return x
        else:
            y = x
            x = ( x + ( n / x )) / 2
        if y == x:
            break 
    return x

def primo(n):
    if n < 0:
        return False
    elif n == 1 or n == 2:
        return True
    elif n > 2:
        x = (n ** 0.5 ) + 2
        x=int(x)
        for i in range(2,x):
            if n % i == 0:
                return False
            else:
                return True

def genprimo(num1,num2):
    primos=[]
    for i in range (num1,num2+1):
        if primo(i)==True:
            #print(x,"es primo y se tardo")
            primos.append(i)
    return primos

def descomponer(n):
    primos=[]
    for i in range(2 , n + 1):
        while n % i == 0:
            primos.append(i)
            n=n/i
    return primos
# genera lista de numeros divisores

def divisores(n):
    div=[]
    for i in range(1 , n + 1):
        if n % i == 0:
            div.append(i)
    return div

def mcd(n1,n2):
    """algoritmo de euclides 
    si a > b > 0   a = b * q + r  ==>> mcd(a.b)=mcd(b,r)"""
    if n1>n2:
        pass
    else:
        aux = n2
        n2 , n1 = n1 , aux
    while n1 % n2 !=0:
        n1 ,n2  = n2 , n1 % n2
    return n2


def maxi(lista):
    a=None
    for i in range(len(lista)):
        if a is None:
            a = lista[i]
        elif lista[i] > a:
            a = lista[i]
    return a

def mini(lista):
    a=None
    for i in range(len(lista)):
        if a is None:
            a = lista[i]
        elif lista[i] < a:
            a=lista[i]
    return a

def prom(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum/len(lista)

def ordenlist_3(list0,list1,list2):
    """Ordena tres listas paralelas  segun el ordenamiento de la primera por orden numerico"
    """
    for k in range(len(list0)-1):
        for x in range(len(list0)-1):
            if list0[x] > list0[x+1]:
                list0[x], list0[x+1] = list0[x+1] ,list0[x]  
                list1[x], list1[x+1] = list1[x+1] ,list1[x]
                list2[x], list2[x+1] = list2[x+1] ,list2[x]                                   
    return list0 , list1 , list2
    #print(list0);print(list1);print(list2)
                
def orden_alf(list):
    """Ordena la lista alfabeticamente hasta la 3 letra"""
    for k in range(len(list)-1): 
        for x in range(len(list)-1): 
            if list[x][0]>=list[x+1][0]: 
                if list[x][1]>=list[x+1][1]:
                    if list[x][2]>= list[x+1][2]:
                        aux=list[x] 
                        list[x]=list[x+1] 
                        list[x+1]=aux
                        #print(x,k)
    return list

def tabla(list):
    """imprime una Matriz  donde le primer lista es el nombre de cada columna y las demas listas son las filas
    y calcula el ancho maximo de cada palabra para el ancho de la columna"""
    ancho = []
    for i in range(len(list[0])):
        ancho.append(0)
        for j in range(len(list)):
            ancho[i] = max(ancho[i],len(list[j][i]))
    for j in range(len(list)):
        fila = '|'
        for i in range(len(list[0])):
            fs = "{:" + str(ancho[i]) + "}"
            fila += fs.format(list[j][i]) + '|'
        print(fila)
        if j == 0:
            print((sum(ancho)+1+len(list[0]))*"-")
    print((sum(ancho)+1+len(list[0]))*"-")

def indice(list,valor):
    if valor.isnumeric() == True:
        valor = int(valor)
        ind = valor -1
        return ind

    if valor in list:
        ind = list.index(valor)
        return ind

    else:
        print("su opcion no es valida")

def convertemp(c,f,k,op):
    if op == 1:
        return (c * 1.8) + 32
    elif op == 2:
        return c + 273.15
    elif op == 3:
        return (f - 32) / 1.8
    elif op == 4:
        return ((f - 32) / 1.8) + 273.15
    elif op == 5:
        return k - 273.15
    elif op == 6:
        return (k-273.15)*1.8 + 32
    else:
        print("opcion incorrecta")
        return None

def menu_temp():
    print("convierta de ºC a ºF o ºK ")
    print("1) de ºC a ºF" )
    print("2) de ºC a ºK" )
    print("3) de ºF a ºC" )
    print("4) de ºF a ºK" )
    print("5) de ºK a ºC" )
    print("6) de ºK a ºF" )
    op=input("-->")
    if op == "1":
        try:
            c=float(input("Ingrese los grados a convertir :"))
            print(c,"ºC son ",convertemp(c,0,0,1),"ºF")
        except ValueError:
            menu_temp()
    elif op == "2":
        try:
            c=float(input("Ingrese los grados a convertir :"))
            print(c,"ºC son ",convertemp(c,0,0,2),"ºK")
        except ValueError:
            menu_temp()
    elif op == "3":
        try:
            f=float(input("Ingrese los grados a convertir :"))
            print(f,"ºF son ",convertemp(0,f,0,3),"ºC")
        except ValueError:
            menu_temp()
    elif op == "4":
        try:
            f=float(input("Ingrese los grados a convertir :"))
            print(f,"ºF son ",convertemp(0,f,0,4),"ºK")
        except ValueError:
            menu_temp()
    elif op == "5":
        try:
            k=float(input("Ingrese los grados a convertir :"))
            print(k,"ºK son ",convertemp(0,0,k,5),"ºC")
        except ValueError:
            menu_temp()
    elif op == "6":
        try:
            k=float(input("Ingrese los grados a convertir :"))
            print(k,"ºK son ",convertemp(0,0,k,6),"ºF")
        except ValueError:
            menu_temp()
    else:
        menu_temp()

def indexall(sub,st):
    "retorna una tupla con los indices de comienzo de una subcadena en un strig o lista o tupla"
    tu = []
    if type(st) == str:
        for i in range(len(st)):
            try:
                ind = (st.index(sub,i,-1))
                if ind not in tu: tu.append(ind)
            except ValueError:
                continue
        if tu == []: return None
        return tuple(tu)
    if type(st) == list or type(st) == tuple:
        for i in range(len(st)):
            if st[i] == sub and i not in tu: tu.append(i)
        if tu == []: return None
        return tuple(tu)

if __name__ == "__main__":
    li=[1000,56,-7,15.7]
    print(li)
    print(" el maximo de li es :",maxi(li))
    print(" el minimo de li es :",mini(li))
    print(" el promedio de li es :",prom(li))

    #list1 =["a","b","c","d"]
    letras=["xyx","abc","aab","xyy","abb","xyz"]
    print(letras)
    print(orden_alf(letras))

    a=[1,2,3,4,5,6]
    a=tuple(a)
    b=(6,7,8,"hola")
    print("aca empieza")
    resultado = suma(a,b)
    print(resultado)

    print(suma("hola"," chau"))

    resultado = resta(100,50,25)

    print(resultado)

    resultado = multi(100,3)

    print(resultado)

    resultado = div(100,3)

    print(resultado)

    resultado = div_esac(100,3)

    print(resultado)
    
    print([10,5,9,4],["a","b","c","d"],[1,2,3,4],sep="\n")
    l1,l2,l3 = ordenlist_3([10,5,9,4],["a","b","c","d"],[1,2,3,4])
    
    print(l1)
    print(l2)
    print(l3)