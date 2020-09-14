def container_with_most_water(input_cor):
    h = 0
    l = len(input_cor) - 1
    print(f'length - {l}')
    area = 0

    while h < l:
        new_area = min (input_cor[h], input_cor[l]) * (l-1)
        print(new_area)
        if new_area > area:
            area = new_area
        if input_cor[h] > input_cor[l]:
            l = l -1
        else:
            h = h +1

    print(max(input_cor))
    print(area)


if __name__ == "__main__":
    container_with_most_water([1,1,1,1,1])
    container_with_most_water([1,8,6,2,5,4,8,3,7])
    pass