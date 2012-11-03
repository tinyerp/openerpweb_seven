# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright © 2012 - Florent Xicluna
#   All Rights Reserved
#
#   License: BSD
#
##############################################################################
{
    'name': 'Web client 7.0 for OpenERP 6.1 server',
    'version': '0.1',
    'category': 'Custom Modules',
    'description': """Adapt the new web client for OpenERP 6.1.""",
    'author': 'Florent Xicluna',
    'website': 'https://code.launchpad.net/~florent.x/openobject-addons/6.1-web_seven',
    'license': 'Other OSI approved licence',
    'depends': ['web'],
    'js': ['static/src/js/compat61.js'],
    'installable': True,
    'auto_install': False,
}
