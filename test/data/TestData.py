class TestData():

    authors = [
        {'id': None, 'f_name': 'Kurt', 'l_name': 'Vonnegut', 'email': 'KVonnegut@gmail.com'},
        {'id': None, 'f_name': 'Mark', 'l_name': 'Twain', 'email': 'MTwain@gmail.com'},
    ]

    _vonnegut_titles = [
        {'id': None, 'author_id': None, 'title': 'Slaughterhouse-Five', 'pub_year': '1969'},
        {'id': None, 'author_id': None, 'title': 'The Sirens of Titan', 'pub_year': '1959'},
        {'id': None, 'author_id': None, 'title': "Cat's Cradle", 'pub_year': '1963'},
        {'id': None, 'author_id': None, 'title': 'Player Piano', 'pub_year': '1952'},
    ]
    _twain_titles = [
        {'id': None, 'author_id': None, 'title': 'The Adventures Of Tom Sawyer', 'pub_year': '1876'},
        {'id': None, 'author_id': None, 'title': 'The Adventures of Huckleberry Finn', 'pub_year': '1878'},
        {'id': None, 'author_id': None, 'title': "A Connecticut Yankee in King Arthur's Court", 'pub_year': '1889'},
        {'id': None, 'author_id': None, 'title': 'Letters from the Earth', 'pub_year': '1962'},
    ]

    books = _vonnegut_titles + _twain_titles

    authors_and_books = [
        {'l_name': 'Vonnegut',
        'titles': _vonnegut_titles},
        {'l_name': 'Twain',
        'titles': _twain_titles}
    ]
