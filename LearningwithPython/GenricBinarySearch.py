'''
lo:lower index of array
hi:end index of arrray
array:sorted list of unique numbers 
condition:function return  strings indicating  whether the query is 'found', or can be found at 'left' side or 'right' side
'''


def binary_search(array,query):
    def condition(mid):
        if array[mid] == query:
               return 'found'
        elif array[mid] < query:
            return 'left'
        else:
            return 'right'
          
    lo=0
    hi=len(array)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
