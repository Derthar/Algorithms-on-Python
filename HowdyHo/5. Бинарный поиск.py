lst = [25, 38, 47, 69, 48, -2, -4, -3, -70, 1, 7]
lst.sort()
what = 69
print(lst)
plus_index = 0
while True:
    find_list = lst
    half = round(len(find_list) // 2)
    mid_elem = find_list[half]
    if what == mid_elem:
        print(f'We find it. His index is {half+plus_index}')
        break
    elif what > mid_elem:
        lst = find_list[half:]
        plus_index += half
    elif what < mid_elem:
        lst = find_list[0:half]