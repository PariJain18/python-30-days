points = [(2,3),(5,1),(1,1),(7,4),(3,2)]
closest_point=points[0]
smallest_distance=999
for point in points:
    distance=point[0]**2+point[1]**2
    if distance<smallest_distance:
        smallest_distance=distance
        closest_point=point
print("Closest point:",closest_point)