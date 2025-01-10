def main():
    triangle_edge = float(input("Enter edge of triangle: "))
    triangle_height = float(input("Enter height of triangle: "))
    area = triangle_edge*triangle_height/2
    print("The area is","%.3f" %area)
main()