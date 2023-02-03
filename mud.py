while True:
  try:
    charac_choice = input("What Story Line do you want to choose?(Hero,Villian,Support,God):\n")
    if charac_choice == ("Hero"):
        print("Correct")
        break
    if charac_choice == ("Villian"):
        print("Correct")
        break
    if charac_choice == ("Support"):
        print("Correct")
        break
    if charac_choice == ("God"):
        print("Correct")
        break
    print("Wrong Choice (Please type the choice exactly as shown!)")
  except Exception as e:
    print(e)