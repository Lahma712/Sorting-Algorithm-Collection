
import time
import random
List = [int(i) for i in input("Please enter a dataset: ").split()]

def MergeSort(List):
	print("\nMergeSort:")
	start = time.time()
	
	def merge(L,R): #L stands for left branch and R for right branch
		Sorted =[]
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
	
	def split(List): #main function that splits the list into left and right branches and then calls the merge function on them
		start = time.time()
		if len(List) ==1 or len(List)==0:
			return List
		else:
			middle = len(List)//2
			L = split(List[:middle])
			R = split(List[middle:])
			return merge(L, R)
	end = time.time()
	print("elapsed time: " + str(end-start) + " seconds")
	return split(List)


def SelectionSort(List):
	print("\nSelectionSort: ")
	start = time.time()
	
	for counter in range(len(List)): #for loop creating smaller sublists
		Min = List[counter] #minimum value
		for x in range(counter, len(List)): #x is the position of the current value
			if List[x] <= Min:
				Min = List[x]
				p = x #saving last x value in variable p
		List[p], List[counter]   = List[counter], List[p] #swaps the minimum value with the first value of the sublist
	end = time.time()
	print("elapsed time: " + str(end-start) + " seconds")	
	return List
	
def InsertionSort(List):
	print("\nInsertionSort:")
	start = time.time()
	def switch(x): #x is the position of the current value
		List[x], List[x+1] = List[x+1], List[x] #swaps two values (value followed by smaller value)
		if List[x] < List[x-1] and x != 0: #follows the switched value to their final position via recursion
			switch(x-1)
	for x in range(len(List)-1):
		if List[x] > List[x+1]:
			switch(x)
	end = time.time()
	print("elapsed time: " + str(end-start) + " seconds")
	return List


def BogoSort(List):
	print("\nBogoSort:")
	start = time.time()
	while True:
		x =0
		j = 0
		while x < len(List)-1:
			if List[x] > List[x+1]:
				j +=1
				List = random.sample(List, len(List))
				break
			x +=1
		if j==0:
			end = time.time()
			print("elapsed time: " + str(end-start) + " seconds")
			return List


def BubbleSort(List):
	print("\nBubbleSort: ")
	start = time.time()
	def switch(x):
		List[x], List[x+1] = List[x+1], List[x] #swaps two values (value followed by smaller value)
		y =0

	while True:
		c =0
		for y in range(len(List)-1):
			if List[y] > List[y+1]:
				switch(y)
				c = 1
		if c == 0:
			end = time.time()
			print("elapsed time: " + str(end-start) + " seconds")
			return List
			


while True:
	Input = input("\nWhat Algorithm?: ")
	if Input in ["Merge", "merge", "mergesort"]:
		print(MergeSort(List))
	if Input in ["Select", "select", "selectionsort"]:
		print(SelectionSort(List))
	if Input in ["Insert", "insert", "insertionsort"]:
		print(InsertionSort(List))
	if Input in ["Bogo", "bogo", "bogosort"]:
		print(BogoSort(List))
	if Input in ["Bubble", "bubble", "bubblesort"]:
		print(BubbleSort(List))
	if Input == "All":
		print(SelectionSort(List))
		print(MergeSort(List))
		print(InsertionSort(List))
		print(BogoSort(List))
		print(BubbleSort(List))
	if Input == "exit":
		quit()
	if Input == "ninput":
		List = [int(i) for i in input("New dataset: ").split()]

