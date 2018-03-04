def search_algo_brute_force(lista, element):
    for i, item in enumerate(lista):
        if item == element:
            return i, item
        else:
            continue

print search_algo_brute_force([2,3,4,5,6,6,7,7,8,88,20.90], 88)


print "***" * 50
def search_algo_binary1(list1, element):
    start = 0
    end = len(list1)-1
    found = False

    while start <= end and not found:
        midpoint = (start+end)//2
        if list1[midpoint] == element:
            found = True
        elif element < list1[midpoint]:
            end = midpoint-1
        else:
            start = midpoint+1
    return found

list_n = [x for x in range(100)]
print search_algo_binary1(list_n, 78)


def search_algo_binary_recursive(list1, elem):
    start_time = time.time()
    if len(list1) == 0:
        return False
    else:
        midpoint = len(list1)//2
        if list1[midpoint] == elem:
            return True
        else:
            if elem < list1[midpoint]:
                return search_algo_binary_recursive(list1[:midpoint], elem)
            else:
                return search_algo_binary_recursive(list1[midpoint+1:], elem)

