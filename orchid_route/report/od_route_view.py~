# -*- coding: utf-8 -*-
from openerp import tools
from openerp.osv import fields, osv

class od_routeview(osv.osv):
    _name = 'od.routeview'
    _description = 'OD ROUTE VIEW'
    _auto = False
    _columns = {
        'id':fields.integer('id'),
        'name':fields.char('Discription',size=128),
        'route_code':fields.char('Route Code',size=4),
        'shop':fields.char('Shop',size=128),
        'vehicle':fields.char('Vehicle',size=128),
        'sale_person': fields.char('Salesperson',size=128),
        'driver': fields.char('Driver',size=128),
        'helper': fields.char('Helper',size=128),
        'assistant': fields.char('Assistant',size=128),
        'area': fields.char('Area',size=128),
        'invoice_no': fields.char('Invoice#',size=128),
        'grv_no': fields.char('GRV#',size=128),
        'receipt_no': fields.char('Receipt#',size=128),
        'transfer_no': fields.char('Transfer#',size=128),
        'pwd_admin': fields.char('Passwd Admin'),
        'pwd_manager':fields.char('Passwd Manager'),
        'pwd_user': fields.char('Passwd User'),
}
#    def init(self, cr):
#        tools.drop_view_if_exists(cr, 'od_routeview')
#        cr.execute("""create or replace view od_routeview as(
#SELECT od.id as id, od.route_code AS route_code,
#	od.name as name,
#	ss.name as shop,
#	vh.name as vehicle,
#	emp.name_related as sale_person,
#	emp_d.name_related as driver,
#	emp_h.name_related as helper,
#	emp_a.name_related as assistant,
#	od.area as area,
#	od.invoice_no as invoice_no,
#	od.grv_no as grv_no,
#	od.receipt_no as receipt_no,
#	od.transfer_no as transfer_no,
#	od.pwd_admin as pwd_admin,
#	od.pwd_manager as pwd_manager,
#	od.pwd_user as pwd_user from od_route od 
#		 LEFT JOIN hr_employee emp on (od.sale_person_id = emp.id)
#	     LEFT JOIN hr_employee emp_d on (od.driver_id = emp_d.id)
#		  LEFT JOIN hr_employee emp_h on (od.helper_id = emp_h.id)
#		  LEFT JOIN hr_employee emp_a on (od.assistant_id = emp_a.id)
#		  LEFT JOIN fleet_vehicle vh ON  (od.vehicle = vh.id)
#		  LEFT JOIN sale_shop ss ON (od.shop_id = ss.id)
#		)
#        """)

class od_product_pull_view(osv.osv):
    _name = 'od.product.pull.view'
    _auto =False
    _description = 'OD Product Pull View'
    _columns = {
        'id':fields.integer('id'),
        'product_id': fields.many2one('product.product','Product'),
        'code': fields.char('Code'),
        'name': fields.char('Name'),
        'list_price': fields.float('List Price'),
        'category': fields.char('Category'),
        'pos_group': fields.char('POS Group'),
        'sale_ok' : fields.boolean('Sale Ok'),
        'category_id': fields.many2one('pos.category','Category ID'),
        'def_unit': fields.char('Def Unit'),
        'unit_category': fields.char('Unit Category'),
        'standard_price': fields.float('Cost'),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'od_product_pull_view')
        cr.execute("""create or replace view od_product_pull_view as(
        SELECT
        pd.id as id,
        pd.id as product_id,
        pd.default_code AS code,
        pd_t.name as name,
        pd_t.list_price as list_price,
        pd_t.standard_price as standard_price,
        cat.name AS category,
        pd_t.sale_ok AS sale_ok,
        pcat.name AS pos_group,
        unit.name AS def_unit,
        unit_cat.name AS unit_category,
        unit.category_id AS category_id
        FROM
        product_product pd
        LEFT JOIN product_template pd_t ON (pd.product_tmpl_id = pd_t.id)
        LEFT JOIN product_category cat ON (pd_t.categ_id = cat.id)
        LEFT JOIN pos_category pcat ON (pd.pos_categ_id = pcat.id)
        LEFT JOIN product_uom unit ON (pd_t.uom_id = unit.id)
        LEFT JOIN product_uom_categ unit_cat ON (unit.category_id = unit_cat.id)
        )
        """)
