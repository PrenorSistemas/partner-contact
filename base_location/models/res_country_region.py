# -*- coding: utf-8 -*-
# Part of Norprevencion. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.modules.registry import Registry
from odoo.tools.safe_eval import safe_eval
import odoo.addons.decimal_precision as dp
import logging
import time

_logger = logging.getLogger(__name__)

com_auto = {'00': '', '01': 'EK', '02': 'CM', '03': 'PV', '04': 'AN', '05': 'CL', '06': 'EX', '07': 'IB', '08': 'CA',
            '09': 'CL', '10': 'EX', '11': 'AN', '12': 'PV', '13': 'CM', '14': 'AN', '15': 'GA', '16': 'CM', '17': 'CA',
            '18': 'AN', '19': 'CM', '20': 'EK', '21': 'AN', '22': 'AR', '23': 'AN', '24': 'CL', '25': 'CA', '26': 'LR',
            '27': 'GA', '28': 'MA', '29': 'AN', '30': 'MU', '31': 'NA', '32': 'GA', '33': 'AS', '34': 'CL', '35': 'IC',
            '36': 'GA', '37': 'CL', '38': 'IC', '39': 'CB', '40': 'CL', '41': 'AN', '42': 'CL', '43': 'CA', '44': 'AR',
            '45': 'CM', '46': 'PV', '47': 'CL', '48': 'EK', '49': 'CL', '50': 'AR', '51': 'CE', '52': 'ME'}


class region(models.Model):
    _name = 'res.country.region'
    _description = 'Region'

    country_id = fields.Many2one('res.country', 'Country', required=True)
    name = fields.Char('Name', size=64, required=True)
    code = fields.Char('Code', size=10)
    state_ids = fields.One2many('res.country.state', 'region_id', string="Res country state")
    _order = 'name'
