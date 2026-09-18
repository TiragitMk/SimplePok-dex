import requests as r

poke_set = r.get("https://pokeapi.co/api/v2/pokemon/?limit=1351").json()["results"]
poke_options = set()
for i in poke_set:
    poke_options.add(i["name"])
poke_options.add("exit")

while True:

    pokemon = input("Type in the pokemon's name (in lowercase) or 'exit': ")
    if pokemon not in poke_options:
        print("Unknown pokemon. Type in lowercase (as in 'pikachu') or type 'exit' without quotes.")
        continue
    elif pokemon == "exit":
        print("Turning off the pokédex...")
        break
    poké_request = r.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    dex_entry = poké_request.json()
    pokedex_display = ""
    poke_nombre = dex_entry["name"].capitalize()
    pokedex_display += poke_nombre + ": " f"Number {dex_entry["id"]}.\n"

    tipos = ""
    for tp in dex_entry["types"]:
        if tp["slot"] == 2:
            tipos += " and "
        tipos += tp["type"]["name"].capitalize()

    mensaje_tipo = poke_nombre + " is a " + tipos + " type pokemon. \n"

    habilidades = ""
    for ability in dex_entry["abilities"]:
        # Los pokémon siempre tienen habilidad oculta, así que siempre acaba en 'and habilidad'.
        if ability["slot"] == 2:
            habilidades += ", "
        elif ability["slot"] == 3:
            habilidades += " and "
        habilidades += ability["ability"]["name"].capitalize()

    if len(dex_entry["abilities"]) == 1:
        mensaje_habilidad = "Its ability is " + habilidades + "."
    elif len(dex_entry["abilities"]) > 1:
        mensaje_habilidad = "Its abilities are " + habilidades + "."

    print(pokedex_display + mensaje_tipo + mensaje_habilidad)