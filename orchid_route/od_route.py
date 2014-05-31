# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from tools.translate import _
class od_route(osv.osv):
    _name = "od.route"
    _description = "OD Route"

    def onchange_device_id(self,cr,uid,ids,device_id):
        warning = {}
        if not device_id:
            return {}
        device_ids = self.search(cr, uid, [('device_id', '=', device_id)])
        if device_ids:
            warning = {
                'title': _('Device ID!'),
                'message': "Device ID already exists..! You are adding the same Device ID again..!"
            }
        return {'warning':warning}
    _columns = {
        'name': fields.char('Discription',size=128,required="1"),
        'route_code': fields.char('Route Code',size=4,required="1"),
        'vehicle':fields.many2one('fleet.vehicle','Vehicle',required="1"),
        'warehouse_id': fields.many2one('stock.warehouse','Warehouse',required="1"),
        'shop_id': fields.many2one('sale.shop','Shop',required="1"),
        'pricelist_id': fields.many2one('product.pricelist','Pricelist', required="1"),
        'sale_person_id':fields.many2one('hr.employee','Sales Person',required="1"),
        'helper_id': fields.many2one('hr.employee','Helper'),
        'driver_id': fields.many2one('hr.employee','Driver'),
        'assistant_id': fields.many2one('hr.employee','Assistant'),
        'area': fields.char('Area', size=128),
        'address': fields.char('Address', size=128),
        'city': fields.char('City', size=128),
        'state_id': fields.many2one("res.country.state", 'State'),
        'country_id': fields.many2one('res.country', 'Country'),
        'invoice_no':fields.char('Invoice No',size=10),
        'grv_no':fields.char('GRV No',size=10),
        'transfer_no':fields.char('Transfer No',size=10),
        'receipt_no':fields.char('Receipt No',size=10),
        'pwd_user':fields.char('Passwd User'),
        'pwd_manager':fields.char('Passwd Manager' ),
        'pwd_admin':fields.char('Passwd Admin'),
        
        'check_qty':fields.boolean('Check Quantity'),      
        'device_id': fields.char('Device ID'),
        'gmail_id': fields.char('Email', size=240),
        'gmail_pwd': fields.char('Passwd'),
        'sim_num': fields.char('SIM #'),
        'server_cont_interval': fields.integer('Contact Interval(mins)'),
        'geo_code': fields.integer('GPS Update Interval(mins)'),
        'so_num': fields.char('SO #'),
        'mr_num': fields.char('MR #'),
        'customer_ids': fields.many2many('res.partner','route_partner_relation','route_id','partner_id','Customers')

#        'show_pwd':fields.boolean('Show Passwd'),

    }
#    _defaults ={
#        'show_pwd':False,
#    }
#     

class od_mob_invd(osv.osv):
    _name = "od.mob.invd"
    _description = "OD mobile invoiceD"
    _columns = {
     'td_srf_no': fields.char('Td_Srf_No',size=10),
     'td_lno': fields.integer('Td_Lno'),
     'td_pcd': fields.integer('Td_Pcd'),
     'td_type': fields.char('TD Type',size=4),
     'td_unit': fields.char('TD Unit',size=4),
     'td_qty': fields.float('TD Qty'),
     'td_rate': fields.float('TD Rate'),
     'td_amt': fields.float('TD Amt'),
     'td_desc': fields.char('TD Unit',size=100),
     'td_billno': fields.char('TD Billno',size=10)
    
    }
class od_mob_invh(osv.osv):
    _name = "od.mob.invh"
    _description = "od mobile invoiceH"
    _columns = {
     'th_srf_no': fields.char('Th_Srf_No',size=10),
     'th_doc_date': fields.date('Th_Doc_Date'),
     'th_cust': fields.integer('Th_Cust'),
     'th_route': fields.char('Th_Route',size=10),
     'th_tot': fields.float('Th Tot'),
     'th_doc_ty': fields.char('Th_Doc_Ty',size=5),
     'th_cust_name': fields.char('Th_Cust_Name',size=100),
     'th_refno': fields.char('Th_RefNo',size=10),
     'th_cash': fields.float('Th_Cash'),
     'th_doc_date_time': fields.datetime('Th_Doc_Date_Time'),
     'th_rec_no':fields.char('Th_Rec_No',size = 50)
    }


class od_mob_receipth(osv.osv):
    _name = "od.mob.receipth"
    _description = "odMobReceiptH"
    _columns = {
     'th_doc_no': fields.char('Th_Doc_No',size=10),
     'th_doc_date': fields.date('Th_Doc_Date'),
     'th_route': fields.char('Th_Route',size=10),
     'th_cust': fields.integer('Th_Cust'),
     'th_amt_paid': fields.float('Th_Amt_Paid'),
     'th_discount': fields.float('Th_Discount'),
     'th_deduction': fields.float('Th_Deduction'),
     'th_pay_mode': fields.char('Th_Pay_Mode',size=15),
     'th_cheque_no': fields.char('Th_Cheque_No',size=15),
     'th_cheque_date': fields.date('Th_Cheque_Date'),
     'th_bank': fields.char('Th_Bank',size=40),
     'th_created_on': fields.datetime('Th_Created_On')
    }


class od_mob_receiptd(osv.osv):
    _name = "od.mob.receiptd"
    _description = "odMobReceiptD"
    _columns = {
     'td_doc_no': fields.char('Td_Doc_No',size=10),
     'td_lno': fields.integer('td_lno'),
     'td_invoice_date': fields.date('Td_Invoice_Date'),
     'td_discount': fields.float('Td_Discount'),
     'td_amt_paid': fields.float('Td_Amt_Paid'), 
    }

class od_mob_receiptdeduction(osv.osv):
    _name = "od.mob.receiptdeduction"
    _description = "odMobReceiptDeduction"
    _columns = {
     'td_doc_no': fields.char('Td_Doc_No',size=10),
     'td_lno': fields.integer('Td_Lno'),
     'td_deduction_type': fields.char('Td_Doc_No',size=10),
     'td_ded_amt': fields.float('Td_Ded_amt'), 
    }



