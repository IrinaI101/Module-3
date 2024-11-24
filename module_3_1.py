calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    list_to_search_lower = [i.lower() for i in list_to_search]
    if string.lower() in list_to_search_lower:
        result = True
    else:
        result = False
    return result

print(string_info("StRawBeRry"))
print(string_info("Christmas Is Coming"))
print(is_contains("cat", ["Catalogue", "cad", "CAt"]))
print(is_contains("STar", ["STarted", "str", "Storm" ]))
print(calls)
