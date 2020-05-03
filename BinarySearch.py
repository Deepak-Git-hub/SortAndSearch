

list1 = [1,9,3,7,2,5,4]
giveValue = 7
index = 0


class BinarySearch:
    def search(self, list1, searchValue):
        lower = 0
        upper = len(list1)-1
        while lower <= upper:
            mid = (lower + upper) // 2
            if list1[mid] == searchValue:
                globals()['index'] = mid
                return True
            else:
                if list1[mid] < searchValue:
                    lower = mid+1
                else:
                    upper = mid-1
        return False




search1 = BinarySearch()
print(list1)
list1 = sorted(list1)
print(list1)
if search1.search(list1, giveValue):
    print ("Value found at {}".format(index+1))
else:
    print("Value not found")