def arithmetic_arranger(problems, show_answers=False):
    '''
        >>> arithmetic_arranger(["3801 - 2", "123 + 49"]) # doctest: +SKIP
        '  3801      123\\n-    2    +  49\\n------    -----'
        >>> arithmetic_arranger(["1 + 2", "1 - 9380"])
        '  1         1\\n+ 2    - 9380\\n---    ------'
        >>> arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        '    3      3801      45      123\\n+ 855    -    2    + 43    +  49\\n-----    ------    ----    -----'
        >>> arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        '  11      3801      1      123         1\\n+  4    - 2999    + 2    +  49    - 9380\\n----    ------    ---    -----    ------'
        >>> arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        'Error: Too many problems.'
        >>> arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        "Error: Operator must be '+' or '-'."
        >>> arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        'Error: Numbers cannot be more than four digits.'
        >>> arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        'Error: Numbers must only contain digits.'
        >>> arithmetic_arranger(["3 + 855", "988 + 40"], True)
        '    3      988\\n+ 855    +  40\\n-----    -----\\n  858     1028'
        >>> arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
        '   32         1      45      123      988\\n- 698    - 3801    + 43    +  49    +  40\\n-----    ------    ----    -----    -----\\n -666     -3800      88      172     1028'
        '''
    arr = None
    row = [''] * 4
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for p in problems:
        arr = p.split(' ')
        value_length = [len(str(arr[0])), len(str(arr[2])), 0]
        if arr[0].isdigit() == False or arr[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        elif arr[1] not in ['-', '+']:
            return "Error: Operator must be '+' or '-'."
        elif value_length[0] > 4 or value_length[1] > 4:
            return 'Error: Numbers cannot be more than four digits.'
        max_length = max(value_length)
        space_between_sing_and_value = 1
        space_between_packets = 0 if row[0] == '' else 4
        row[0] += ' ' * space_between_packets + ' ' * (
                    max_length - value_length[0] + space_between_sing_and_value + 1) + arr[0]
        row[1] += ' ' * space_between_packets + arr[1] + ' ' * (
                    max_length - value_length[1] + space_between_sing_and_value) + arr[2]
        row[2] += ' ' * space_between_packets + '-' * (max_length + space_between_sing_and_value + 1)
        solution = int(arr[0]) + int(arr[2]) * (-1 if arr[1] == '-' else 1)
        value_length[2] = len(str(solution))
        row[3] += ' ' * space_between_packets + ' ' * (
                    max_length - value_length[2] + space_between_sing_and_value + 1) + str(solution)

    row[3] = f'\n{row[3]}' if show_answers == True else ''
    return f'{row[0]}\n{row[1]}\n{row[2]}{row[3]}'


if __name__ == '__main__':
    import doctest

    #doctest.testmod()
    doctest.testfile('example.txt')

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["235 + 52"])}')
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "1 - 9380"], True)}')

# print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "1 - 9380"], True)}')
# print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "1 - 9380"], True)}')
# print(f'\n{arithmetic_arranger(["32 / 698", "3801 - 2", "45 + 43", "1 - 9380"], True)}')
# print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
# arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
