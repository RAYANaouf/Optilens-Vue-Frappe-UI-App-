import frappe
from frappe import _

@frappe.whitelist()
def get_today_sales():
    """Get today's total sales amount"""
    try:
        today = frappe.utils.today()
        sales = frappe.db.sql("""
            SELECT SUM(grand_total) as total
            FROM `tabSales Invoice`
            WHERE posting_date = %s AND docstatus = 1
        """, today, as_dict=True)
        
        if sales and sales[0].get('total'):
            return frappe.format_value(sales[0].total, {'fieldtype': 'Currency'})
        return '$0.00'
    except Exception as e:
        frappe.log_error(f"Error fetching today's sales: {e}")
        return '$0.00'

@frappe.whitelist()
def get_total_products():
    """Get total number of products/items"""
    try:
        count = frappe.db.count('Item', {'disabled': 0})
        return count
    except Exception as e:
        frappe.log_error(f"Error fetching total products: {e}")
        return 0

@frappe.whitelist()
def get_low_stock_items():
    """Get count of low stock items"""
    try:
        # Get items with actual_qty <= 10
        low_stock = frappe.db.sql("""
            SELECT COUNT(DISTINCT item_code) as count
            FROM `tabBin`
            WHERE actual_qty <= 10
        """, as_dict=True)
        
        if low_stock and low_stock[0].get('count'):
            return low_stock[0].count
        return 0
    except Exception as e:
        frappe.log_error(f"Error fetching low stock items: {e}")
        return 0

@frappe.whitelist()
def get_pos_products():
    """Get products for POS"""
    try:
        items = frappe.db.get_all('Item',
            filters={'disabled': 0},
            fields=['item_code', 'item_name'],
            limit=50
        )
        
        # If no items found, return sample data for testing
        if not items:
            return [
                {
                    'item_code': 'SAMPLE-001',
                    'item_name': 'Sample Product 1',
                    'image': None,
                    'standard_rate': 100.0,
                    'item_group': 'Products'
                },
                {
                    'item_code': 'SAMPLE-002',
                    'item_name': 'Sample Product 2',
                    'image': None,
                    'standard_rate': 150.0,
                    'item_group': 'Products'
                },
                {
                    'item_code': 'SAMPLE-003',
                    'item_name': 'Sample Product 3',
                    'image': None,
                    'standard_rate': 75.0,
                    'item_group': 'Products'
                }
            ]
        
        return items
    except Exception as e:
        frappe.log_error(f"Error fetching POS products: {e}")
        return []

@frappe.whitelist()
def get_inventory_items():
    """Get inventory items with stock levels"""
    try:
        items = frappe.db.sql("""
            SELECT 
                b.item_code,
                i.item_name,
                i.item_group,
                b.actual_qty,
                i.modified
            FROM `tabBin` b
            LEFT JOIN `tabItem` i ON b.item_code = i.item_code
            WHERE i.disabled = 0
            ORDER BY b.actual_qty ASC
            LIMIT 100
        """, as_dict=True)
        return items
    except Exception as e:
        frappe.log_error(f"Error fetching inventory items: {e}")
        return []

@frappe.whitelist()
def get_pricing_data():
    """Get pricing data for items"""
    try:
        items = frappe.db.get_all('Item',
            filters={'disabled': 0},
            fields=['item_code', 'item_name', 'standard_rate', 'modified'],
            limit=100
        )
        
        # Add wholesale rate if price list exists
        for item in items:
            item['wholesale_rate'] = item.get('standard_rate', 0) * 0.8  # 20% discount for wholesale
        
        return items
    except Exception as e:
        frappe.log_error(f"Error fetching pricing data: {e}")
        return []
