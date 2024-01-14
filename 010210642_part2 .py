# devim akarer / term project / part-2
# open levelling net computation

import math

print("This program calculates the elevations in open levelling net")
print("------------------------------------------------------------")

# list (we will use later)

point_ID = []
bs_list = []
fs_list = []
dh_list = []
el_list = []
un_point_ID = []

# input

firstID = input("Enter the point ID of known point     : ")
point_ID.append(firstID)
elevation_of_point_a = float(input("Enter the elevation of point A(m)     : "))
el_list.append(elevation_of_point_a)
number_of_unknown = input("Enter the number of unknown points    : ")
for dev in range(int(number_of_unknown)):
    im = input("Enter the ID of unknown point "+str(dev + 1)+"       "+": ")
    un_point_ID.append(im)
    point_ID.append(im)

new = point_ID[:-1]
for dev in range(len(point_ID) - 1):
    akr = input("Enter the BS reading of point " + str(new[dev]) + "(m)" + "    " + ": ")
    bs_list.append(akr)
    er = input("Enter the FS reading of point " + str(un_point_ID[dev]) + "(m)" + "    " + ": ")
    fs_list.append(er)

# delta H

for dev in range(len(point_ID) - 1):
    dh = float(bs_list[dev]) - float(fs_list[dev])
    dh_list.append(dh)

# elevation

for dev in range(len(point_ID) - 1):
    el = float(dh_list[dev]) + float(el_list[dev])
    el_list.append(el)

# output

print("\n")
print(format("Point ID", "15s"), format("Point ID", "15s"), "Delta H")
print("_________________________________________")
akr = point_ID[:-1]
for dev in range(len(bs_list)):
    print(format(akr[dev], "15s"), format(un_point_ID[dev], "15s"), format(dh_list[dev], ".3f"))
print("_________________________________________")
print("\n")
print(format("Point ID", "15s"), "Elevation")
print("_________________________")
for dev in range(len(fs_list)):
    print(format(un_point_ID[dev], "15s"), format(el_list[dev + 1], ".3f"))
print("_________________________")
