# 2.4 Python Librarian

authors = {
    "Arundhati Roy": {
        "genre": "literary fiction",
        "books": [
            "The God of Small Things",
            "The Ministry of Utmost Happiness"
        ],
        "active": True
    },
    "Brandon Sanderson": {
        "genre": "fantasy",
        "books": [
            "The Way of Kings",
            "Words of Radiance",
            "Oathbringer"
        ],
        "active": True,
        "phone": {
            "home": "(281) 330-8004",
            "work": "(877) CASH-NOW"
        }
    },
    "Kobo Abe": {
        "genre": "absurdist fiction",
        "books": [
            "The Woman in the Dunes",
            "The Face of Another"
        ],
        "active": False
    },
}
# D. Create a list of all books available in our library

print(list(authors.keys()))
