'''Given a list of N numbers, write a function to shift the numbers circularly by some integer k 
(where k < N). The function should take a list and k as arguments and return the shifted list.
1. Write a function that assumes shifting is to the left.
2. Write a function that takes a third argument that specifies shifting left or right.
Hint:
original list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shifted by 4, to the left: [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
shifted by 4, to the right: [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]'''

def shift_left(mylist, k):
    """
    Shifts the list to the left by k positions.

    Args:
    mylist (list): The input list of integers.
    k (int): Number of positions to shift.

    Returns:
    list: The shifted list.
    """
    n = len(mylist)
    k = k % n  # Handle cases where k >= n
    return mylist[k:] + mylist[:k]

def shift_list(mylist, k, direction):
    """
    Shifts the list to the left or right by k positions.

    Args:
    mylist (list): The input list of integers.
    k (int): Number of positions to shift.
    direction (str): Direction of the shift ('left' or 'right').

    Returns:
    list: The shifted list.
    """
    n = len(mylist)
    k = k % n  # Handle cases where k >= n
    if direction.lower() == "left":
        return mylist[k:] + mylist[:k]
    elif direction.lower() == "right":
        return mylist[-k:] + mylist[:-k]
    else:
        raise ValueError("Invalid direction! Use 'left' or 'right'.")

mylist = list(map(int, input("Enter the elements of the list: ").split()))
k = int(input("Enter the number of positions to shift: "))
shifted = shift_left(mylist, k)
print("Shifted list (left):", shifted)

direction = input("Enter the direction to shift (left or right): ").strip()
shifted = shift_list(mylist, k, direction)
print(f"Shifted list ({direction}):", shifted)
