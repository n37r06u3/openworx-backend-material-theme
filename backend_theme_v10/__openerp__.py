# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "V10c Backend Theme",
    "summary": "Odoo 10.0 community backend theme"
               "web",
    "version": "10.0.1.0.0",
    "category": "Website",
    "website": "http://www.openworx.nl",
	"description": """
Backend theme for Odoo 10.0 community edition.
The app dashboard is based on the module web_responsive from LasLabs Inc.
    """,
    "author": "Openworx",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
}
