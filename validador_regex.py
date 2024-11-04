# Validador usando regex para (Email, Rut)
import re

# ----------------------------------------------------- Email
def verifyEmail(op):
    value=""
    e = re.match(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+', op)
    try:
        if e != None:
            value=e.group()
        else:
            value="Formato no-valido!."
    except Exception as ex:
        value="Error Email", ex

    return value

# ----------------------------------------------------- Rut
def getRut(dni):
    data=""
    r = re.match(r'\d{2}\.\d{3}\.\d{3}-[a-zA-Z0-9]', dni)
    try:
        if r != None:
            data=r.group()
        else:
            data="Formato no-valido!."
    except Exception as ex:
        data="Error Email", ex
    
    return data

def formRut(dni, n):
    cadena=""
    sub1 = dni[0:2]+"."+dni[2:5]+"."
    if n == 1:
        sub2 = dni[5:10]
        cadena = sub1+sub2
    if n == 2:
        sub2 = dni[5:8]+"-"+dni[8:9]
        cadena = sub1+sub2
        
    return getRut(cadena)
#----
def verifyRut(op):
    value=""
    if len(op) == 12:
        value = getRut(op)
    elif len(op) == 10:
        value = formRut(op, 1)
    elif len(op) == 9:
        value = formRut(op, 2)
    else:
        value = "Formato no-valido!."
    return value


# -------------- usando validadores
#print(verifyRut("11.111.111-k"))
#print(verifyEmail("ejemplo@gmail.com"))