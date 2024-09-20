number=int(input("Enter any number:"))
while True:
    if number%3==0 and number%5==0:
        print("Fizz Buzz")
        next_num=int(input("Again enter any number:"))
        number += next_num
    elif number%3==0:
        print("Fizz")
        next_num=int(input("Again enter any number:"))
        number += next_num
    elif number%5==0:
        print("Buzz")
        next_num=int(input("Again enter any number:"))
        number += next_num
    else:
        print("Fizz")
        print("You lost")
        break
    
    


    
            
          
       


    

  
        

       
        
       