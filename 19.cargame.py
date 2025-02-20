command=input(">")
started=False
while command.upper() != "QUIT":
    if command.upper()=="HELP":
        print("Start-To start the car\nStop-To stop the car\nQuit-To Exit")
    elif command.upper()=="START":
        if started:
            print("Car is already started")
        else:  
            print("Car started.Ready to go")
            started=True
    elif command.upper()=="STOP":
        if not started:
            print("Car is already stopped")
        else:
            print("Car stopped")  
            started=False
    else:
        print("Invalid output Press HELP for assistance")  
    command=input(">")    
else:
  print("Quitting the game")
  
    
           

  