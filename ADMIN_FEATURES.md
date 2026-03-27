# Admin Management Features

## 🎯 **Overview**

ServiceDesk Plus MCP Server provides full support for system administration (Admin Management) functions including site management, user groups, users, technicians, permissions, departments, locations, and system settings.

## 🏢 **Site Management**

### **Features:**
- ✅ **CRUD Operations** - Create, read, update, delete sites
- ✅ **Site Types** - Support for site types: headquarters, branch_office, data_center, warehouse, retail_store, manufacturing_plant
- ✅ **Location Details** - Address, city, country, zip code
- ✅ **Contact Information** - Phone number, contact email
- ✅ **Filtering** - Filter by site type, status

### **Tools (6 tools):**
- `list_sites` - Get list of sites with filters
- `get_site` - Get site details
- `create_site` - Create a new site
- `update_site` - Update site information
- `delete_site` - Delete a site
- `get_site_types` - Get list of site types

### **Usage Examples:**
```
"Create a new site 'Branch Office Hanoi' with type branch_office"
"Get list of all data centers"
"Update the address for site 'Headquarters'"
"Delete site 'Old Warehouse' that is no longer in use"
```

## 👥 **User Group Management**

### **Features:**
- ✅ **CRUD Operations** - Create, read, update, delete user groups
- ✅ **Group Types** - Support for group types: department, project, location_based, role_based, custom
- ✅ **Permission Management** - Assign and manage permissions for groups
- ✅ **Site Association** - Link groups with sites
- ✅ **Manager Assignment** - Assign a manager to groups

### **Tools (8 tools):**
- `list_user_groups` - Get list of user groups
- `get_user_group` - Get user group details
- `create_user_group` - Create a new user group
- `update_user_group` - Update a user group
- `delete_user_group` - Delete a user group
- `get_group_types` - Get list of group types
- `get_group_permissions` - Get group permissions
- `update_group_permissions` - Update group permissions

### **Usage Examples:**
```
"Create a user group 'IT Support Team' with type department"
"Assign 'read' permissions for tickets and 'write' for assets to group 'IT Support'"
"Get list of all user groups in site 'Headquarters'"
"Update the manager for group 'Software Development'"
```

## 👤 **User & Technician Management**

### **Features:**
- ✅ **CRUD Operations** - Create, read, update, delete users and technicians
- ✅ **Role Management** - Support for roles: admin, manager, technician, user, viewer
- ✅ **Status Management** - Manage statuses: active, inactive, locked, pending_activation
- ✅ **Site Assignment** - Assign users/technicians to sites
- ✅ **Department Assignment** - Assign to departments
- ✅ **Skills & Specializations** - Manage skills and specializations (for technicians)

### **Tools (12 tools):**
- `list_admin_users` - Get list of admin users
- `get_admin_user` - Get admin user details
- `create_admin_user` - Create a new admin user
- `update_admin_user` - Update an admin user
- `delete_admin_user` - Delete an admin user
- `list_admin_technicians` - Get list of admin technicians
- `get_admin_technician` - Get admin technician details
- `create_admin_technician` - Create a new admin technician
- `update_admin_technician` - Update an admin technician
- `delete_admin_technician` - Delete an admin technician
- `get_user_roles` - Get list of user roles
- `get_technician_roles` - Get list of technician roles

### **Usage Examples:**
```
"Create an admin user 'john.doe' with role technician and assign to site 'Headquarters'"
"Create a technician 'jane.smith' with skills 'network, security' and specializations 'firewall'"
"Update the role of user 'mike.wilson' from user to manager"
"Get list of all technicians in department 'IT Support'"
"Lock user 'inactive.user' due to inactivity"
```

## 🔐 **Permission Management**

### **Features:**
- ✅ **Permission Levels** - Support for levels: none, read, write, admin
- ✅ **Role-based Permissions** - Manage permissions by roles
- ✅ **User-specific Permissions** - Assign individual permissions to each user
- ✅ **Permission Inheritance** - Inherit permissions from roles and groups

### **Tools (5 tools):**
- `get_permissions` - Get list of all permissions
- `get_role_permissions` - Get role permissions
- `update_role_permissions` - Update role permissions
- `get_user_permissions` - Get user permissions
- `update_user_permissions` - Update user permissions

### **Usage Examples:**
```
"Get list of all available permissions in the system"
"Assign 'admin' permission for tickets and 'write' for assets to role 'manager'"
"Update permissions for user 'john.doe' with 'read' for reports"
"Check current permissions of role 'technician'"
```

## 🏛️ **Department Management**

### **Features:**
- ✅ **CRUD Operations** - Create, read, update, delete departments
- ✅ **Department Types** - Support for different department types
- ✅ **Site Association** - Link departments with sites
- ✅ **Manager Assignment** - Assign a manager to departments
- ✅ **Organizational Structure** - Build organizational structure

