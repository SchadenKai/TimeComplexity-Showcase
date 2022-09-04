from os import system, name
from time import sleep 
 
# Side Functions
def assign_long_list(arr):                     
    for i in range(8**8):
        arr.append(i) 
def clear():
    system('cls')
def main_menu(choice, arr):
    target = int(input('Enter target number: '))
    if choice == '0':
        targ_index = int(input('Enter the index of where to search: '))
        return search_zero(arr, targ_index, target)
    elif choice == '1':
        return search_first(arr, target) 
    elif choice == '1.2':
        return search_first2D(arr, target)  
    elif choice == '2':
        return search_second(arr, target)
    else:
        return -2
def choice_list(choice):
    if choice == 1:
        return short_list
    elif choice == 2:
        return long_list
    elif choice == 3:
        return arr_2D

#   Main Functions 
#   Big O(1)
##  Constant time 
##  Standard Search algo - User takes guess of the index position of the 
##  user's target value 
def search_zero(arr, index, target):                                                    
    if target == arr[index]:
        return index
    else:
        return -1
#   Big O(n)
##  Linear search algorithm
def search_first(arr, target):                                                            
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1
#   Big O(n**2)
##  Linear search algorithm in terms of 2D Arrays(List)
##  Raising the size of the array doubles the time it takes
def search_first2D(arr, target):                                                            
    for outer_elem in range(len(arr)-1):
        for inner_elem in range(len(arr[0])-1):
            if target == arr[outer_elem][inner_elem]:
                return [outer_elem, inner_elem]
    return -1
#   Big O(log n)
##  Binary Search Algorithm
def search_second(arr, target):                                            
    lowptr = 0
    highptr = len(arr) - 1
    mid = 0
    while lowptr <= highptr:
        mid = (highptr + lowptr) // 2
        if target == arr[mid]:
            print('index =', mid)
            return mid
        elif target < arr[mid]:
            highptr = mid - 1
        else:
            lowptr = mid + 1
    return -1
    
#   Variables and Lists [Short, Long and 2D Lists]
short_list = [1,2,3,4,5,6,7,8,9]
long_list = []
assign_long_list(long_list)
arr_2D = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ]
tic = 0
toc = 0
result = 0

#   Main menu | Program loop
while True:
    clear()
    print(' Search zero [0]          Search first [1]\n',
        'Search first 2D [1.2]    Search second [2]')
    ui_choice = input('Select desired search: ')
    print('Enter what array to input \n',
        'Short list [1]     Long list [2]    2D list [3]'
        )
    ui_list = int(input('Enter desired list type: '))
    pass_list = choice_list(ui_list)
    result = main_menu(ui_choice, pass_list)

    #   Print Results + Error Handling
    if result == -2:
        print('[ERROR] Input in range of choices')
    elif result == -1:
        print('[NOT FOUND!]')
    else:
        print('[FOUND!]')
        print('Index value = ', result)
    
    #   Controls statement - End while loop (User input)
    end_statement = input('Do you want to exit?? [Y/N]')
    if end_statement == 'Y':
        print('Thank you for using the program! Goodbye....')
        print('Goes of for 5 secs...')
        sleep(5)
        clear()
        break
    else:
        continue