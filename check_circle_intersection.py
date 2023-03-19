
import math
import matplotlib.pyplot as plt

print("Input x1, y1, r1, x2, y2, r2:")
x1,y1,r1,x2,y2,r2 = 1,1,4,1,1,5#[int(i) for i in input().split()]
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d <= r1-r2:
    print("C2  is in C1")
elif d <= r2-r1:
    print("C1 (" , x1,y1,r1, ") is in C2")
elif d < r1+r2:
    print("Circumference of C1  and C2  intersect")
elif d == r1+r2:
    print("Circumference of C1 and C2 will touch")
else:
    print("C1 and C2  do not overlap")

figure, axes = plt.subplots()
colored_circle =plt.Circle((x1, x2), r1, color='blue')
axes.set_aspect( 1 )
axes.add_artist( colored_circle )
plt.title( 'Colored Circle' )
#plt.show()
