# files.py
# Part 1
OUT_FILE = "name.txt"
name = input("Enter name: ")
with open(OUT_FILE, 'w') as out_file:  
    print(name, file=out_file)

# Part 2
with open(OUT_FILE, 'r') as in_file: 
    text = in_file.read().strip()  
print(f"Your name is {text}")

# Part 3
NUMBERS_FILE = "numbers.txt"
with open(NUMBERS_FILE, 'w') as out_file:  
    out_file.write('17\n')
    out_file.write('42\n')
    out_file.write('400\n')

total = 0
with open(NUMBERS_FILE, 'r') as in_file: 
    for _ in range(2):  # Only sum the first two numbers
        value = in_file.readline().strip() 
        total += int(value)  
print(f"Total of first two numbers: {total}")


# Part 4
with open(NUMBERS_FILE, 'r') as in_file:  
    print("All numbers in the file:")
    for line in in_file:  
        print(line.strip())  
