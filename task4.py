# task 4 Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n . The second line contains an array A[]   of  n  integers each separated by a space.

# -----------------------------------------------code----------------------------------------------



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
list1 = list(arr)
list1.sort()
set1 = set(list1)
list2 = list(set1)     #3rd and final solution is to remove duplicates bhaishab maja aagai 
list2.sort()
print(list2[-2])
