biosphere = {
    ("biopshere", 1): {
        'categories': ['things'],
        'code': 1,
        'exchanges': [],
        'name': 'an emission',
        'type': 'process',
        'unit': 'kg'
        },
    ("biosphere", 2): {
        'categories': ['things'],
        'code': 2,
        'exchanges': [],
        'type': 'another emission',
        'unit': 'kg'
        },
}

food = {
    ("food", 1): {
        'categories': ['stuff', 'meals'],
        'code': 1,
        'exchanges': [{
            'amount': 0.5,
            'input': ('Test', 2),
            'technosphere': True,
            'uncertainty type': 0},
            {'amount': 0.05,
            'input': ('biosphere', 1),
            'technosphere': False,
            'uncertainty type': 0}],
        'location': 'GLO',
        'name': 'lunch',
        'type': 'process',
        'unit': 'kg'
        },
    ("food", 2): {
        'categories': ['stuff', 'meals'],
        'code': 2,
        'exchanges': [{
            'amount': 0.25,
            'input': ('Test', 1),
            'technosphere': True,
            'uncertainty type': 0},
            {'amount': 0.15,
            'input': ('biosphere', 2),
            'technosphere': False,
            'uncertainty type': 0}],
        'location': 'GLO',
        'name': 'dinner',
        'type': 'process',
        'unit': 'kg'
        },
    }
