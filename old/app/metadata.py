''' Metadata

Contains metadata details. Typically for developers and not production users.
Descriptions are reflected on the generated Doc page

'''

# The tags for the FastAPI OpenAPI auto documenter
tags_metadata = [
    {
        "name": "Owners",
        "description": "Operations with Pets Owner",
    },
    {
        "name": "Pets",
        "description": "Operations with Pets",
    },
    {
        "name": "Trainers",
        "description": "Operations with Pet Trainer",
    },
    {
        "name": "Nutrition Plans",
        "description": "Operations with Nutrition Plan",
    },
    {
        "name": "Item Assignments",
        "description": "Operations regarding item assignments",
    },
]

swagger_ui_parameters = {
    "syntaxHighlight": True
}

app_title = 'Pets Sample FastAPI'
app_version = '1.1.0'
app_desc = '''
This is the FastAPI Sample Project. Designed to emulate a pets and trainer system.
Primarily for teaching and learning FastAPI.
Feel free to use a test webserver for basic sample data
'''