import turtle

N = int(input())
v = []

scale = 20
while len(v) < N:
  line = input().split()
  for i in range(0, len(line)//2):
    v.append((float(line[i*2]), float(line[i*2+1])))
# turtle.hideturtle()
# turtle.penup()
# turtle.goto(v[len(v)-1][0]*scale, v[len(v)-1][1]*scale)
# turtle.pendown()
# for vt in v:
#   turtle.goto((vt[0]*scale, vt[1]*scale))
# turtle.exitonclick()

def polygon_centroid(points):
  n = len(points)
  if n == 0:
    return None
  
  # Ensure the polygon is closed by adding the start point to the end of the list.
  points.append(points[0])
  
  # Calculate signed polygon area
  A = sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in zip(points, points[1:])) / 2.0

  # Calculate centroid coordinates
  Cx = sum((x0 + x1) * (x0*y1 - x1*y0) for ((x0, y0), (x1, y1)) in zip(points, points[1:])) / (6*A)
  Cy = sum((y0 + y1) * (x0*y1 - x1*y0) for ((x0, y0), (x1, y1)) in zip(points, points[1:])) / (6*A)
  
  return (Cx, Cy)

print(polygon_centroid(v))

print(v)
