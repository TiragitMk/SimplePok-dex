import requests as consulta

categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
#print("categorias: ",categorias.json())
lista_categoria = categorias.json()
lista_categoria_dic=[]
num=0
for i in lista_categoria:
    
    lista_categoria_dic.append({"clave":num, "valor":i})
    num = num +1

for diccionario in lista_categoria_dic:
    print(f"{diccionario['clave']} - {diccionario['valor']}")  

seleccion = int(input("Seleccione un numero para categoria: ") )
categoria_seleccionada=None
for diccionario in lista_categoria_dic:
    if diccionario['clave'] == seleccion:
        categoria_seleccionada = diccionario['valor']
        #print(f"tu seleccion fue {diccionario['valor']}")

#print("ultimo dato de lista categoria: ",lista_categoria[len(lista_categoria)-1])
response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

#print("codigo http de respuesta: ",response.status_code)   CÓDIGO DE RESPUESTA
#print("cabecera: ",response.headers['content-type'])       HEADERS: CATEGORÍAS
#print("encoding: ",response.encoding)                      ENCODING (LÍMITE DEL CONTENIDO TEXTUAL)
#print("respuesta en string: ",response.text)               PASA EL CONTENIDO A STR.
print("respuesta en json:",response.json())                 # PASA EL CONTENIDO A JSON

