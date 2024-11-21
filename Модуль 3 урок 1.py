calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_ = len(string)
    upper_ = string.upper()
    lower_ = string.lower()
    return (len_, upper_, lower_)


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [i.upper() for i in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
