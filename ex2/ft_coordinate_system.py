import sys

def ft_coordinate_system() -> tuple [float, float, float]:
    print("===Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    cordinates :  tuple [float, float, float] 
    while True:
        try:
            text = input("Enter new coordinates as floats in format 'x,y,z': ")
            xyz = text.split(",") 
            #text halinde x,y,z formatinda girilmelidir halen textir
        except ValueError as error:
            print("Invalid syntax")
            continue
        for i in range(1 , 4):
            try:
                tuple
			
            
        
        
        return xyz