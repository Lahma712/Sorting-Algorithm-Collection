import time
import random
import threading
def merge(List):
    def Merge(L, R, l, r, Sorted):  # L stands for left branch and R for right branch
        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                Sorted += [L[l]]
                l += 1
            else:
                Sorted += [R[r]]
                r += 1
        if l < len(L):
            Sorted += L[l:]
        else:
            Sorted += R[r:]
        return Sorted

    def split(List):  # main function that splits the list into left and right branches and then calls the merge function on them

        if len(List) == 1 or len(List) == 0:
            return List
        else:
            middle = len(List) // 2

            return Merge(split(List[:middle]), split(List[middle:]), 0, 0, [])

    SortedList = split(List)
    return SortedList


def select(List):
    for counter in range(len(List)):  # for loop creating smaller sublists
        Min = List[counter]  # minimum value
        for x in range(counter, len(List)):  # x is the position of the current value
            if List[x] <= Min:
                Min = List[x]
                p = x  # saving last x value in variable p
        List[p], List[counter] = List[counter], List[p]  # swaps the minimum value with the first value of the sublist
    return List


def insert(List):
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
    Liste = List
    def median(List, start, end, mid):
        if List[start] <= List[mid] <= List[end] or (List[end] <= List[mid] <= List[start]):
            return mid
        if List[start] <= List[end] <= List[mid] or (List[mid] <= List[end] <= List[start]):
            return end
        return start

    def partition(List, start, end):
        lesser = start+1
        pivot = median(List, start, end, (start+end+1) // 2)
        List[start], List[pivot] = List[pivot], List[start]
        while True:
            while lesser <= end and List[end] >= List[start]:
                end -= 1
            while lesser <= end and List[lesser] <= List[start]:
                lesser += 1
            if lesser <= end:
                List[lesser], List[end] = List[end], List[lesser]
            else:
                break
        List[start], List[end] = List[end], List[start]
        return end

    def quicksort(List, start, end):
        if start >= end:
            return List
        Prt = partition(List, start, end)
        quicksort(List, start, Prt - 1)
        quicksort(List, Prt + 1, end)

    quicksort(Liste, 0, len(Liste) - 1)
    return Liste


def radix(List):
    List = list(map(str, List))
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

def sleep(List):
    global sorted
    sorted = []
    global threads
    threads = []
    def Sleep(Value):
        time.sleep(Value/1000)
        sorted.append(Value)
        return 
    for value in List:
        t = threading.Thread(target= Sleep, args = [value])
        threads.append(t)

    for Thread in threads:
        try:
            Thread.start()
        except:
            continue
    
    return sorted


print("Commands:\n-Bubblesort -> bubble\n-Selectionsort -> select\n-Insertionsort -> insert\n-Mergesort -> merge\n-Quicksort -> quick\n-Radix LSD (base 10) -> radix\n-Bogosort -> bogo\n-Sleepsort -> sleep\n\n-New dataset -> new\n-Show initial dataset -> dataset\n-Show sorted dataset -> result\n-Show elapsed time-> time")


def Dataset():
    Input = input("\nGenerate dataset or enter your own?(1/2): ")
    if Input == "1":
        Input = input("Enter length of dataset: ")
        try:
            sizeBound = [int(i) for i in input("Enter boundaries ('min int'-'max int'): ").split("-")]
            listinput = ""
            for i in range(int(Input)):
                listinput += str(random.randint(sizeBound[0], sizeBound[1]))
                listinput += " "
            return listinput
        except(ValueError):
            print("\nInvalid dataset, please try again")
            return Dataset()
    elif Input == "2":
        listinput = input("Enter dataset: ")
        return listinput
    else:
        print("\nInvalid command,please try again")
        return Dataset()


listinput = Dataset()
while True:
    try:
        List = [int(i) for i in listinput.split()]
    except(ValueError):
        print("\nInvalid dataset, please try again")
        listinput = Dataset()
        continue
    
    Input = input("Command: ").lower()
    if Input in ["bubble", "select", "insert", "merge", "quick", "radix", "bogo", "sleep"]:
        try:
            start = time.time()
            Sorted = eval(Input + "(List)")
            end = time.time()
            print("Sorted!")
          
        except(RecursionError):
            print("\nMaximal recursion depth reached: Please decrease your dataset length or increase your boundaries.")
            listinput = Dataset()

    elif Input == "new":
        listinput = Dataset()
    elif Input == "time":
        try:
            print("Time: " + str(end-start))
        except:
            print("First sort your dataset using one of the sorting algorithm commands (f.ex quick, bubble, merge etc)")
    elif Input == "result":
        try:
            print(Sorted)
        except:
            print("First sort your dataset using one of the sorting algorithm commands (f.ex quick, bubble, merge etc)")
    elif Input == "dataset":
        print(List)
    
