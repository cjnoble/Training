alist = [i for i in range(1, 50, 3)]


def find_max(data):

    if len(data) == 1:
        return data[0]

    else:
        compare = find_max(data[1:])

        if data[0] > compare:
            return data[0]
        else:
            return compare


print(find_max(alist))