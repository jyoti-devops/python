"""
use the co-ordinates and check for
the container with most water
"""


def container_with_most_water(input_cor):
    """
    container_with_most_water
    """
    height = 0
    length = len(input_cor) - 1
    area = 0

    while height < length:
        new_area = min(input_cor[height], input_cor[length]) * (length-1)
        print(new_area)
        if new_area > area:
            area = new_area
        if input_cor[height] > input_cor[length]:
            length -= length
        else:
            height += 1

    print(max(input_cor))
    print(area)


if __name__ == "__main__":
    container_with_most_water([1, 1, 1, 1, 1])
    container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