# pcat.name AS pos_group,
#        LEFT JOIN pos_category pcat ON (pd.pos_categ_id = pcat.id)
class od_pricelist_view(osv.osv):
    _name = 'od.pricelist.view'
    _auto = False
    _description = 'Od Pricelist View'
    _columns ={
       # 'shop_id': fields.many2one('sale.shop','Shop',readonly=True),
        'route_id': fields.many2one('od.route','Route',readonly=True),
        'based_on' :fields.char('Based On',readonly=True),
        'price_discount' :fields.float('Discount Price',readonly=True),
        'min_qty' :fields.float('Min Qty',readonly=True),
        'price_surcharge' :fields.float('Surcharge Price',readonly=True),
        'pdt_id':fields.many2one('product.product','Product',readonly=True),
        'pdt_cat_id':fields.many2one('product.category','Category',readonly=True),
        'pricelist_id': fields.many2one('product.pricelist.item','Pricelist Item',readonly=True),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'od_pricelist_view')
        cr.execute("""create or replace view od_pricelist_view as(
SELECT
  row_number() OVER (ORDER BY item.id) AS id,
 item. id as pricelist_id,
 od_rte. ID AS route_id,
 base AS based_on,
 item.min_quantity AS min_qty,
 price_discount,
 price_surcharge,
 product_id AS pdt_id,
 categ_id  AS pdt_cat_id
FROM
 product_pricelist_item item
LEFT JOIN product_pricelist_version p_version ON 
 item.price_version_id = p_version. ID
LEFT JOIN product_pricelist p_list ON 
 p_version.pricelist_id = p_list. ID
LEFT JOIN od_route od_rte ON 
 od_rte.pricelist_id = p_list. ID
WHERE
 item. SEQUENCE = 0
AND p_version.active = 't'
AND p_list.active = 't'
AND p_list. TYPE = 'sale'
AND od_rte.id is NOT NULL

)
""")

class od_sale_route_view(osv.osv):
    _name = 'od.sale.route.view'
    _auto = False
    _description = 'Od Sale Route View'
    _columns = {
        'order_id':fields.many2one('sale.order','Sale Order'),
        'order_line_id': fields.many2one('sale.order.line','Sale Order Line'),
        'client_order_ref': fields.char('Client Order Ref'),
        'date_order': fields.date('Order Date'),
        'route_code': fields.char('Route Code',size =30),
        'invoice_type_id':fields.many2one('sale_journal.invoice.type','Invoice Type'),
        'shop_id': fields.many2one('sale.shop','Shop'),
        'partner_id': fields.many2one('res.partner','Customer'),
        'user_id': fields.many2one('res.users','User'),
        'pricelist_id': fields.many2one('product.pricelist','Price List'),
        'name': fields.char('name',size=100),
        'product_id': fields.many2one('product.product','Product'),
        'pdt_name': fields.char('pdt_name',size=100),
        'product_uom': fields.many2one('product.uom','UOM'),
        'product_uom_qty': fields.float('product_uom_qty'),
        'price_unit': fields.float('price_unit'), 
        'discount': fields.float('Discount'),
        'delay':fields.char('delay',size = 50),
        'type': fields.selection([('make_to_stock', 'from stock'), ('make_to_order', 'on order')], 'Procurement Method'),
    }

    def init(self, cr):
        tools.drop_view_if_exists(cr, 'od_sale_route_view')
        cr.execute("""create or replace view od_sale_route_view as(

SELECT
  ROW_NUMBER () OVER (ORDER BY so_line.product_id) AS id,
  route.route_code as route_code, 
  so.id as order_id,
  so.date_order as date_order,
  so.shop_id as shop_id,
  so.invoice_type_id as invoice_type_id,
  so.partner_id as partner_id,
  so.user_id as user_id,
  so.pricelist_id as pricelist_id, 
  so.name as name,
  so.client_order_ref as client_order_ref,
  so_line.id as order_line_id,
  so_line.product_id as product_id,
  so_line.name as pdt_name,
  so_line.product_uom as product_uom, 
  so_line.price_unit as price_unit,
  so_line.product_uom_qty as product_uom_qty,
  so_line.discount as discount,
  so_line.delay as delay,
  so_line.type as type
 FROM
 sale_order_line so_line
LEFT JOIN sale_order so ON so.id = so_line.order_id
LEFT JOIN od_route route ON route.shop_id = so.shop_id
WHERE
 so. STATE = 'draft' and so.name not like (route_code || '%')
AND so.partner_id IN (
 SELECT
  partner_id
 FROM
  route_partner_relation
 WHERE
  route_id = route. ID
))
""")
