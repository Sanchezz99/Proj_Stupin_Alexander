def numeric_axis(A, B, C):
   if A > B:
       distance_B = A - B
   else:
       distance_B = B - A
   if A > C:
       distance_C = A - C
   else:
       distance_C = C - A
   if distance_B < distance_C:
       axis_point = "B"
       main_distance = distance_B
   else:
       axis_point = "С"
       main_distance = distance_C
   return axis_point, main_distance
A = 6
B = 8
C = 7
axis_result = numeric_axis(A, B, C)
print(f"Самая близкая точка к A: {axis_result[0]}")
print(f"Расстояние от A: {axis_result[1]}")
