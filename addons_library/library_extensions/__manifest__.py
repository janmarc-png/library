{
    'name': 'Library Extensions',
    'version': '1.0.0',
    'summary': 'Extensions for the Library module',
    'description': 'This module extends the functionality of the Library module.',
    'author': 'Jan Marc Coloma',
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_category_views.xml',
        'views/library_menus.xml',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': False,
}