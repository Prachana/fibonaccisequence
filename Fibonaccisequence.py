#sequence =  0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fs(number_of_sequence):
    if number_of_sequence <= 1:
        return 0
    elif number_of_sequence == 2:
        return 1
    else:
        return fs(number_of_sequence - 1) + fs(number_of_sequence - 2)


print(fs(5))