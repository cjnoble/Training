

def bubble_sort (dataset):

    for i in range(len(dataset) - 1, 0, -1):

        for j in range(i):

            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        #print(dataset)


def merge_sort (dataset):

    if len(dataset) == 1:
        return dataset

    i = len(dataset)//2

    a = dataset[:i]
    b = dataset[i:]

    merge_sort(a)
    merge_sort(b)

    i = 0
    j = 0
    k = 0

    while True:

        if i == len(a):
            dataset[k:] = b[j:]
            break
        elif j == len(b):
            dataset[k:] = a[i:]
            break

        if a[i] > b[j]:
            dataset[k] = b[j]
            j += 1
        else:
            dataset[k] = a[i]
            i += 1

        k += 1
    return dataset

def quicksort (dataset, first=0, last=None):

    if last is None:
        last = len(dataset) - 1

    if first < last:

        pivot = first
        pval = dataset[pivot]

        i = 1
        j = last

        while True:

            while dataset[i] <= pval and i <= j:
                i += 1

            while dataset[j] >= pval and i <= j:
                j -= 1

            if i <= j:
            # Exchange upper and lower
                temp = dataset[j]
                dataset[j] = dataset[i]
                dataset[i] = temp
            else:
                break

        # Exchange pivot and upper value
        dataset[pivot] = dataset[j]
        dataset[j] = pval

        print(dataset)
    
        quicksort(dataset, first, j-1)
        quicksort(dataset, j+1, last)

    return dataset

list1 = [5, 3, 8, 2, 1, 34, 23, 3, 67, 32, 58, 28, 4236, 36, 19, 0]

#print(bubble_sort(list1))

#print(merge_sort(list1))

print(quicksort(list1))