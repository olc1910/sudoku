board = input("Where is the board as txt located witch you wanna generate as python list: ")
with open(board, 'r') as file:
    lines = file.readlines()
result = []
    
for line in lines:
    numbers = [int(num) for num in line.split()]
    result.append(numbers)
for row in result:
    print(row)