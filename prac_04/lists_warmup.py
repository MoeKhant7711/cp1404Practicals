numbers = ["ten", 1, 4, 1, 5, 9, 1]

print(numbers[0])            
print(numbers[len(numbers)-1]) 
print(numbers[3])           
print(numbers[:len(numbers)-1]) 
print(numbers[3:4])          
print(5 in numbers)          
print(7 not in numbers)      
print("3" not in numbers)    
print(numbers + [6, 5, 3])   
numbers[0] = "TEN"           
numbers[-1] = 100            
print(numbers[2:])          
print(9 in numbers)          
