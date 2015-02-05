#coding: utf8
##############################################################################
#
#    Tecon Soluciones Informáticas, S.L.
#    (http://www.tecon.es). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv,fields

class account_invoice(osv.osv):
  _inherit = 'account.invoice'
  
  _columns = {
              'partner_bank_id': fields.many2one('res.partner.bank', 'Bank Account',
               help='Bank Account Number, Company bank account if Invoice is customer or supplier refund, otherwise Partner bank account number.'),
              }
  
  def create(self, cr, uid, values, context = None):
    if values.has_key('payment_type') and values.has_key('partner_id') and not values.has_key('parter_bank_id') :
      partner_id = values.get('partner_id')
      payment_type_id = values.get('payment_type')
      if payment_type_id :
        payment_type = self.pool.get('payment.type').browse(cr, uid, payment_type_id)
        if payment_type :
          bank_value = False
          if payment_type.force_bank_payment_id :
            bank_value = payment_type.force_bank_payment_id.id
          elif payment_type.suitable_bank_types :
            for payment_type.suitable_bank_type in payment_type.suitable_bank_types :
              code_search = payment_type.suitable_bank_type.code
              bank_partner_ids = self.pool.get('res.partner.bank').search(cr, uid, [('partner_id','=',partner_id),('state','=',code_search)],order='default_bank desc')            
              if bank_partner_ids :
                bank_value = bank_partner_ids[0]
                break        
          if bank_value :
            values.update({'partner_bank_id':bank_value})
    return super(account_invoice,self).create(cr, uid, values, context)
  
  def onchange_payment_type(self,cr,uid,ids,payment_type,partner_id,result=None):
    result = super(account_invoice,self).onchange_payment_type(cr,uid,ids,payment_type,partner_id,result=result)
    if result is None:
      result = {'value': {}}
    
    if payment_type :
      payment_type_data = self.pool.get('payment.type').browse(cr, uid, payment_type)
      if payment_type_data.force_bank_payment_id :
        result['value']['partner_bank_id'] = payment_type_data.force_bank_payment_id.id
    
    return result
    
    
account_invoice()