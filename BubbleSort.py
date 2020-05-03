


class BubbleSort:
    def sortValues(self, list1):
        temp = 0
        for i in range(0,len(list1),1):
            for j in range(i+1, len(list1),1):
                if list1[i] > list1[j]:
                    temp = list1[j]
                    list1[j]=list1[i]
                    list1[i]=temp
            print("->",list1)
        return list1


list1 = [1, 9, 3, 7, 2, 5, 4]
sort1= BubbleSort()
result = sort1.sortValues(list1)
print(result)