# basic loop example
my_list = [1, 5, "Hello", 2.7]
for x in my_list:
    print(x)

list1 = range(10, 30, 3)
print("length of list1: %d" % len(list1))


# type comparision
for x in my_list:
    if(isinstance(x, int)):
        print(x)


int_List = [1, 2, 3, 4, 1, 3, 3, 4, 5, 5, 7, 7, 8]
int_to_search = input("Please enter ")
