import math
AB=int(input())
BC=int(input())
hypotenuse=math.hypot(AB,BC)                      
angle = math.acos(BC/hypotenuse)
angleToDegrees = math.degrees(angle)
print(round(angleToDegrees))
