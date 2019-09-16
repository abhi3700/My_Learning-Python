"""
    This computes the `key` corresponding to a `value` in a dictionary.
    Case-1: Simple dictionary
    Case-2: Nested dictionary
"""
# #################################################################################################################################
# Case-1: Simple dictionary
dict_simple = {'george' : 16, 'amber' : 19}
key_simple = ""
try:
    key_simple = list(dict_simple.keys())[list(dict_simple.values()).index(19)]
except ValueError:      # ignore this exception error when item not found
    pass
print(key_simple)


# ==================================================================================================================================
# Case-2: Nested dictionary
dict_nested = {
        "phone_no1": {
            "username": "abhi3701",
            "country": "India",
            "last_product":"A",
            "last_key_a": "Alltest343247328507230",
            "last_key_b": "Alltest343247328507230",
            "last_key_c": "Alltest34324652374554657",
            "last_key_d": "Alltest347878423542356878",
            "last_key_d": "Alltest3478784235443423",
            "datetime": "2019-09-29",
            }
        }

dict_nested_val1 = dict_nested['phone_no1']     # get the value of key - "phone_no1"
print(dict_nested_val1.get("username"))            # get the value of key - "username" in the second root.
key_nested = ""
try:
    key_nested = list(dict_nested_val1.keys())[list(dict_nested_val1.values()).index('India')]       # get the key corresponding to value - 'India'
except ValueError:      # ignore this exception error when item not found
    pass
print(key_nested)

# ==================================================================================================================================
# Case-3: Nested (2 times) dictionary
dict_nested2 = {
        "phone_no1": {
            "product_a": {
                "username": "abhi3701",
                "country": "India",
                "key": "Alltest2438542342374",
                "datetime": "2019-09-29",
                }
            }
        }

print(dict_nested2['phone_no1']['product_a']['key'])
dict_nested2_val2 = dict_nested2['phone_no1']['product_a']
key_nested2 = ""
try:
    key_nested2 = list(dict_nested2_val2.keys())[list(dict_nested2_val2.values()).index('India')]       # get the key corresponding to value - 'India'
except ValueError:      # ignore this exception error when item not found
    pass
print(key_nested2)
