import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
with open(path1, "r") as file1:
    cen_x, cen_y = map(int, file1.readline().split())
    rad_x, rad_y = map(int, file1.readline().split())
with open(path2, "r") as file2:
    points_coord = file2.readlines()
    for i in range (len(points_coord)):
        points_coord[i] = points_coord[i].replace("\n", "")

for coord in points_coord:
    coord_x, coord_y = map(int, coord.split())
    if (coord_x - cen_x) ** 2 + (coord_y - cen_y) ** 2 < (rad_x - cen_x) ** 2 + (rad_y - cen_y) ** 2:
        print(1)
    elif (coord_x - cen_x) ** 2 + (coord_y - cen_y) ** 2 > (rad_x - cen_x) ** 2 + (rad_y - cen_y) ** 2:
        print(2)
    else:
        print(0)