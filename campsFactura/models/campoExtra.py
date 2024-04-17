from odoo import models, fields, api

class CampoExtra(models.Model):
    _inherit = 'res.partner'
    _description = 'Campo Extras Factura'
    

    Representante = fields.Char('Representante', required=False, placeholder='Representante')
    
