#TALLER 2 - EJERCICIOS DE ALGORITMIA ESTRUCTURA CONDICIONAL


                        #1. Leer dos (2) números y los imprima en forma ascendente.


# print("ingrese dos numeros para ordenar de forma ascendente")
# num1 = input("ingrese el primer numero ")
# num2 = input("ingrese el segundo numero ")
# if  type(num1) and type(num2) == 'int':

#     if num1 > num2:
#         print(num2)
#         print (num1)
#     elif num2 > num1:
#         print(num1)
#         print(num2)
#     elif num1 == num2:
#         print("los numeros son iguales")

# else:
#     print("ingreso un dato invalido, por favor ingresa solamente numeros")



                        # 2. (Sentencia match) Diseñar un algoritmo que lea por teclado un número
                        # comprendido entre 1 y 10. Se desea visualizarsi el número es par o impar. En primer
                        # lugar, se deberá
                        # detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
                        # si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”;si es 2, 4, 6, 8, 10, escribir
                        # un mensaje de “par”.




# usernum=input("ingrese un numero comprendido del 1 al 10 para verificar si es par o impar")


# rest2 = usernum % 10

# if rest2 = 0:

                        # 3. (Sentencia match) Diseñar un algoritmo que lea un número entero entre 1 y 10, y
                        # nos muestre por pantalla el número ingresado en letra (1 = uno). Si el número leído
                        # no está comprendido entre 1 y 10 mostrar un mensaje de error  



                        # 4. Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta
                        # lo siguiente:
                        # • toda llamada que dure tres minutos o menos tiene un coste de 200 pesos.
                        # • cada minuto adicional a partir de los tres primeros es un paso de contador y
                        # cuesta 100 pesos
# print("vamos a calcular el valor de su llamada. ")
# print("recuerde que los segundos, pasado el minuto anterior, cuenta como un minuto. ")
# min=input("ingrese el numero de minutos que consumio en su llamada. ")
# a=200
# b=100
# if  type(min)  == 'int':
#     if min <= 3:
#         print("su llamada tiene un costo de: ", a)
#     else:
#         min >3
#         rest=a+((min - 3)*b) 
#         print("su llamada tiene un costo de: ", rest)
# else:
#     print("ingreso un dato invalido, por favor ingrese el tiempo que duro la llamada en minutos completos")


                        # 5. En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros
                        # y Y conejos blancos. Hacer un algoritmo que:
                        # • Imprima la cantidad de conejos vendida
                        # • Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de
                        # los conejos negros, imprima el monto total de la venta.
                        # • Imprima el color de los conejos que se vendieron más.


# print("vamos a calcular el total de ventas que tuviste.")
# conejosT=input("ingrese el numero de conejos que tienes en la granja. ")
# conejosB=input("ingrese el numero de conejos blancos que vendiste en la granja ")
# conejosN=input("ingrese el numero de conejos negros que vendiste en la granja ")
# conejosT=int(conejosT)
# conejosTotal=int(conejosB)+int(conejosN)
# if conejosT >= conejosTotal:
#     PconejosB =input("ingrese el valor de los conejos blancos ")
#     PconejosN =input("ingrese el valor de los conejos Negros ")
#     VconejosB = int(conejosB) * int(PconejosB)
#     VconejosN = int(conejosN) * int(PconejosN)
#     Vtotal = VconejosB+VconejosN
#     print("El numero de conejos que vendiste en total es: ", conejosTotal)
#     print("El monto total de conejos blancos en precio es: ",VconejosB)
#     print("El monto total de conejos negros en precio es: ",VconejosN)
#     print("El monto total de la venta es: ", Vtotal)
#     if conejosB>conejosN:
#         print("El numero de conejos que mas vendiste fueron los conejos blancos")
#     elif conejosB<conejosN:
#         print("El numero de conejos que mas vendiste fueron los conejos negros")
#     else:
#         print("El numero de conejos vendidos blancos y negros es igual.")
# else:
#     print("El numero de conejos vendidos es superior al numero de conejos que tienes en la granja. ")




                        # 6. Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes,
                        # determinadas sobre las siguientes condiciones:
                        # • NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante
                        # tendrá 3 evaluaciones.
                        # • NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante
                        # presentara 2 trabajos.
                        # • NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
                        # • Nota mínima 1,0 nota máxima: 5,0

# print("ingrese el numero de notas de sus 3 evaluaciones ")
# eva1=float(input("ingrese la nota de su primera evaluacion "))
# eva2=float(input("ingrese la nota de su segunda evaluacion "))
# eva3=float(input("ingrese la nota de su tercera evaluacion "))
# nP=(eva1*20/100)+(eva2*20/100)+(eva3*20/100)
# print("su nota de evaluacion es: ",nP)
# print("ingrese el numero de notas de sus 2  trabajos ")

