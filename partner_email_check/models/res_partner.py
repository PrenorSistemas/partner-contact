# -*- coding: utf-8 -*-
# Copyright 2017 Komit <http://komit-consulting.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import api, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

try:
    from validate_email import validate_email
except ImportError:
    _logger.debug('Cannot import "validate_email".')

    def validate_email(email):
        _logger.warning(
            'Can not validate email, '
            'python dependency required "validate_email"')
        return True


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def constrains_email(self):
        for rec in self.filtered("email"):
            self.email_check(rec.email)

    @api.model
    def email_check(self, emails):
        for email in emails.split(','):
            if not validate_email(email):
                raise ValidationError(
                    _("%s is an invalid email") % email.strip()
                )
        return True
