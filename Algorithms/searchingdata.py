

def is_sorted (data):

    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

if __name__ == "__main__":

    alist = [i for i in range(1, 50, 3)]
    alist[5] = 1000
    print(is_sorted(alist))