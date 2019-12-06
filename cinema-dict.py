# film name, age and seat left
films={
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Test2":[12,5]
    }

while True:
    choice = input ("What film do you want to watch today?:").strip().title()

    if choice in films:
        #now checking if the user is old enought to watch the film
        age = int(input("How old are you?:").strip())
        
        # checking to see if the person is old enough
        if age >= films[choice][0]: 
        # Checking if there are seat available
          if films[choice][1] > 0:
              print("Enjoy the film!")
                #reduce the number of available seats
              films[choice][1]= films[choice][1] - 1
          else:
              print("Sorry!, we are sold out!")
            
        else:
            print("Sorry! you are too young to see the film!")
            
    else:
        print("Sorry! we dont have that film")

    
