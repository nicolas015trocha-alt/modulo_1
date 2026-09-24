contactos = {
    "maria":{
        "nombre_completo":"MARIA JOSE HERNANDEZ CARRILLO",
        "telefono":"314567890",
        "direccion":"La Chinita"
    },
    "nicolas":{
        "nombre_completo":"NICOLAS DAVID TROCHA SIMANCAS",
        "telefono":"3008232101",
        "direccion":"El Silencio"
    }
}

print(contactos.keys())

for i,key in enumerate(contactos):
    print(i+1,"-",key)