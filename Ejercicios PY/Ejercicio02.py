def promedio_modificado(notas):
    # Eliminar la peor nota 
    notas.remove(min(notas))

    # Duplicar la mejor nota
    notas.append(max(notas))

    # Calcular el nuevo promedio
    return sum(notas) / len(notas)

# Entrada de notas
entrada = input("Ingrese las notas separadas por espacio: ")
notas = list(map(int, entrada.split()))

# Resultado
print("Promedio final:", promedio_modificado(notas))

