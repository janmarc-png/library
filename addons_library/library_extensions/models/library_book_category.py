from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    _order = 'name'

    name = fields.Char(
        string='Category Name',
        required=True,
        help='Name of the book category'
    )

    _sql_constraints = [
        ('category_name_unique', 'unique(name)', 'Category name must be unique!'),
    ]
