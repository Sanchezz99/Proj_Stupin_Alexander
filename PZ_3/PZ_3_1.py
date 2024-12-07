def coordinates_rectangle(x, y, x1, y1, x2, y2):
    return (x1 < x < x2) and (y1 < y < y2)
x = 4
x1 = 3
x2 = 5
y = 8
y1 = 7
y2 = 9
result = coordinates_rectangle(x, y, x1, y1, x2, y2)
print(result)