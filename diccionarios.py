yo = {"nombre": "Nicolas", "edad": 21, "es_estudiante": True}

yo_lista = ["Nicolas", 21, True]
print(yo_lista[0])
print(yo["nombre"])

# Modificar un elemento
yo_lista[0] = "Nicolas Trocha"
print(yo_lista)
yo["nombre"] = "Nicolas Trocha"
print(yo)
# Agregar un elemento
yo_lista.append("cra 45 #54-46")  # -->Lista
yo["direccion"] = "cra 45 #54-46"
yo["telefono"] = "+57 3008232101"

#Update
yo_2 = {"rh": "o+", "profesion": "Cientifico de datos"}
yo.update(yo_2)
print(yo)

eliminado_1 = yo.pop("profesion")
eliminado_2 = yo.pop("rh")
print(eliminado_1)
print("="*50)
print(yo)