from shapes import Shape, Square, Triangle

print("...................")
print("Shapes and Geometry")
print("...................")

choice = input("Enter choice, 1. Square, 2. Triangle: ")
if choice == "1":
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    square = Square(width, height)
    print(f"Square area = {square.area()}")
    print(f"Square perimeter = {square.perimeter()}")