calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    for i in range(0, len(list_to_search)):
        str_is_list = False
        if string.upper() in list_to_search[i].upper():
            str_is_list = True
        else:
            if str_is_list == True:
                continue
            else:
                str_is_list = False
    return str_is_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
