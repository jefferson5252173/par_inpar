#programa para verificar si un numero es par o inpar

print("----------------------")
print("-----par o impar------")
print("----------------------")

#input
x = int(input("digite un numero: "))

#prosessing
r=x%2
if x==0:
    msj="par"
else:
    msj="impar"

print(" el numero " + str(r) + "es" + msj)    

