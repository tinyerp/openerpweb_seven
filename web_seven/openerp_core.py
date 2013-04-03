# -*- coding: utf-8 -*-
from contextlib import contextmanager
import logging

import openerp
from openerp.osv import orm, fields
from openerp.release import version_info
import openerp.tools as tools

logger = logging.getLogger('openerp.osv.orm')


def patch_cli():
    """Create a fake "cli" object to replace the missing module."""
    openerp.cli = type('cli', (), {'Command': object})


def patch_modules_registry():
    """Backport the Registry.cursor helper."""
    def cursor(self, auto_commit=True):
        cr = self.db.cursor()
        try:
            yield cr
            if auto_commit:
                cr.commit()
        finally:
            cr.close()

    openerp.modules.registry.Registry.cursor = contextmanager(cursor)


def patch_osv_name_get():
    """Do not fail if _rec_name refers to a non-existent column."""
    def name_get(self, cr, user, ids, context=None):
        if not ids:
            return []
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = self.read(cr, user, ids, [self._rec_name], context, load='_classic_write')
        try:
            return [(r['id'], tools.ustr(r[self._rec_name])) for r in res]
        except KeyError:
            logger.warning('Model %r is missing _rec_name attribute' % self._name)
            return [(res_id, str(res_id)) for res_id in ids]
    name_get.__doc__ = orm.BaseModel.name_get.__doc__
    orm.BaseModel.name_get = name_get


def patch_osv_fields_char():
    """Arguments "string" and "size" become optional with OpenERP 7."""
    _column = fields._column

    def __init__(self, string="unknown", size=None, **args):
        _column.__init__(self, string=string, size=size, **args)
        self._symbol_set = (self._symbol_c, self._symbol_set_char)

    fields.char.__init__ = __init__


def patch_addons_base():
    """Backport missing _columns and methods for the "base" addon."""
    openerp.modules.load_openerp_module('base')
    ir_ui_menu = openerp.addons.base.ir.ir_ui_menu.ir_ui_menu
    company_columns = openerp.addons.base.res.res_company.res_company._columns

    def get_needaction_data(self, cr, uid, ids, context=None):
        return {}

    company_columns['logo_web'] = fields.binary("Logo Web")
    ir_ui_menu.get_needaction_data = get_needaction_data


def patch_all():
    if version_info < (7, 0):
        patch_cli()
        patch_modules_registry()
        patch_osv_name_get()
        patch_osv_fields_char()
        patch_addons_base()
