number = int(input())

if(number < 1):
   print("Invalid number entered")
while number > 1:
      if(number % 2)==0:
        number = number / 2
        steps +=1
        print(number)
      else:
           number = number * 3 + 1
           print(number)
           steps +=1
print("steps =" + str(steps))         
       
  
 

    
