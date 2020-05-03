

list1 = [1,9,3,7,2,5,4]
giveValue= 7
index = 0

class SearchValue:

    def search(self, list1, giveValue):
        for i in range(0,len(list1)):
            if list1[i]==giveValue:
                globals()['index'] = i
                return True
        return False

search1=SearchValue()
if search1.search(list1, giveValue):
    print ("Value found at- {}".format(index+1))
else:
    print("value not found")





