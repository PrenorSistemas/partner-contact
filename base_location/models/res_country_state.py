# -*- coding: utf-8 -*-
# Part of Norprevencion. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.modules.registry import Registry
from odoo.tools.safe_eval import safe_eval
import odoo.addons.decimal_precision as dp
import logging
import time

_logger = logging.getLogger(__name__)



class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    region_id = fields.Many2one('res.country.region')