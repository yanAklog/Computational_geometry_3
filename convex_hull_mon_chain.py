import matplotlib.pyplot as plt

def orientation(point_1, point_2, point_3):
    return (point_2[0] - point_1[0])*(point_3[1] - point_1[1]) - (point_2[1] - point_1[1])*(point_3[0] - point_1[0])


def convex_hull(points):
    points = sorted(set(points))

    L_hull = []
    U_hull = []

    for i in points:
        while len(L_hull) >= 2 and orientation(L_hull[-2], L_hull[-1], i) <= 0:
            L_hull.pop()
        
        L_hull.append(i)
    
    for i in reversed(points):
        while len(U_hull) >= 2 and orientation(U_hull[-2], U_hull[-1], i) <= 0:
            U_hull.pop()
        
        U_hull.append(i)
    
    return L_hull[:-1] + U_hull[:-1]




points = []

with open("DS1.txt") as f:
    coordinates = f.readline()

    while coordinates:
        x = int((coordinates.split()[0]))
        y = int(coordinates.split()[1])
        points.append((x, y))
        coordinates = f.readline()


convex_hull = convex_hull(points)

with open("convex_hull.txt", 'w') as f:
    for i in convex_hull:
        f.write(f'{i[0]} {i[1]}\n')


px = 1/plt.rcParams['figure.dpi']
plt.figure(figsize=(960*px, 540*px))

plt.scatter([i[0] for i in points], [i[1] for i in points], color='orange')
plt.scatter([i[0] for i in convex_hull], [i[1] for i in convex_hull], color='blue')
plt.plot([i[0] for i in convex_hull], [i[1] for i in convex_hull], color='blue')
plt.plot([convex_hull[-1][0], convex_hull[0][0]], [convex_hull[-1][1], convex_hull[0][1]], color='blue')
plt.axis("off")
plt.savefig('convex_hull_image.png')