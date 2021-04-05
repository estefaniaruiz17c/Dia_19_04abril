# Manejo de fechas en Python
print("Manejo de fechas en Python")

from datetime import datetime, date, timedelta
# Creación del primer archivo de texto en replit, que contendrá los ejercicios de manejo de fechas del archivo 'fechas_1.txt'
file_slash = open('operaciones_fechas_1.txt', 'w')

# Primera frase del archivo nuevo
file_slash.write("Ejercicios de manejo de fechas del texto 'fechas_1.txt'\n")
file_slash.write("\n")

# Para acceder al archivo de texto de 'fechas_1.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
slash = open('fechas_1.txt','r')
texto1 = slash.read()
# Es importante cerrar este archivo antes de proseguir con el código
slash.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_slash.write("- Las fechas del primer texto de la 1 a la 6 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'fechas_1.txt'
file_slash.write(texto1)
file_slash.write("\n")

# Para acceder al archivo de texto de 'fechas_1.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
slash = open('fechas_1.txt','r')
texto1lis = slash.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
slash.close()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
print()
print(texto1lis)
print()
f1 = (texto1lis[1].rstrip('\n'))
f2 = (texto1lis[2].rstrip('\n'))
f3 = (texto1lis[3].rstrip('\n'))
f4 = (texto1lis[4].rstrip('\n'))
f5 = (texto1lis[5].rstrip('\n'))
f6 = (texto1lis[6].rstrip('\n'))
#print(list(f1))
#print(list(f3))
# Operaciones entre fechas
file_slash.write("\n")
file_slash.write("- Operaciones entre fechas: \n")
file_slash.write("\n")

# Sumaremos 30 días a la primera fecha
file_slash.write("- Sumaremos 30 días a la primera fecha con timedelta() y strptime(): \n")

file_slash.write("\n")

# usamos strptime para convertir el string al formato date
date1 = datetime.strptime(f1,'%d/%m/%Y')
file_slash.write("Fecha 1: ")
file_slash.write(str(date1))

file_slash.write("\n")

# Realizamos la suma de los 30 días y ponemos la respuesta en el archivo 'operaciones_fechas_1.txt'
suma3d = (date1 + timedelta(days=30))
file_slash.write("30 días más de la fecha 1: ")
file_slash.write(str(suma3d))
print(suma3d)

file_slash.write("\n")
# Comparararemos 4 fechas, si la comparación es verdadera saldrá True, de otro modo, saldrá False
file_slash.write("\n- Comparación fecha 2 y fecha 3: \n")

# Verificar si la fecha 2 es menor a la fecha 3
comp1 = f2 < f3
file_slash.write("\nEs la fecha 2 menor que la fecha 3?: ")

file_slash.write("\n")

# Escribir la respuesta de la comparación anterior en 'operaciones_fechas_1.txt'
file_slash.write(str(comp1))
print(comp1)
file_slash.write("\n")

# Comparación fecha 4 y 5
file_slash.write("\n- Comparación fecha 4 y fecha 5: \n")

# Verificar si la fecha 4 y 5 son diferentes
comp2 = f4 != f5
file_slash.write("\nEs la fecha 4 diferente a la fecha 5?: ")

file_slash.write("\n")

# Escribir la respuesta de la comparación anterior en 'operaciones_fechas_1.txt'
file_slash.write(str(comp2))
print(comp2)

file_slash.write("\n")

# Restaremos 9 días a la primera fecha
file_slash.write("\n- Restaremos 9 días a la sexta fecha con timedelta(): \n")

file_slash.write("\n")

# usamos strptime para convertir el string al formato date
date6 = datetime.strptime(f6,'%d/%m/%Y')
file_slash.write("Fecha 6: ")
file_slash.write(str(date6))

file_slash.write("\n")

# Realizamos la resta de 9 días y ponemos la respuesta en el archivo 'operaciones_fechas_1.txt'
resta9d = (date6 - timedelta(days=9))
file_slash.write("9 días menos de la fecha 6: ")
file_slash.write(str(resta9d))
print(resta9d)

#fecha1_1= int(fecha1[0:4])
#print(fecha1_1)
#fecha1_2= int(fecha1[5:7])
#print(fecha1_2)
#fecha1_3= int(fecha1[8:])
#print(fecha1_3)
#print(texto1)
#fest = datetime.date(int(texto1))
#file_festivos.write(str(fest))
#file_festivos.write("{:%d de %B de %Y}".format(texto1))
#file_festivos.write("\n")
file_slash.close()

print("--------"*8)

# Crear y abrir el archivo 'operaciones_fechas_2.txt'
file_parent = open('operaciones_fechas_2.txt', 'w')

# Primera frase del archivo nuevo
file_parent.write("Ejercicios de manejo de fechas del texto 'fechas_2.txt'\n")
file_parent.write("\n")

# Para acceder al archivo de texto de 'fechas_2.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
parent = open('fechas_2.txt','r')
texto2 = parent.read()
# Es importante cerrar este archivo antes de proseguir con el código
parent.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_parent.write("- Las fechas del segundo texto de la 1 a la 4 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'fechas_2.txt'
file_parent.write(texto2)
file_parent.write("\n")

# Para acceder al archivo de texto de 'fechas_2.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
parent = open('fechas_2.txt','r')
texto2lis = parent.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
parent.close()

print((texto2lis))
print()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
d1 = (texto2lis[1].rstrip('\n'))
d2 = (texto2lis[2].rstrip('\n'))
d3 = (texto2lis[3].rstrip('\n'))
d4 = (texto2lis[4].rstrip('\n'))

print()
print(type(d1))

# De esta manera, cada fecha queda en modo string, pero para las funciones que usaremos ahora, se requiere que los números de la fecha sean de tipo int, para eso haremos la conversión de manera individual para cada número que está separado por comas

# Cambiar cada número de string a int para la fecha 1 del texto 2, d1 
d1_1= int(d1[1:5])
print(d1_1)
d1_2= int(d1[6:8])
print(d1_2)
d1_3= int(d1[9:11])
print(d1_3)

# Cambiar cada número de string a int para la fecha 2 del texto 2, d2 
d2_1= int(d2[1:5])
print(d2_1)
d2_2= int(d2[6:8])
print(d2_2)
d2_3= int(d2[9:11])
print(d2_3)

# Cambiar cada número de string a int para la fecha 3 del texto 2, d3 
d3_1= int(d3[1:5])
print(d3_1)
d3_2= int(d3[6:8])
print(d3_2)
d3_3= int(d3[9:11])
print(d3_3)

# Cambiar cada número de string a int para la fecha 4 del texto 2, d4 
d4_1= int(d4[1:5])
print(d4_1)
d4_2= int(d4[6:8])
print(d4_2)
d4_3= int(d4[9:11])
print(d4_3)

# Empezaremos con los ejercicios
file_parent.write("\n- Ejercicios con funciones: \n")

# date(): forma de mostrar la fecha de distintas maneras
file_parent.write("\n- date(): \n")

# Usar date colocando los argumentos ya transformados en int 
fech1 = date(d1_1,d1_2,d1_3)
file_parent.write("\nFecha 1 representada de la manera 1: ")
file_parent.write(str(fech1))
print(fech1)

# Otra froma de representar esta fecha, tal como las indicadas en el texto 1. Mostrar el resultado en 'operaciones_fechas_2'
a1 = ( "{:%d/%m/%y}".format(fech1))
file_parent.write("\nFecha 1 representada de la manera 2: ")
file_parent.write(str(a1))

file_parent.write("\n")

# date(): forma de mostrar la fecha de una manera, y uso de .day(), .month(), .year() para ver específicamente cada valor
file_parent.write("\n- date(), .day(), .month(), .year(): \n")

# Usar date colocando los argumentos ya transformados en int 
fech2 = date(d2_1,d2_2,d2_3)
# Mostrar la fecha como sale con date
file_parent.write("\nFecha 2: ")
file_parent.write(str(fech2))
# Mostrar el día de la fecha 2
file_parent.write("\nDía fecha 2: ")
file_parent.write(str(fech2.day))
# Mostrar el año de la fecha 2
file_parent.write("\nAño fecha 2: ")
file_parent.write(str(fech2.year))
# Mostrar el mes de la fecha 2
file_parent.write("\nMes fecha 2: ")
file_parent.write(str(fech2.month))

print(fech2)

file_parent.write("\n")
# date() y otras formas de imprimir la fecha
file_parent.write("\n- date() y otras formas de mostrar la fecha: \n")

# Usar date colocando los argumentos ya transformados en int 
fech3 = date(d3_1,d3_2,d3_3)
file_parent.write("\nFecha 3: ")
file_parent.write(str(fech3))

# Forma 1: 'día de la semana abreviado', 'día' de 'nombre del mes abreviado' de 'año escrito con 2 dígitos'
a3_1 = ( "{:%a, %d de %b de %y}".format(fech3))
file_parent.write("\nFecha 3 representada de la manera 1: ")
file_parent.write(str(a3_1))

# Forma 2: 'día de la semana completo', 'día' de 'nombre del mes abreviado' de 'año escrito con 4 dígitos'
a3_2 = ( "{:%A, %d de %b de %Y}".format(fech3))
file_parent.write("\nFecha 3 representada de la manera 2: ")
file_parent.write(str(a3_2))

# Forma 3: 'día de la semana abreviado', 'día' de 'nombre del mes completo' de 'año escrito con 2 dígitos'
a3_3 = ( "{:%a, %d de %B de %y}".format(fech3))
file_parent.write("\nFecha 3 representada de la manera 3: ")
file_parent.write(str(a3_3))

# Forma 4: 'día de la semana completo', 'día' de 'nombre del mes completo' de 'año escrito con 4 dígitos'
a3_4 = ( "{:%A, %d de %B de %Y}".format(fech3))
file_parent.write("\nFecha 3 representada de la manera 4: ")
file_parent.write(str(a3_4))

file_parent.write("\n")

# date(), weekday() y otra forma de imprimir la fecha
file_parent.write("\n- date(), weekday() y otra forma de imprimir la fecha: \n")

# Usar date colocando los argumentos ya transformados en int 
fech4 = date(d4_1,d4_2,d4_3)
file_parent.write("\nFecha 4: ")
file_parent.write(str(fech4))

# Fecha en fomato largo
a4_2 = ( "{:%c}".format(fech4))
file_parent.write("\nFecha 4 en fomato largo: ")
file_parent.write(str(a4_2))

# weekday(): el lunes sería el día 0, martes día 1, miércoles día 2, jueves día 3, viernes día 4, sábado día 5, domingo día 6
file_parent.write("\nWeekday() fecha 4: ")
file_parent.write(str(fech4.weekday()))

file_parent.write("\n")

# Cerramos el archivo 'operaciones_fechas_2.txt'
file_parent.close()