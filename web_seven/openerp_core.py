# -*- coding: utf-8 -*-
import logging

from openerp.osv import orm
from openerp.release import version_info
import openerp.tools as tools

logger = logging.getLogger('openerp.osv.orm')


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


def patch_all():
    if version_info < (7, 0):
        patch_osv_name_get()
