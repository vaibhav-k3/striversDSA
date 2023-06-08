def get_sum(ptr,arr):
    if ptr >= len(arr):
        return 0
    else:
        if arr[ptr] == -1:
            return 0
        sum = arr[ptr] + get_sum(2*(ptr)+1,arr) + get_sum(2*(ptr)+2,arr)
        return sum




def solution(arr):
    # Type your solution here 
    sum_left = 0
    left_ptr = 1
    right = 2
    sum_left = get_sum(1,arr)
    sum_right = get_sum(2,arr)
    if sum_left > sum_right:
        print("Left")
    else :
        print("Right")
    
    print(sum_left)



arr = [3,6,2,9,-1,10,20]
solution(arr)