# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.modules.module import get_module_resource
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class res_relationship(osv.osv):
    _name = "res.relationship"
    
    _columns = {
        'name': fields.char('Name', required=True),
    }
res_relationship()

class res_religion(osv.osv):
    _name = "res.religion"
    
    _columns = {
        'name': fields.char('Name', required=True),
    }
res_religion()

class employee_document_type(osv.osv):
    _name = "employee.document.type"
    
    _columns = {
        'name': fields.char('Name', required=True),
    }
employee_document_type()