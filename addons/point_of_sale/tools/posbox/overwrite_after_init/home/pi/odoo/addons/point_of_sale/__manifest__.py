{
    'name': 'Website Slides',
    'category': 'Website',
    'sequence': 145,
    'version': '1.0',
    'summary': 'Share and Organize Courses',
    'website': 'https://www.odoo.com/app/elearning',
    'description': "",
    'depends': ['website', 'website_profile'],
    'data': [
        'views/website_slides_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_slides/static/src/scss/*.scss',
            'website_slides/static/src/js/*.js',
        ],
    },
    'application': True,
    'license': 'LGPL-3',
}
