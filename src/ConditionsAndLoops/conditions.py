x = -1
if(x < 5):
    print("Less than 5")
elif (x < 10):
    print("Greater than 5 but less than 10")
else:
    print("Greater than 10")


# find max value
x, y, z = 10, 15, 12
if ((x > y) and (x > z)):
    print("Maximum value: %d" % x)
elif(y > z):
    print("Maximum value: %d" % y)
else:
    print("Maximum value: %d" % z)
