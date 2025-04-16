a, b, c = map(int, input().split())

if a <= 0 or b <= 0 or c <= 0:
    print("No Negative Edges")
else:
    sides = sorted([a, b, c])
    
    if sides[0] + sides[1] <= sides[2]:
        print("No Possible Triangles")
    else:
        if a == b == c:
            print("your edges type: Equilateral")
        elif a == b or b == c or a == c:
            print("your edges type: Isosceles")
        else:
            print("your edges type: Scalene")

        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print("your angles type: Right")
        elif sides[0]**2 + sides[1]**2 > sides[2]**2:
            print("your angles type: Acute")
        else:
            print("your angles type: Obtuse")
