def promedio_modificado(notas):
    # Eliminar la peor nota 
    notas.remove(min(notas))

    # Duplicar la mejor nota
    notas.append(max(notas))

    # Calcular el nuevo promedio
    return sum(notas) / len(notas)

# Ejemplo
notas = [12, 15, 17, 14]
print("Promedio final: ", promedio_modificado(notas))