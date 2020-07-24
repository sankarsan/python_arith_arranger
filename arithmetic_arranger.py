def arithmetic_arranger(problems):
    ret_val = validate_input(problems)
    valid_operators = ["+", "-"]
    interim_list_top = []
    interim_list_bottom = []
    for elem in problems:
        flag = False
        for op in valid_operators:
            if elem.find(op) > -1:
                flag = True
                ret_val = process_input_element(op, elem)
                break
        if not flag:
            ret_val = "Error: Operator must be '+' or '-'."
            break
        elif len(ret_val) == 1:
            ret_val = ret_val[0]
            break
        interim_list_top.append(ret_val[0])
        interim_list_bottom.append(ret_val[1])

    ret_val = format_output(interim_list_bottom, interim_list_top)
    return ret_val


def format_output(interim_list_bottom, interim_list_top):
    ret_val = ""
    top_line = ""
    bottom_line = ""
    footer_line = ""
    for i in range(len(interim_list_top)):
        top_line += interim_list_top[i]
        bottom_line += interim_list_bottom[i]
        footer_line += "-----"
        if i < len(interim_list_top):
            top_line += "   "
            bottom_line += "   "
            footer_line += "   "
    ret_val = top_line + "\n" + bottom_line + "\n" + footer_line
    return ret_val


def process_input_element(operator, elem):
    temp = elem.split(operator)
    x = temp[0].strip()
    y = temp[1].strip()

    if len(x) > 4 or len(y) > 4:
        ret_val = ["Error: Numbers cannot be more than four digits."]
    elif x.isnumeric() and y.isnumeric():
        ret_val = [x.rjust(5), operator + y.rjust(4)]
    else:
        ret_val = ["Error: Numbers must only contain digits."]

    return ret_val


def validate_input(problems):
    ret_val = ""
    if len(problems) == 0:
        ret_val = "Error: No problem provided."
    elif len(problems) > 5:
        ret_val = "Error: Too many problems."
    return ret_val
