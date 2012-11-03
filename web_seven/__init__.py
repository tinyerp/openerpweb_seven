# -*- coding: utf-8 -*-

from . import openerp_core
from . import openerpweb

openerp_core.patch_all()

# Using OpenERP Web 7?
openerpweb.patch_web7()
