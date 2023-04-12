

def together(l1, l2):
    c = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if lst1[i] >= lst2[j]:
            c.append(lst2[j])
            j +=1
        else:
            c.append(lst1[i])
            i += 1
    c += lst1[i:] + lst2[j:]
    return c



lst1 = [1,3,4,5,6,7,8,9,10, 12, 14,20,21]
lst2 = [-1,3,4,7,10,12,13, 14, 15,16,17]


if __name__ == '__main__':
    print(lst1)
    print(lst2)
    print(together(lst1, lst2))
