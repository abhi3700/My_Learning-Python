"""
"description": to set the nested dictionary and get the value of item
"""

import json

"""
# Dictionary (Nested)
"stats": {
    "correct": {
        "count": 2
    }
}
"""
item_dict = dict(stats= dict(correct= dict(count=0)))
print(item_dict)    # {'stats': {'correct': {'count': 0}}}
print(item_dict.get('stats'))   # {'correct': {'count': 0}}
print(item_dict['stats']['correct']['count'])   # 0