1. mk.sh
```bash
#!/bin/sh

for i in $(seq 1 $1); do
  touch "in$i.txt"
  touch "out$i.txt"
done
```
`./mk.sh 3`  
creates 3 sets of in/out txt files

2. run.sh
```bash
#!/bin/sh

python ./*.py < in$1.txt > output.txt
dos2unix -q output.txt
diff output.txt out$1.txt
echo $?
```
`./run.sh 1`  
runs test case 1 and give diff result

3. init.sh
```bash
#!/bin/sh

for dir in $(seq 65 $(printf '%d\n' "'$1")); do
  c="$(printf "\\$(printf '%03o' "$dir")")"
  mkdir "$c"
  touch "$c/$c.py"
  cp mk.sh "$c/mk.sh"
  cp run.sh "$c/run.sh"
done
```
`./init.sh O`  
creates folders from A to O with A.py and copies mk.sh and run.sh

**TIPS**
------------------
- Analyze time complexity. According to given range, given time limit and memory limit.
- consider edge cases.
- think of common problems like fib

**Python Functions**
------------------
- str.ljust(), str.rjust(), str.center()
- ord()
- zip()
- f"{number:05}"
- str.zfill()
- "{:0>5}".format(s)
- unpack *
- slice [start:end:step]
- io.StringIO()
- weaved_str = ''.join([str1[i:i+1] + str2[i:i+1] for i in range(max(len(str1), len(str2)))])
- bin(), hex(), oct()
- int(binary_str, 2)
- join()
- vec3 !!write a full geometry class
```py
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
```

- combination
```py
def  combination(n, k):
  k = min(k, n-k)
  result = 1
  for i in range(1, k+1):
    result *= n - i + 1
    result //= i
  return result
```
- permutation
```py
def permutation(n, k):
  result = 1
  for i in range(n - k + 1, n + 1):
    result *= i
  return result
```
- Breadth-first search
- Run time report
```py
import time
start_time = time.time()
runtime = time.time() - start_time
print(f"Runtime: {runtime} seconds")
```

#### Graph Algorithms:
Depth-First Search (DFS) and Breadth-First Search (BFS)  
Dijkstra's algorithm  
Floyd-Warshall algorithm  
Minimum Spanning Trees (Kruskal's and Prim's algorithms)  
Topological sorting  
Strongly Connected Components (Tarjan's and Kosaraju's algorithms)  
Max Flow algorithms (Ford-Fulkerson, Edmonds-Karp)  
Bellman-Ford algorithm  
#### Dynamic Programming:  
Knapsack problems  
Coin change problem  
Longest Common Subsequence (LCS)  
Dynamic Time Warping (DTW)  
Matrix Chain Multiplication  
Traveling Salesman Problem (using bit masking)  
Memoization  
Tiling
#### Data Structures:  
Binary Search Trees  
Segment Trees  
Fenwick Trees (Binary Indexed Trees)  
Hash Tables  
Disjoint Set Union (Union-Find)  
Heaps and Priority Queues  
Trie and Suffix Trees  
#### Number Theory:  
Modular arithmetic  
Greatest Common Divisor (GCD) and Extended Euclidean Algorithm  
Sieve of Eratosthenes for prime factorization  
Modular exponentiation  
Fermat's little theorem  
#### Geometry:  
Convex Hull (Graham's Scan, Jarvis March)  
Point-in-polygon algorithms  
Line intersection  
Closest pair of points  
#### String Algorithms:  
KMP string matching  
Rabin-Karp string matching  
Z algorithm  
Manacher's algorithm for longest palindromic substring  
#### Greedy Algorithms:  
Activity selection  
Fractional knapsack  
Huffman coding  
#### Divide and Conquer:  
Merge sort and variations  
Quick sort  
Fast Fourier Transform (FFT) for polynomial multiplication  
#### Search Techniques:  
Binary search  
Ternary search  
Meet in the middle  
#### Miscellaneous:  
Chinese Remainder Theorem  
Two-pointers technique  
Inclusion-Exclusion principle  
Pigeonhole principle  

```py
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

# Example
points = [(0, 0), (1, 0), (1, 1), (0, 1)]
print(polygon_centroid(points))  # Output: (0.5, 0.5)

```