### **Tools (6 tools):**
- `list_departments` - Get list of departments
- `get_department` - Get department details
- `create_department` - Create a new department
- `update_department` - Update a department
- `delete_department` - Delete a department
- `get_department_types` - Get list of department types

### **Usage Examples:**
```
"Create a department 'Software Development' with type IT"
"Assign manager 'tech.lead' to department 'Development'"
"Get list of all departments in site 'Headquarters'"
"Update the description for department 'Quality Assurance'"
"Delete department 'Legacy Support' that is no longer active"
```

## 📍 **Location Management**

### **Features:**
- ✅ **CRUD Operations** - Create, read, update, delete locations
- ✅ **Location Types** - Support for different location types
- ✅ **Site Association** - Link locations with sites
- ✅ **Physical Details** - Address, floor, room
- ✅ **Hierarchical Structure** - Hierarchical location structure

### **Tools (6 tools):**
- `list_locations` - Get list of locations
- `get_location` - Get location details
- `create_location` - Create a new location
- `update_location` - Update a location
- `delete_location` - Delete a location
- `get_location_types` - Get list of location types

### **Usage Examples:**
```
"Create a location 'Server Room A' with type data_center in site 'Headquarters'"
"Get list of all locations on floor 3"
"Update room information for location 'Conference Room 1'"
"Create a location 'Warehouse Section B' with type storage"
"Delete location 'Old Office Space' that is no longer in use"
```

## ⚙️ **System Settings**

### **Features:**
- ✅ **System Configuration** - General system settings
- ✅ **Email Settings** - Email notification configuration
- ✅ **Notification Settings** - Notification configuration
- ✅ **Security Settings** - Security configuration
- ✅ **Performance Settings** - Performance optimization

### **Tools (6 tools):**
- `get_system_settings` - Get system settings
- `update_system_settings` - Update system settings
- `get_email_settings` - Get email settings
- `update_email_settings` - Update email settings
- `get_notification_settings` - Get notification settings
- `update_notification_settings` - Update notification settings

### **Usage Examples:**
```
"Get current system settings"
"Update email settings to send ticket notifications"
"Configure notification settings for high priority tickets"
"Check email settings for automated reports"
"Update system settings for performance optimization"
```

## 🔄 **Workflow Integration**

### **Features:**
- ✅ **Automated User Provisioning** - Automatically create users based on rules
- ✅ **Role-based Access Control** - Access control by roles
- ✅ **Permission Inheritance** - Automatic permission inheritance
- ✅ **Site-based Organization** - Organization by sites
- ✅ **Department Hierarchy** - Hierarchical department structure

### **Workflow Examples:**
```
"When creating a new user, automatically assign to the corresponding department and site"
"When changing a user's role, automatically update permissions"
"When creating a new site, automatically create default locations and departments"
"When creating a department, automatically create the corresponding user group"
```

## 📊 **Reporting & Analytics**

### **Features:**
- ✅ **User Activity Reports** - User activity reports
- ✅ **Permission Audit** - Permission auditing
- ✅ **Site Utilization** - Site utilization
- ✅ **Department Performance** - Department performance
- ✅ **System Health** - System health status

### **Report Examples:**
```
"Report on the number of users by roles and sites"
"Audit permissions of all admin users"
"Report on site utilization"
"Analyze department performance"
"Audit log of permission changes"
```

## 🛡️ **Security Features**

### **Features:**
- ✅ **Role-based Security** - Role-based security
- ✅ **Permission Validation** - Permission validation
- ✅ **Audit Logging** - Change logging
- ✅ **Access Control** - Access control
- ✅ **Data Protection** - Data protection

### **Security Best Practices:**
```
"Always use the principle of least privilege"
"Regular audit of permissions and access rights"
"Log all admin activities"
"Regular review of user roles and permissions"
"Backup and recovery of admin configurations"
```

## 🚀 **Benefits**

1. **Centralized Administration** - Centralized administration of the entire system
2. **Role-based Access Control** - Access control by roles
3. **Organizational Structure** - Clear organizational structure
4. **Automated Workflows** - Process automation
5. **Security Compliance** - Security compliance
6. **Scalability** - Scalability
7. **Audit Trail** - Change history tracking

## 📈 **Performance**

- **Async Operations** - All operations are async
- **Batch Processing** - Batch processing
- **Caching** - Cache frequently used data
- **Optimized Queries** - Optimized queries
- **Connection Pooling** - Efficient connection management

---

**Total Admin Tools:** 49 tools
**Coverage:** ✅ Complete Admin Management
**Integration:** ✅ Full CMDB Integration
**Security:** ✅ Role-based Access Control