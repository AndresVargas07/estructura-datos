x=int (input ("Escribir un número"))
y=int (input ("Escribir un número"))

operacion=input("Escribir un signo para operar: ")
if operacion=="+":
  print(x+y)
elif operacion=="-":
  print(x-y)
elif operacion=="*":
  print(x*y)
elif operacion=="/":
  print(x/y)
else:
  print("Operación no válida")
