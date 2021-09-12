def get_names(file):
	f=open(file,'r')
	data=f.read().replace('\n','')
	data=data.split('user: ')
	file_names=[]
	data.pop(0)
	for text in data:
		head, sep, tail = text.partition(',')
		file_names.append(head)
	return file_names

def del_duplicates(arr):
    n=len(arr)
    if(n==0 or n == 1):
        return arr
    pivot=0
    for last_o in range(0, n-1):
        if(arr[last_o]!=arr[last_o+1]):
            arr[pivot]=arr[last_o]
            pivot=pivot+1
    arr[pivot]=arr[n-1]
    return arr[0:pivot+1]

def fast_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array

names1=get_names('file1')
names2=get_names('file2')
names1=fast_sort(names1)
names2=fast_sort(names2)
names1=del_duplicates(names1)
names2=del_duplicates(names2)
for name2 in names2:
	for name1 in names1:
		if name1==name2:
			names1.remove(name1)
			break
print(names1)