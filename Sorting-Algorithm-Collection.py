import time
import random


def merge(List):
    print("\nMergeSort:")
    def Merge(L, R):  # L stands for left branch and R for right branch
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

    def split(
            List):  # main function that splits the list into left and right branches and then calls the merge function on them

        if len(List) == 1 or len(List) == 0:
            return List
        else:
            middle = len(List) // 2
           
            L = split(List[:middle])
            R = split(List[middle:])

            return Merge(L, R)

    SortedList = split(List)
    return SortedList


def select(List):
    print("\nSelectionSort: ")
    for counter in range(len(List)):  # for loop creating smaller sublists
        Min = List[counter]  # minimum value
        for x in range(counter, len(List)):  # x is the position of the current value
            if List[x] <= Min:
                Min = List[x]
                p = x  # saving last x value in variable p
        List[p], List[counter] = List[counter], List[p]  # swaps the minimum value with the first value of the sublist
    return List


def insert(List):
    print("\nInsertionSort:")
    def switch(x):  # x is the position of the current value
        List[x], List[x + 1] = List[x + 1], List[x]  # swaps two values (value followed by smaller value)
        if List[x] < List[
            x - 1] and x != 0:  # follows the switched value to their final position via iteration (not recursion -> will reach max depth)
            for i in range(x, -1, -1):
                if List[i] > List[i - 1]:
                    break
                if List[i] < List[i - 1] and i != 0:
                    List[i], List[i - 1] = List[i - 1], List[i]

    for x in range(len(List) - 1):
        if List[x] > List[x + 1]:
            switch(x)
   
    return List


def bogo(List):
    print("\nBogoSort:")
    

    def check(List):
        for x in range(len(List) - 1):
            if List[x] > List[x + 1]:
                return False
        return True

    def Bogo(List):
        while not check(List):
            List = random.sample(List, len(List))
        return List

    SortedList = Bogo(List)
    return SortedList


def bubble(List):
    print("\nBubbleSort: ")

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
            return List


def quick(List):
    print("\nQuickSort: ")
    
    
    def quicksort(List):
        if len(List) == 1 or len(List) == 0:
            return List
        R = []
        L = []
        pivot = List[random.randint(0,len(List)-1)] # taking a random item of the list as a pivot
        
        for i in range(len(List) - 1):
            if List[i] >= pivot:
                R.append(List[i])
            else:
                L.append(List[i])
        
        SortedList = quicksort(L)+ [pivot] + quicksort(R)
        return SortedList
   
    
    SortedList = quicksort(List)
    return SortedList
    
    

def radix(List):
    print("\nRadix LSD (base 10): ")
    List  = list(map(str, List))
    buckets = {}
    for x in range(10):
        bucket = {x: []}
        buckets.update(bucket)

    Max = int(List[0])
    for x in range(len(List)):
        if int(List[x]) > int(Max):
            Max = List[x]

    for x in range(len(List)):
        List[x] = ("0" * (len(str(Max)) - len(List[x])) + List[x])
    for z in range(len(str(Max)))[::-1]:

        for j in range(len(List)):
            buckets[eval(str(List[j])[z])].append(List[j])
        List = []
        for y in range(10):
            List += buckets[y]
            buckets[y] = []
    return list(map(int, List))


print("Commands:\n-Bubblesort -> bubble\n-Selectionsort -> select\n-Insertionsort -> insert\n-Mergesort -> merge\n-Quicksort -> quick\n-Radix LSD (base 10) -> radix\n-Bogosort -> bogo\n\n-New dataset -> ninput")

def Dataset():
    Input = input("\nGenerate dataset or enter your own?(1/2): ")
    if Input == "1":
        Input =input("Enter length of dataset: ")
        sizeBound = [int(i) for i in input("Enter boundaries ('min int'-'max int'): ").split("-")]
        listinput = ""
        for i in range(int(Input)):
            listinput += str(random.randint(sizeBound[0], sizeBound[1]))
            listinput += " "
        print("Generated dataset: " + listinput)
    elif Input == "2":
        listinput = input("Enter your dataset: ")
    else:
    	print("invalid command")
    	Dataset()
    return listinput

listinput = Dataset()
while True:
    List = [int(i) for i in listinput.split()]
    Input = input("What Algorithm?: ").lower()
    if Input in ["bubble", "select", "insert", "merge", "quick", "radix", "bogo"]:
      try:
          start = time.time()
          Sorted = eval(Input + "(List)")
          end = time.time()
          print(Sorted)
          print("\nElapsed time: " + str(end - start) + " seconds")
      except(RecursionError):
          print("\nMaximal recursion depth reached: Please decrease your dataset length or increase your boundaries. ")
          listinput = Dataset()
          
    if Input == "ninput":
        listinput = Dataset()
    else:
    	continue
