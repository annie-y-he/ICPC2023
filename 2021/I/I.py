import math

class Vec3:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  @staticmethod
  def add(v1, v2):
    return Vec3(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

  @staticmethod
  def subtract(v1, v2):
    return Vec3(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

  @staticmethod
  def magnitude(v):
    return (v.x**2 + v.y**2 + v.z**2)**0.5

  @staticmethod
  def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

  @staticmethod
  def cross(v1, v2):
    return Vec3(v1.y * v2.z - v1.z * v2.y,
                v1.z * v2.x - v1.x * v2.z,
                v1.x * v2.y - v1.y * v2.x)
  @staticmethod
  def angle_between(v1, v2):
    dp = Vec3.dot(v1, v2)
    mnt = Vec3.magnitude(v1) * Vec3.magnitude(v2)
    cosa = max(min(dp / mnt, 1.0), -1.0)
    return math.acos(cosa)
  
  def __str__(self):
    return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
  


# Test
v1 = Vec3(1.6, 2.3, 3.9)
v2 = Vec3(4.1, 5.4, 6.8)

print(Vec3.add(v1, v2))
print(Vec3.subtract(v1, v2))
print(Vec3.magnitude(v1))
print(Vec3.dot(v1, v2))
print(Vec3.cross(v1, v2))
