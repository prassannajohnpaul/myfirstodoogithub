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

class hr_employee_family_members(osv.osv):
    _name = 'hr.employee.family.member'
    
    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)
    
    _columns = {
        'name': fields.char('First Name', required=True),
        'eng_second_name': fields.char('Second Name'),
        'eng_third_name': fields.char('Third Name'),
        'arb_first_name': fields.char('First Name'),
        'arb_second_name': fields.char('Second Name'),
        'arb_third_name': fields.char('Third Name'),
        'gender': fields.selection([('male', 'Male'), ('female', 'Female')], 'Gender'),
        'dob': fields.date("Date of Birth"),
        'relationship_id': fields.many2one('res.relationship', 'Relationship'),
        'ssnid': fields.char('SSN No', help='Social Security Number'),
        'sinid': fields.char('SIN No', help="Social Insurance Number"),
        'identification_id': fields.char('Identification No'),
        'mobile': fields.char('Mobile'),
        'email': fields.char('Email'),
        'country_id': fields.many2one('res.country', 'Nationality'),
        'employee_id': fields.many2one('hr.employee', 'Employee'),
        'document_ids': fields.one2many('hr.employee.family.document', 'family_member_id', 'Family Member'),
        'image': fields.binary("Photo",
            help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'hr.employee': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'hr.employee': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),
    }
    
class hr_employee_family_document(osv.osv):
    _name = 'hr.employee.family.document'
    
    _columns = {
        'name': fields.char('Document No / ID', required=True),
        'family_member_id': fields.many2one('hr.employee.family.member', 'Employee'),
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
    
class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    
    _columns = {
        'family_member_ids': fields.one2many('hr.employee.family.member', 'employee_id', 'Family Members'),    
    }