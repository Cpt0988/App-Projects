

try:    
    width: float=input("Enter rectangle width: ")
    length :float=input("Enter rectangle length: ")
    
    if width == length:
        exit("That look like a square.")

    area :int = width * length
    print(area)
except ValueError:
    print('Enter a number,please.')