import requests, json, os, time

while True:
  print("🌟Dad Joke Generator🌟")
  print(" Time for a JOKE! ")
  print()
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  joke = result.json()
  print(joke["joke"])
  time.sleep(1)
  choice = input("Do you want to... (pick 1, 2, 3, or 4): \n1: Get a new joke \n2: Save this joke \n3: load an old joke\n4: load all previous jokes\n> ")
  if choice == "1":
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
    joke = result.json()
    print(joke["joke"])
    saveJoke = input("Do you want to save this joke? (y/n)\n> ")
    if saveJoke == "y":
      nameSave = input("What do you want to name this joke?\n> ")
      if nameSave == "":
        print("You must enter a name for the joke!")
      else:
        f = open(nameSave + ".txt", "w")
        f.write(joke["joke"])
        f.close()
        print("Your joke has been saved")
        time.sleep(1)
        os.system("clear")
    else:
        print("Okay, no problem!")
        time.sleep(1)
        os.system("clear")

  elif choice == "2":
    save = input("Give this joke a name!\n> ")
    if save == "":
      print("You must enter a name for the joke!")
    else:
      f = open(save + ".txt", "w")
      f.write(joke["joke"])
      f.close()
      print("Your joke has been saved")
      print()
      print()
  elif choice == "3":
      load = input("What joke do you want to load?\n> ")
      if load == "":
        print("You must enter the name for a joke!")
      else:
        f = open(load + ".txt", "r")
        print(f.read())
        f.close()
        time.sleep(2)
        os.system("clear")
  elif choice == "4":
    f = os.listdir()
    for i in f:
      if i.endswith(".txt"):
        print(i)
        f = open(i, "r")
        print(f.read())
        print()
        time.sleep(5)
        os.system("clear")