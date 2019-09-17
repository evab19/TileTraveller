
[x,y] = [1,1]
 

while [x,y] != [3,1]:
    
    if [x,y] == [1,1]:
        print("You can travel: (N)orth.")
        direction = str.lower(input("Direction: "))
        if direction == "n":
            y += 1
        else:
            print("Not a valid direction!")
            


    elif [x,y] == [1,2]:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = str.lower(input("Direction: "))
        if direction == "n":
            y += 1
        elif direction == "e":
            x += 1
        elif direction == "s":
            y -= 1
        else: 
            print("Not a valid direction")
            
    
    elif [x,y] == [1,3]:
        print("You can travel: (E)ast or (S)outh.")
        direction = str.lower(input("Direction: "))
        if direction == "s":
            y -= 1
        if direction == "e":
            x +=  1
        else:
            print("Not a valid direction!")
            
    
    elif [x,y] == [2,1]:
        print("You can travel: (N)orth.")
        direction = str.lower(input("Direction: "))
        if direction == "n":
            y += 1
        else:
            print("Not a valid direction!")
            

    elif [x,y] == [2,2]:
        print("You can travel: (S)outh or (W)est.")
        direction = str.lower(input("Direction: "))
        if direction == "s":
            y -= 1
        elif direction == "w":
            x -= 1
        else:
            print("Not a valid direction!")
            

    elif [x,y] == [2,3]:
        print("You can travel: (E)ast or (W)est.")
        direction = str.lower(input("Direction: "))
        if direction == "e":
            x += 1
        elif direction == "w":
            x -= 1
        else:
            print("Not a valid direction!")
            

    elif [x,y] == [3,3]:
        print("You can travel: (S)outh or (W)est.")
        direction = str.lower(input("Direction: "))
        if direction == "w":
            x -= 1
        elif direction == "s":
            y -= 1
        else:
            print("Not a valid direction!")
            

    elif [x,y] == [3,2]:
        print("You can travel: (N)orth or (S)outh.")
        direction = str.lower(input("Direction: "))
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        else:
            print("Not a valid direction!")
            

print("Victory!")