# tbj1=float(input("ingrese la nota de su primer trabajo "))
# tbj2=float(input("ingrese la nota de su segundo trabajo "))
# nT=(tbj1*20/100)+(tbj2*20/100)
# print("la nota de sus trabajos es: ",nT)
# nF= nT + nP
# print("su nota final es: ", nF)


                        # 7. Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,
                        # cantidad y su precio con descuento. El descuento lo hace en base a la clave, si laclave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo
                        # existen dos claves).

# print("Bienvenido a Tu tienda virtual")
# print("logeate")
# uN=input("ingrese nombre de usuario: ")
# Cl=input("ingrese su clave de cliente elite: ")
# if Cl == "1":
#     nA=str(input("ingrese el nombre del articulo que quieres comprar. "))
#     pA=float(input("ingrese el valor del articulo para calcular tu descuento promocional por cliente elite. "))
#     pT = pA * (10/100)
#     dT = pA - pT 
#     print("El valor de su producto con el 10% por ser cliente elite ", uN,"es de:", dT)
#     print("no olvides seguir acumulando puntos y aumentando tu rango elite.")
#     print("hasta la proxima")
# elif Cl == "2":
#     nA=str(input("ingrese el nombre del articulo que quieres comprar. "))
#     pA=float(input("ingrese el valor del articulo para calcular tu descuento promocional. "))
#     pT = pA * (20/100)
#     dT = pA - pT 
#     print("El valor de su producto con el 20% por ser cliente TOP ELITE", uN,"es de:", dT)
#     print("¡Enhorabuena eres de nuestros clientes TOP ELITE!")
#     print("Gracias por preferirnos, hasta la proxima.")
# else:
#     print("ingresaste mal tu clave, recuerda que las clave de cliente elite asignadas estan en tu correo, revisa tu correo y confirma.")




                        # 8. En un hospital existen tres áreas: Psiquiatría, Pediatría, Traumatología. El
                        # presupuesto anual del hospital se reparte a estas tres (3) áreas; usted debe realizar
                        # un algoritmo que permita ingresar el valor del presupuesto anual, ingresar el
                        # porcentaje correspondiente a cada área, realizar el cálculo del presupuesto que
                        # corresponde a cada área, si la suma de los porcentajes no corresponde al 100% debe
                        # mostrar un mensaje de error.
                        # Mostrar el porcentaje asignado a cada área y el presupuesto obtenido.

# print("Seguimiento y presupuesto para tu hospital")
# preAnual=input("ingrese el monto de su presupuesto anual ")
# porPsi=input("presupuesto en porcentaje(omite el %) para el area de Psiquiatría: ")
# porPed=input("presupuesto en porcentaje(omite el %) para el area de Pediatría: ")
# porTra=input("presupuesto en porcentaje(omite el %) para el area de Traumatología: ")
# porTotal=float(porPsi)+float(porPed)+float(porTra)
# porPsi=float(porPsi)
# porPed=float(porPed)
# porTra=float(porTra)
# preAnual=float(preAnual)
# if porTotal == 100:

#     prePsi = preAnual * (porPsi/100)
#     print("El presupuesto para el area de Psiquiatria al cual se le invierte el",porPsi,"% correspondiente al presupuesto anual es de un valor de: $",prePsi)
    
#     prePed = preAnual * (porPed/100)
#     print("El presupuesto para el area de Pediatria al cual se le invierte el",porPed,"% correspondiente al presupuesto anual es de un valor de: $",prePed)
    
#     preTra = preAnual * (porTra/100)
#     print("El presupuesto para el area de Traumatologia al cual se le invierte el",porTra,"% correspondiente al presupuesto anual es de un valor de: $",preTra)

# elif porTotal < 100:

#     print("El porcentaje es menor al 100% recuerda especificar que hacer con el restante.")
    
#     prePsi = preAnual * (porPsi/100)
#     print("El presupuesto para el area de Psiquiatria al cual se le invierte el",porPsi,"% correspondiente al presupuesto anual es de un valor de: $",prePsi)
    
#     prePed = preAnual * (porPed/100)
#     print("El presupuesto para el area de Pediatria al cual se le invierte el",porPed,"% correspondiente al presupuesto anual es de un valor de: $",prePed)
    
#     preTra = preAnual * (porTra/100)
#     print("El presupuesto para el area de Traumatoligia al cual se le invierte el",porTra,"% correspondiente al presupuesto anual es de un valor de: $",preTra)

#     input("ingresa que haras con el restante, para actualizarnos segun tus necesidades.")
# else:
#     print("El valor de porcentajes es superior al 100% corrige y vuelve a intentarlo.")


                    # 9. Diseñar un algoritmo para determinar el precio del tiquete de ida y vuelta en avión,
                    # conociendo la distancia a recorrer, sabiendo que si el número de días de estancia es
                    # superior o igual a 7 y la distancia superior a 800 km el billete tiene una reducción
                    # del30%. El precio por km es de $2,5 dólares


