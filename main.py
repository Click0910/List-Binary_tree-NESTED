# # Given a data structure, print all titles

def print_titles(list_food):
    for food in list_food:
        print(food['title'])
        if "subcategories" in food:
            print_titles(food['subcategories'])


categories = [
    {
        "title": "Food",
        "subcategories": [
            {"title": "Bread"},
            {
                "title": "Meat",
                "subcategories": [
                    {"title": "Pork",
                     "subcategories": [
                         {"title": "White Pork"},
                         {"title": "Red Pork"}
                     ]
                     },
                    {"title": "Beef"},
                ],
            },
            {"title": "Cheese"},
        ],
    },
    {"title": "Drinks"},
]

print_titles(categories)
