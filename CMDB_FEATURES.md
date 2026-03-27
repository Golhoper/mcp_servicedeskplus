# CMDB Features - ServiceDesk Plus MCP Server

## 🎯 **CMDB Overview**

The MCP server has been extended to fully support CMDB (Configuration Management Database) functions of ServiceDesk Plus, including:

## 📋 **Supported CMDB Modules**

### 1. **Configuration Items (CIs) Management**
- ✅ `list_configuration_items` - Get list of CIs with filters
- ✅ `get_configuration_item` - Get CI details
- ✅ `create_configuration_item` - Create a new CI
- ✅ `update_configuration_item` - Update a CI
- ✅ `delete_configuration_item` - Delete a CI
- ✅ `get_ci_types` - Get list of CI types
- ✅ `get_ci_relationships` - Get CI relationships

**Usage Examples:**
```
"Create a new Configuration Item for a web server named 'WEB-SRV-001', type 'server', status 'active'"
"Get list of 20 Configuration Items with type 'network_device' and status 'active'"
"Update CI WEB-SRV-001 with status 'under_maintenance'"
```

### 2. **Asset Management**
- ✅ `list_assets` - Get list of assets with filters
- ✅ `get_asset` - Get asset details
- ✅ `create_asset` - Create a new asset
- ✅ `update_asset` - Update an asset
- ✅ `delete_asset` - Delete an asset
- ✅ `get_asset_types` - Get list of asset types
- ✅ `get_asset_categories` - Get asset categories
- ✅ `get_asset_locations` - Get asset locations
- ✅ `get_asset_models` - Get asset models
- ✅ `get_asset_vendors` - Get asset vendors

**Usage Examples:**
```
"Create a new asset named 'LAPTOP-001', type 'laptop', status 'in_use', assigned to 'john.doe@company.com'"
"Get list of assets with status 'under_maintenance' and location 'IT Department'"
"Update asset LAPTOP-001 with status 'retired'"
```

### 3. **Software License Management**
- ✅ `list_software_licenses` - Get list of software licenses
- ✅ `get_software_license` - Get license details
- ✅ `create_software_license` - Create a new license
- ✅ `update_software_license` - Update a license
- ✅ `get_software_products` - Get list of software products
- ✅ `get_license_types` - Get license types

**Usage Examples:**
```
"Create a new software license for 'Microsoft Office 365' with 100 licenses, vendor 'Microsoft'"
"Get list of licenses with vendor 'Adobe' and product 'Photoshop'"
"Update the Office 365 license with a new license count of 150"
```

### 4. **Contract Management**
- ✅ `list_contracts` - Get list of contracts
- ✅ `get_contract` - Get contract details
- ✅ `create_contract` - Create a new contract
- ✅ `update_contract` - Update a contract
- ✅ `get_contract_types` - Get contract types
- ✅ `get_contract_vendors` - Get contract vendors

**Usage Examples:**
```
"Create a new contract with vendor 'Dell', starting from '2024-01-01', ending '2024-12-31'"
"Get list of contracts with status 'active' and vendor 'Microsoft'"
"Update the Dell contract with a new end date of '2025-12-31'"
```

### 5. **Purchase Order Management**
- ✅ `list_purchase_orders` - Get list of purchase orders
- ✅ `get_purchase_order` - Get purchase order details
- ✅ `create_purchase_order` - Create a new purchase order
- ✅ `update_purchase_order` - Update a purchase order
- ✅ `get_po_statuses` - Get purchase order statuses

**Usage Examples:**
```
"Create a new purchase order with vendor 'HP' for 10 laptops"
"Get list of purchase orders with status 'pending_approval'"
"Update PO HP-001 with status 'approved'"
```

### 6. **Vendor Management**
- ✅ `list_vendors` - Get list of vendors
- ✅ `get_vendor` - Get vendor details
- ✅ `create_vendor` - Create a new vendor
- ✅ `update_vendor` - Update a vendor
- ✅ `get_vendor_types` - Get vendor types

**Usage Examples:**
```
"Create a new vendor 'Dell Technologies' with email 'contact@dell.com'"
"Get details of vendor 'Microsoft'"
"Update vendor Dell with a new phone number"
```

## 🔧 **Statuses and Data Types**

### **Asset Statuses:**
- `in_use` - In use
- `in_stock` - In stock
- `under_maintenance` - Under maintenance
- `retired` - Retired
- `lost` - Lost
- `stolen` - Stolen

### **CI Statuses:**
- `active` - Active
- `inactive` - Inactive
- `under_maintenance` - Under maintenance
- `retired` - Retired

### **Contract Statuses:**
- `active` - Active
- `expired` - Expired
- `pending` - Pending
- `terminated` - Terminated

### **Purchase Order Statuses:**
- `draft` - Draft
- `pending_approval` - Pending approval
- `approved` - Approved
- `ordered` - Ordered
- `received` - Received
- `cancelled` - Cancelled

## 🎯 **Real-World Usage Examples**

### **Infrastructure Management:**
```
"Create a Configuration Item for the new database server 'DB-SRV-001'"
"Get list of all active network devices"
"Create an asset for a new switch and assign it to the data center"
```

### **Software Management:**
```
"Create a software license for Adobe Creative Suite with 50 licenses"
"Check the remaining number of licenses for Microsoft Office"
"Update the Adobe license with a new expiration date"
```

### **Contract Management:**
```
"Create a maintenance contract with vendor Dell for 3 years"
"Get list of contracts expiring in the next 30 days"
"Update the Microsoft contract with a new value"
```

### **Procurement Management:**
```
"Create a purchase order for 20 monitors from vendor HP"
"Check the status of purchase order PO-2024-001"
"Update the PO with a new delivery date"
```

## 🔍 **Search and Reporting**

All tools support:
- **Pagination** - Limit the number of results
- **Filtering** - Filter by various criteria
- **Search** - Search by keywords
- **Sorting** - Sort results

## 📊 **AI Integration**

The MCP server allows the AI assistant to:
- **Automatically create** CIs, assets, licenses, contracts
- **Track** status and lifecycle of items
- **Report** on inventory and compliance
- **Manage** relationships between items
- **Optimize** procurement and vendor management

## 🚀 **Benefits**

1. **Centralized Management** - Centralized management of all configuration items
2. **Compliance Tracking** - Track compliance with licenses and contracts
3. **Asset Lifecycle** - Manage the entire lifecycle of assets
4. **Vendor Management** - Efficiently manage vendor relationships
5. **Procurement Automation** - Automate the procurement process
6. **Reporting & Analytics** - CMDB data reporting and analysis

With these CMDB features, the MCP server provides a complete solution for managing the entire IT infrastructure through an AI assistant!