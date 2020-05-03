


class SelectionSort:
    def sortValues(self, list1):

        for i in range(len(list1)):
            minpos = i
            for j in range(i, len(list1)):
                if list1[j] < list1[minpos]:
                    minpos = j

            temp = list1[i]
            list1[i] = list1[minpos]
            list1[minpos] = temp
            print("->",list1)
        return list1


list1 = [4, 9, 7, 3, 2, 5, 1]
sort1= SelectionSort()
result = sort1.sortValues(list1)
print(result)