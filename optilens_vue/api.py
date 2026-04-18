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

@frappe.whitelist()
def get_filter_options():
    """Get filter options for stock page (companies, warehouses, brands, item groups)"""
    try:
        # Get companies
        companies = frappe.db.get_all('Company', fields=['name'], limit=50)
        company_list = [c['name'] for c in companies]
        
        # Get warehouses with company
        warehouses = frappe.db.get_all('Warehouse', 
            filters={'is_group': 0, 'disabled': 0},
            fields=['name', 'company'],
            limit=50
        )
        warehouse_list = [{'name': w['name'], 'company': w.get('company', '')} for w in warehouses]
        
        # Get brands
        brands = frappe.db.get_all('Brand', 
            fields=['name'],
            limit=50
        )
        brand_list = [b['name'] for b in brands]
        
        # Get item groups
        item_groups = frappe.db.get_all('Item Group', 
            filters={'is_group': 0},
            fields=['name'],
            limit=50
        )
        group_list = [g['name'] for g in item_groups]
        
        return {
            'companies': company_list,
            'warehouses': warehouse_list,
            'brands': brand_list,
            'groups': group_list,
        }
    except Exception as e:
        frappe.log_error(f"Error fetching filter options: {e}")
        return {
            'companies': [],
            'warehouses': [],
            'brands': [],
            'groups': [],
        }

@frappe.whitelist()
def get_stock_matrix(companies=None, warehouses=None, brands=None, groups=None):
    """Get stock matrix data based on filters"""
    try:
        # Parse JSON strings if needed
        if isinstance(companies, str):
            companies = frappe.parse_json(companies) or []
        if isinstance(warehouses, str):
            warehouses = frappe.parse_json(warehouses) or []
        if isinstance(brands, str):
            brands = frappe.parse_json(brands) or []
        if isinstance(groups, str):
            groups = frappe.parse_json(groups) or []
        
        # Build base query
        conditions = []
        params = []
        
        # Join with Item and Warehouse
        join_conditions = [
            "LEFT JOIN `tabItem` i ON b.item_code = i.item_code",
            "LEFT JOIN `tabWarehouse` w ON b.warehouse = w.name"
        ]
        
        # Apply warehouse filter (also filters by company implicitly)
        if warehouses:
            conditions.append("b.warehouse IN %(warehouses)s")
            params['warehouses'] = warehouses
        elif companies:
            # If no warehouses selected but companies selected, filter by company
            conditions.append("w.company IN %(companies)s")
            params['companies'] = companies
        
        # Apply brand filter
        if brands:
            conditions.append("i.brand IN %(brands)s")
            params['brands'] = brands
        
        # Apply item group filter
        if groups:
            conditions.append("i.item_group IN %(groups)s")
            params['groups'] = groups
        
        # Build and execute query
        where_clause = " AND ".join(conditions) if conditions else "1=1"
        joins = " ".join(join_conditions)
        
        query = f"""
            SELECT 
                b.item_code,
                b.warehouse,
                b.actual_qty,
                i.item_name,
                i.custom_sph,
                i.custom_cyl,
                i.brand,
                i.item_group,
                w.company
            FROM `tabBin` b
            {joins}
            WHERE {where_clause}
            ORDER BY b.item_code, b.warehouse
            LIMIT 1000
        """
        
        results = frappe.db.sql(query, params, as_dict=True)
        
        # Debug: Check for negative quantities
        negative_items = [r for r in results if r.actual_qty < 0]
        print(f">>> Total items: {len(results)}, Negative qty items: {len(negative_items)}")
        if negative_items:
            print(f">>> First negative item: {negative_items[0]}")
        
        # Format data for matrix - items have SPH and CLY (come from POS or Optic app) attributes
        matrix_data = {}
        
        for row in results:
            # Extract SPH and CLY from item_code or custom fields
            sph = row.get('custom_sph', 0)
            cly = row.get('custom_cly', 0)
            
            key = f"{sph}_{cly}"
            if key not in matrix_data:
                matrix_data[key] = 0
            matrix_data[key] += row.actual_qty
        
        return {
            'matrix': matrix_data,
            'items': results,
            'total_qty': sum(r.actual_qty for r in results),
            'filters_applied': {
                'companies': companies,
                'warehouses': warehouses,
                'brands': brands,
                'groups': groups
            }
        }
    except Exception as e:
        frappe.log_error(f"Error fetching stock matrix: {e}")
        return {
            'matrix': {},
            'items': [],
            'total_qty': 0,
            'filters_applied': {}
        }
