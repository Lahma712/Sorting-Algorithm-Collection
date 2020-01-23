import time
import random

def MergeSort(List):
    print("\nMergeSort:")
    start = time.time()

    def merge(L, R):  # L stands for left branch and R for right branch
        Sorted = []
        while True:
            if len(L) == 0:
                Sorted += R
                break
            if len(R) == 0:
                Sorted += L
                break
            elif L[0] <= R[0]:
                Sorted.append(L[0])
                L.remove(L[0])
            else:
                Sorted.append(R[0])
                R.remove(R[0])
        return Sorted

    def split(List):  # main function that splits the list into left and right branches and then calls the merge function on them

        if len(List) == 1 or len(List) == 0:
            return List
        else:
            middle = len(List) // 2
            L = split(List[:middle])
            R = split(List[middle:])

            return merge(L, R)

    SortedList = split(List)
    end = time.time()
    print("elapsed time: " + str(end - start) + " seconds")
    return SortedList



def SelectionSort(List):
    print("\nSelectionSort: ")
    start = time.time()

    for counter in range(len(List)):  # for loop creating smaller sublists
        Min = List[counter]  # minimum value
        for x in range(counter, len(List)):  # x is the position of the current value
            if List[x] <= Min:
                Min = List[x]
                p = x  # saving last x value in variable p
        List[p], List[counter] = List[counter], List[p]  # swaps the minimum value with the first value of the sublist
    end = time.time()
    print("elapsed time: " + str(end - start) + " seconds")
    return List


def InsertionSort(List):
    print("\nInsertionSort:")
    start = time.time()

    def switch(x):  # x is the position of the current value
        List[x], List[x + 1] = List[x + 1], List[x]  # swaps two values (value followed by smaller value)
        if List[x] < List[x - 1] and x != 0:  # follows the switched value to their final position via iteration (not recursion -> will reach max depth)
            for i in range(x,-1,-1):
                if List[i] > List[i-1]:
                    break
                if List[i] < List[i - 1] and i != 0:
                    List[i], List[i -1] = List[i - 1], List[i]

    for x in range(len(List) - 1):
        if List[x] > List[x + 1]:
            switch(x)
    end = time.time()
    print("elapsed time: " + str(end - start) + " seconds")
    return List


def BogoSort(List):
	print("\nBogoSort:")
	start = time.time()
	def check(List):
		for x in range(len(List)-1):
			if List[x] > List[x+1]:
				return False
		return True
	def bogo(List):
		while not check(List):
			List= random.sample(List, len(List))
		return List
	SortedList = bogo(List)
	end = time.time()
	print("elapsed time: " + str(end - start) + " seconds")
	return SortedList


def BubbleSort(List):
    print("\nBubbleSort: ")
    start = time.time()

    def switch(x):
        List[x], List[x + 1] = List[x + 1], List[x]  # swaps two values (value followed by smaller value)
        y = 0

    while True:
        c = 0
        for y in range(len(List) - 1):
            if List[y] > List[y + 1]:
                switch(y)
                c = 1
        if c == 0:
            end = time.time()
            print("elapsed time: " + str(end - start) + " seconds")
            return List
            
def QuickSort(List):
	print("\nQuickSort: ")
	start = time.time()
	def quicksort(List):
		if len(List) == 1 or len(List) == 0:
			return List
		R = []
		L = []
		pivot = List[len(List)-1] #taking the last item of the list as a pivot
		plist = [pivot]
		for i in range(len(List)-1):
			if List[i] >= pivot:
				R.append(List[i])
			else:
				L.append(List[i])
		SortedList = quicksort(L)+plist+quicksort(R)
		return SortedList
	SortedList = quicksort(List)
	end = time.time()
	print("elapsed time: "  + str(end - start) + " seconds")
	return SortedList

listinput = input("\nEnter a dataset: ")
while True:
    List = [int(i) for i in listinput.split()]
    Input = input("What Algorithm?: ").lower()
    if Input in ["merge", "mergesort"]:
        print(MergeSort(List))
    if Input in ["select", "selectionsort"]:
        print(SelectionSort(List))
    if Input in ["insert", "insertionsort"]:
        print(InsertionSort(List))
    if Input in ["bogo", "bogosort"]:
        print(BogoSort(List))
    if Input in ["bubble", "bubblesort"]:
        print(BubbleSort(List))
    if Input in ["quick", "quicksort"]:
    	print(QuickSort(List))
    if Input == "ninput":
    	listinput = input("\nEnter a dataset:")
    if Input == "exit":
        quit()
