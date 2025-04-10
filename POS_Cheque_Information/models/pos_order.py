from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
  _inherit = 'pos.order'

  identite_number = fields.Char(string="Identité Number")
  cheque_number = fields.Char(string="Numero Chèque")
  banque = fields.Selection([
    ('attijari_wafabank', 'ATTIJARI WAFABANK'),
    ('banque_populaire', 'Banque Populaire'),
    ('SGMB', 'Socièté Général'),
    ('LPB', 'AL BARID BANK'),
    ('BCP', 'BANQUE CENTRALE POPULAIRE'),
    ('BMCE', 'BANK OF AFRICA'),
    ('BMCI', 'BANQUE MAROCAINE POUR LE COMMERCE ET L’INDUSTRIE'),
    ('CADM', 'CREDIT AGRICOLE DU MAROC'),
    ('CFG', 'CFG BANK'),
    ('CDM', 'CREDIT DU MAROC'),
    ('CITI', 'CITIBANK MAGHREB'),
    ('ABM', 'ARAB BANK MAROC'),
    ('CIH', 'CREDIT IMMOBILIER ET HOTELIER')
  ], string="Banque")
  status = fields.Selection([
    ('ok', 'OK'),
    ('ko', 'KO'),
  ], string="Status", default="ok")
  cheque_date = fields.Date(string="Date pour le Chèque", help="Date of the cheque.")

  def _order_fields(self, ui_order):
    result = super()._order_fields(ui_order)
    _logger.debug("UI Order: %s", ui_order)
    result['identite_number'] = ui_order.get('identite_number')
    result['cheque_number'] = ui_order.get('cheque_number')
    result['banque'] = ui_order.get('banque')
    result['cheque_date'] = ui_order.get('cheque_date')

    return result



