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
from openerp import tools, api
from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
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
    
    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}