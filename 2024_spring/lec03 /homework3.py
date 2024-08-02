def cancellation(input_list, stop_word):


    output_list = []
    for item in input_list:
        if item == stop_word:
            return output_list
        output_list.append(item)
    return output_list

def copy_all_but_skip_word(input_list, skip_word):

    output_list = []
    for item in input_list:
        if item != skip_word:
            output_list.append(item)
    return output_list

def my_average(input_list):

    total_sum = sum(input_list)
    count = len(input_list)
    return total_sum / count
