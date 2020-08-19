# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Foche_mission(models.Model):
    _name = 'fiche.mission'
    _description = 'Fiche de mission'


    name = fields.Char(string="nom")
    date_create = fields.Date()
    base_depart_ain_sbaa = fields.Boolean(string='Ain Sebaa')
    base_depart_maarif = fields.Boolean(string='Mâarif')
    masculin = fields.Boolean(string='masculin')
    feminin = fields.Boolean(string='féminin')
    mutuelle_avec = fields.Boolean(string="Oui")
    mutuelle_sans = fields.Boolean(string="Non")
