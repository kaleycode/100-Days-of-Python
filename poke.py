import requests, os, time
while True:
    base_url = "https://pokeapi.co/api/v2/"
    name = input("What Pokemon do you want?\n>")
    os.system("clear")
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    pokeData = response.json()
    print(f"Name: {pokeData["name"]}")
    time.sleep(.2)
    print(f"ID: {pokeData["id"]}")
    time.sleep(.2)
    print(f"Height: {pokeData["height"]}")
    time.sleep(.2)
    print(f"Weight: {pokeData["weight"]}")
    print()
