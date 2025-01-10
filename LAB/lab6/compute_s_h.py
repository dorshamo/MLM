# use the following strings:
# "Enter v(0-100) m/s and a (0-90 degrees):"
# "Time: %.1f.....S=%5.2f H=%5.2f" ......"
# "Fallen!"
# "Finish"
import math 
 
"""Calculate height of projectile at time t."""
def height (v, a, t):
    # put your code here
    vy = v*math.sin(a)
    h = (vy*t)-((9.81*(t**2))/2)
    return h
    

    
"""Calculate horizontal distance traveled at time t."""
def horizontal(v,a,t):
    # put your code here
    vx = v*math.cos(a)
    s = vx*t
    return s

   
"""Convert angle from degrees to radians."""
def deg2rad(a):
    # put your code here
    a = a/180*math.pi
    return a
    

"""creating a main function"""
def main():
    # put your code here
    v = 0
    a = 0
#while loop to stop the the loopwhen the input is -1.
    while v != -1 and a != -1:
        v,a = eval(input("Enter v(0-100) m/s and a (0-90 degrees):\n"))
#if statement to print finish when 1 of the inputs is over the limits
        if v >= 100 or  v <= 0 or a <= 0 or a >= 90 or (v==-1 and a ==-1):
            print("Finish")
            a = -1
            v = -1
        else:
            t = 0.1
            a = deg2rad(a)
            h = height(v, a, t)
            s = horizontal(v, a, t)
#inner loop that gives the functions new  paramerers and print the calculations every 0.1 seconds
            while h >= 0:
                 print("Time: %.1f....S=%.2f H=%.2f"%(t, s, h),sep='')
                 t = t + 0.1
                 h = height(v, a, t)
                 s = horizontal(v, a, t)
#when hight under zero print the last calculation and stops the loop
            if h < 0:
                print("Time: %.1f....S=%5.2f H=%5.2f"%(t, s, h),sep='')
            print("Fallen!")
        
   
main()    





