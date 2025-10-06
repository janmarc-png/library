# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one(
        'res.partner',
        string='Author',
        required=True,
        help='Author of the book'
    )
    category_id = fields.Many2many(
            'library.book.category',
            'library_book_category_rel',
            'book_id',
            'category_id',
            string='Categories',
            help='Categories for this book'
        )
