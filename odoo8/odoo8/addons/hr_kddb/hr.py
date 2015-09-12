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

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    
    _columns = {
        'code': fields.char('Code', required=True),
        'eng_second_name': fields.char('Second Name'),
        'eng_third_name': fields.char('Third Name'),
        'arb_first_name': fields.char('First Name'),
        'arb_second_name': fields.char('Second Name'),
        'arb_third_name': fields.char('Third Name'),
        'document_ids': fields.one2many('hr.document', 'employee_id', 'Documents'),
        
        'home_street': fields.char('Street'),
        'home_street2': fields.char('Street2'),
        'home_zip': fields.char('Zip', size=24, change_default=True),
        'home_city': fields.char('City'),
        'home_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'home_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'home_phone': fields.char('Phone'),
        'home_mobile': fields.char('Mobile'),
        
        'home_emg_street': fields.char('Street'),
        'home_emg_street2': fields.char('Street2'),
        'home_emg_zip': fields.char('Zip', size=24, change_default=True),
        'home_emg_city': fields.char('City'),
        'home_emg_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'home_emg_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'home_emg_phone': fields.char('Phone'),
        'home_emg_mobile': fields.char('Mobile'),
        
        'residencial_street': fields.char('Street'),
        'residencial_street2': fields.char('Street2'),
        'residencial_zip': fields.char('Zip', size=24, change_default=True),
        'residencial_city': fields.char('City'),
        'residencial_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'residencial_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'residencial_phone': fields.char('Phone'),
        'residencial_mobile': fields.char('Mobile'),
        
        'residencial_emg_street': fields.char('Street'),
        'residencial_emg_street2': fields.char('Street2'),
        'residencial_emg_zip': fields.char('Zip', size=24, change_default=True),
        'residencial_emg_city': fields.char('City'),
        'residencial_emg_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'residencial_emg_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'residencial_emg_phone': fields.char('Phone'),
        'residencial_emg_mobile': fields.char('Mobile'),
    }
    
class hr_document(osv.osv):
    _name = 'hr.document'
    
    _columns = {
        'name': fields.char('Document No / ID', required=True),
        'employee_id': fields.many2one('hr.employee', 'Employee'),
        'document_type_id': fields.many2one('employee.document.type', 'Document Type'),
        'document_type': fields.char('Document Type'),
        'issue_date': fields.datetime('Issue Date'),
        'expiry_date': fields.datetime('Expiry Date'),
        'alert_before': fields.integer('Alert Before'),
        'document': fields.binary('Document'),
        'issued_country_id': fields.many2one('res.country', 'Issued Country'),
        'entry_type': fields.selection([('single', 'Single'), ('multiple', 'Multiple')], 'Entry Type'),
        'deposited_user_id': fields.many2one('res.users', 'Deposited With'),
        'deposited_date': fields.datetime('Deposited Date'),
    }
    
    def onchange_document_type_id(self, cr, uid, ids, document_type_id, context=None):
        if document_type_id:
            document_type = self.pool.get('employee.document.type').browse(cr, uid, document_type_id).name
            return {'value': {'document_type': document_type.upper()}}
        return {'value': {'document_type': False}}
    
class hr_employee_work_history(osv.osv):
    _name = 'hr.employee.work.history'
    
    _columns = {
    
    }
    