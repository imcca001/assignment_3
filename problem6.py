p = (0.00, 0.00, 0.00)
a = (20.900, 15.300, 20.400)
b = (0.600,34.700,8.100)
c = (12.100,15.800,2.300)
d = (15.000,5.800,16.900)

point_list = [a, b, c, d]

import math

def euclid_distance(p, q):
    distance = math.sqrt(((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2) + ((p[2] - q[2]) ** 2))
    #print distance
    return distance

#euclid_distance(p, q)

#This function was use to find the shortest distance between the origin, "p" in the points above and the rest of the points
def check_distance(origin, distances):
    for point in distances:
        distance = 0
        farthest_point = ''
        if euclid_distance(origin, point) < distance or distance == 0:
            distance = euclid_distance(origin, point)
            farthest_point = point
    #print distance, farthest_point
    return distance
    #return farthest_point

#check_distance(p, point_list)

def check_list(distances):
    distance = 0
    first_point = ''
    second_point = ''
    for first in distances:
        for second in distances:
            if ((euclid_distance(first, second) < distance or distance == 0) and (first != second)):
                distance = euclid_distance(first, second)
                first_point = first
                second_point = second
    print first_point, second_point, distance

check_list(point_list)
