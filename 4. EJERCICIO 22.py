#Capitulo 4. Ejercicio propuesto 22

nombre = input("Ingrese el nombre del empleado: ")
salario_hora = float(input("Ingrese el salario básico por hora: "))
horas_trabajadas = int(input("Ingrese el número de horas trabajadas al mes: "))
salario_mensual = salario_hora * horas_trabajadas

if salario_mensual > 450000:
  print(f"Nombre: {nombre}, Salario mensual: {salario_mensual}")
else:
  print(f"Nombre: {nombre}")
