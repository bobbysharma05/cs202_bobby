'''Given a list of N numbers, write a function to shift the numbers circularly by some integer k 
(where k < N). The function should take a list and k as arguments and return the shifted list.
1. Write a function that assumes shifting is to the left.
2. Write a function that takes a third argument that specifies shifting left or right.
Hint:
original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shifted by 4, to the left: [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
shifted by 4, to the right: [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]'''

#part1 
def Shifted_list(k):
    for i in range(0,len(mylist)):
        shlist.append(mylist[i-k])
    return shlist

mylist = list(map(int, input("Enter the elements of list = ").split()))
shlist = []
print(mylist)
print(Shifted_list(len(mylist)-1))

#part2
def Shifted_list(k):
    if sh.lower() == "left":
        for i in range(0,len(mylist)):
            shlist.append(mylist[i-k])
        return shlist
    elif sh.lower()=="right":
        for i in range(0,len(mylist)):
            shlist.append(mylist[k-i])
        return shlist


mylist = list(map(int, input("Enter the elements of list = ").split()))
j = int(input("Write the shifting number = "))
sh = str(input("Shifting will be left or right = "))
shlist = []
print(mylist)
print(Shifted_list(len(mylist)-1))