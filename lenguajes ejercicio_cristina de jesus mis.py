import re

opcion =0
while opcion !=10:
    #print(diccionario)

    print("\n selecciona una opcion")
    print("1.Todas las palabras que tengan una longitud de 7 o más letras\n2.Expresiones que NO finalicen con una vocal.\n3.Las palabras que inicien con “M” donde la segunda letra no sea vocal\n4.Expresiones encerradas entre comillas\n5.Ip’s\n6.Horas\n7.Telefonos\n8.Correos electrónicos\n9.Url’s\n10.Código postal")
    opcion = int(input("ingrese una opción: "))

    if opcion == 1:
      texto= "ejercicios de la materia de lenguajes y automatas"
        print(texto, end="\n")
        regex = "[a-zA-Z]\d{7}"
        if re.search(regex,texto):
           print("si hay palabras de 7 o mas letras")
        else:
            print("no hay palabras de 7 o mas letras") 
    elif opcion == 2:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "[A-Za-z]+"
        if re.search(regex,texto):
           print("si hay palabras que terminan con vocal")
        else:
            print("no hay palabras que terminan con vocal") 
    elif opcion == 3:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "[M][^aeiou][A-Za-z]"
        if re.search(regex,texto):
           print("si hay palabras que inician con M")
        else:
            print("no hay palabras que inician con M") 
    elif opcion == 4:
            texto="ejercicios de la materia de lenguajes y automatas"
        regex = "((1[0-2]|0?[1-9]):([0-5][0-9]?([AaPp][Mm]"
        if re.search(regex,texto):
           print("si hay una expresion encerrada en comillas")
        else:
            print("no hay una expresion encerrada en comillas")
    elif opcion == 5:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "((1[0-2]|0?[1-9]):([0-5][0-9]?([AaPp][Mm]"
        if re.search(regex,texto):
           print("si hay una Ip's")
        else:
            print("no hay una Ip's")
    elif opcion == 6:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "((1[0-2]|0?[1-9]):([0-5][0-9]?([AaPp][Mm]"
        if re.search(regex,texto):
           print("si hay una hora")
        else:
            print("no hay una hora")
    elif opcion == 7:
        texto="ejercicios de la materia de lenguajes y automatas 9851158687"
        regex = "(\+?\d[2]|\(\+?\d[2]\))?(\d{8,12})"
        if re.search(regex,texto):
           print("si hay un telefono")
        else:
            print("no hay un telefono")
    elif opcion == 8:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "([a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})+"
        if re.search(regex,texto):
           print("si hay un correo electronico")
        else:
            print("no hay un correo electronico")
    elif opcion == 9:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "(?:(?:https?|http|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&#\/%=~_|])"
        if re.search(regex,texto):
           print("si hay una url's")
        else:
            print("no hay una url's")
    elif opcion == 10:
        texto="ejercicios de la materia de lenguajes y automatas"
        regex = "(\d{5})"
        if re.search(regex,texto):
           print("si hay un codigo postal")
        else:
            print("no hay un codigo postal")

    else:
        print("\n¡¡¡La opción Seleccionada es Incorrecta!!!")
        
