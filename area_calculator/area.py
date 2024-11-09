import math

def paint_calc(height,width,cover):
    cans= (math.ceil(height*width/cover))
    print(f"number of cans required :{cans}")

t_height=int(input("enter the height : "))
t_width=int(input("enter the width : "))
coverage=5
paint_calc(height=t_height,width=t_width,cover=coverage)
