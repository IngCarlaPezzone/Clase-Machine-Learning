def f(x):
    return 2*x

def calculaEdad(cumple):
    """
    Esta funcion calcula la edad de una persona
    Argumentos 
        cumple , Puede ser un str (dd-mm-aaaa)
                 o un un objeto datatime
    Retorma 
        entero int con la edad
    """
    from datetime import date
    if isinstance(cumple, str):
        
        dia = cumple[:2]
        mes = cumple[3:5]
        año = cumple[6:]
        
        cumple = date( int(año), int(mes), int(dia))
    hoy  = date.today()
    edad = hoy.year - cumple.year - ( (hoy.month, hoy.day) < (cumple.month, cumple.day))
    return edad