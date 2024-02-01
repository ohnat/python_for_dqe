# 1. create list of 100 random numbers from 0 to 1000
#import random
import random
#create a list
mylist = []
#add random numbers from 0 to 1000 untill it reach 100
for i in range(100):
    mylist.append(random.randint(0, 1000))
#print list results
print(mylist)

# 2. sort list from min to max (without using sort())
#define sorting program
def bubbleSort(mylist):
    # define n as number of elements in list
    n = len(mylist)
    #go thru all elements in array
    for i in range(n):
        for j in range(0, n - i - 1):
            #compare the elements one to one until they are sorted
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
#use sorting program for mylist
bubbleSort(mylist)
#print sorted result
print("My sorted list: ", mylist)

# 3.calculate average for even and odd numbers
# print both average result in console 
# def separate lists for odd and even numbers
evenList = []
oddList = []

# iterate thru each number in mylist
for i in mylist:
    # checking condition
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
# print even and odd lists
print("Even list: ", evenList)
print("Odd list: ", oddList)

# program to get average of a list
def average(mylist):
    return sum(mylist) / len(mylist)
#count average for even and odd lists
avgEvenList = average(evenList)
avgOddList = average(oddList)
# print avg for even and odd lists
print("Average for even list: ", round(avgEvenList))
print("Average for odd list: ", round(avgOddList))

