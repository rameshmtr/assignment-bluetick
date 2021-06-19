#1. Write a function to implement binary search which will take a sorted list and a number. 
#   It returns the index where number is present in the list else nil
    
def binarySearch(sorted_list, number):  
    low = 0  
    high = len(sorted_list) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2  
  
        if sorted_list[mid] < number:  
            low = mid + 1  
  
        elif sorted_list[mid] > number:  
            high = mid - 1  
  
        else:  
            return mid  
  
    return -1  


sorted_list = [12, 24, 32, 39, 45, 50, 54]  
number = 12  
  
result = binarySearch(sorted_list, number)  
  
if result != -1:  
    print(result)  
else:  
    print("nil") 