# Linear Search - Python3

# Procedure linear_search is used to search an element sequentially.
# Worst-case complexity O(n)
def linear_search(list, search_element):
    for i in range(0, len(list)):
        if (search_element == list[i]):
            print("Element found at position: ", (i+1))

#Test with hardcoded data.
x = []
n = int(input("Enter the size of the list: "))
for i  in range(0, n):
    y = int(input(f"Enter the {i}th element of the list: "))
    x.add(y)
linear_search(x, 2)
