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
{
    "name": "tcn_invoice_ccc",
    "version": "1.0",
    "depends": ["base","sale"],
    "author": "Tecon Soluciones Informáticas S.L.",
    "category": "sale",
    "description": """
    Selección automática de cuenta de pago en factura dependiendo del cliente / forma de pago.
    """,
    "init_xml": [],
    'update_xml': ["views/payment_type_view.xml"],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
