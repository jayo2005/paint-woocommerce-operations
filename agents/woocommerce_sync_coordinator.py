#!/usr/bin/env python3
"""
WooCommerce Sync Coordinator Agent - Manages e-commerce integration and synchronization
This agent handles the critical connection between Odoo and the WooCommerce online store
"""

import os
import sys
import json
import logging
from github import Github
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WooCommerceSyncCoordinator:
    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.cross_repo_token = os.environ.get('CROSS_REPO_TOKEN', self.github_token)
        self.module_path = '/home/jason/odoo17_custom_addons/integration_woocommerce'
        
        # Module capabilities based on code analysis
        self.module_info = {
            'type': 'Commercial module from VentorTech',
            'dependencies': ['integration', 'queue_job', 'sale_management'],
            'architecture': 'Job queue-based asynchronous processing',
            'key_features': {
                'products': 'Bidirectional sync with variant support',
                'orders': 'Real-time webhook import',
                'inventory': 'Stock level synchronization',
                'customers': 'B2B/B2C customer management'
            }
        }
        
        # Paint business context
        self.business_context = {
            'products': 'Paint products with color variants and sizes',
            'formulas': 'Tikkurila formulas must sync correctly',
            'customers': 'B2B paint shops and B2C consumers',
            'inventory': 'Critical for paint availability'
        }
    
    def analyze_request(self, issue_title, issue_body):
        """Analyze requests and provide WooCommerce-specific guidance"""
        title_lower = issue_title.lower()
        body_lower = issue_body.lower()
        
        # Product sync questions
        if any(word in title_lower + ' ' + body_lower for word in ['product', 'sync', 'variant', 'color']):
            return self.handle_product_sync_request(issue_title, issue_body)
        
        # Order/webhook questions
        elif any(word in title_lower + ' ' + body_lower for word in ['order', 'webhook', 'real-time']):
            return self.handle_order_sync_request(issue_title, issue_body)
        
        # Job queue questions
        elif any(word in title_lower + ' ' + body_lower for word in ['job', 'queue', 'async', 'background']):
            return self.handle_job_queue_request(issue_title, issue_body)
        
        # Configuration questions
        elif any(word in title_lower + ' ' + body_lower for word in ['config', 'setup', 'webhook', 'api']):
            return self.handle_configuration_request(issue_title, issue_body)
        
        # General request
        else:
            return self.general_response(issue_title)
    
    def handle_product_sync_request(self, title, body):
        """Guide product synchronization setup"""
        return f"""## 🛒 WooCommerce Sync Coordinator Response - Product Synchronization

I'll help you set up product synchronization between Odoo and WooCommerce.

### Product Sync Capabilities:

1. **Paint Product Structure**
   - Simple products: Single paint products
   - Variable products: Paint with color/size variants
   - Bundles: Paint kits and accessories
   - Custom attributes for Tikkurila formulas

2. **Synchronization Process**
   ```python
   # Module location: {self.module_path}
   # Process flow:
   # 1. Configure field mappings
   # 2. Set sync direction (Odoo→WC, WC→Odoo, or both)
   # 3. Enable job queue for bulk operations
   # 4. Schedule or trigger sync
   ```

3. **Paint-Specific Mappings**
   - Product name → WooCommerce title
   - Tikkurila color code → Custom attribute
   - Paint size variants → Variable product options
   - Formula info → Product description/meta
   - Stock levels → Inventory sync

4. **Job Queue Processing**
   - Bulk imports run in background
   - Progress tracking via job dashboard
   - Error handling and retry logic
   - Avoids timeout issues

### Configuration Steps:
1. **Field Mapping**: Map Odoo fields to WooCommerce
2. **Variant Setup**: Configure color/size attributes
3. **Image Sync**: Product images and color swatches
4. **Pricing**: Handle B2B/B2C price lists
5. **Categories**: Map paint categories

### Critical for Paint Business:
- Ensure Tikkurila color codes sync correctly
- Maintain formula integrity in descriptions
- Handle paint size variants properly
- Keep stock levels accurate

---
*Synchronizing paint products between Odoo and online store*"""
    
    def handle_order_sync_request(self, title, body):
        """Handle order synchronization queries"""
        return f"""## 🛒 WooCommerce Sync Coordinator Response - Order Management

### Order Synchronization Features:

1. **Real-Time Order Import**
   - Webhook triggers on order creation/update
   - Immediate processing in Odoo
   - No delay for customer orders
   - Automatic customer creation

2. **Webhook Configuration**
   ```
   WooCommerce → Webhook → Odoo Controller → Job Queue → Order Creation
   ```
   - Webhook URL: `https://[odoo-domain]/woocommerce/webhook/order`
   - Events: Order created, updated, completed
   - Security: Webhook secret validation

3. **Order Processing Flow**
   - Order received via webhook
   - Job queued for processing
   - Customer matched/created
   - Products mapped to Odoo
   - Order created with proper workflow

4. **Paint Order Specifics**
   - Custom color selections
   - Formula requirements captured
   - B2B customer pricing applied
   - Delivery instructions preserved

### Job Queue Benefits:
- Non-blocking order processing
- Retry failed imports
- Bulk order handling
- Performance optimization

### Configuration Requirements:
1. Enable webhooks in WooCommerce
2. Configure webhook secret
3. Set order field mappings
4. Define order workflow
5. Test with sample orders

### Error Handling:
- Failed orders queued for retry
- Email notifications on errors
- Manual intervention options
- Detailed error logs

---
*Ensuring paint orders flow seamlessly from web to warehouse*"""
    
    def handle_job_queue_request(self, title, body):
        """Explain job queue functionality"""
        return f"""## 🛒 WooCommerce Sync Coordinator Response - Job Queue System

### Understanding the Job Queue Architecture:

1. **What is Job Queue?**
   - Asynchronous task processing system
   - Based on OCA's `queue_job` module
   - Prevents timeouts on heavy operations
   - Allows parallel processing

2. **How It Works**
   ```
   Trigger → Create Job → Queue → Worker → Execute → Complete/Retry
   ```
   - Jobs run in background
   - Multiple workers possible
   - Automatic retry on failure
   - Progress tracking

3. **WooCommerce Integration Jobs**
   - **Product Import/Export**: Bulk product sync
   - **Order Import**: Process webhook data
   - **Stock Update**: Inventory synchronization
   - **Customer Sync**: B2B/B2C customer data

4. **Job Channels**
   ```python
   # Defined channels:
   - root.woocommerce
   - root.woocommerce.product
   - root.woocommerce.order
   ```
   - Priority-based processing
   - Resource allocation control
   - Prevents system overload

5. **Monitoring Jobs**
   - Menu: Settings → Technical → Job Queue
   - View pending/failed/done jobs
   - Retry failed jobs manually
   - Check execution logs

### Benefits for Paint Business:
- Import thousands of products without timeout
- Process orders immediately via webhooks
- Update stock levels in batches
- Handle peak sales periods

### Troubleshooting:
- Check job queue dashboard
- Verify worker processes running
- Review failed job logs
- Adjust job priorities if needed

---
*Asynchronous processing for reliable e-commerce integration*"""
    
    def handle_configuration_request(self, title, body):
        """Guide module configuration"""
        return f"""## 🛒 WooCommerce Sync Coordinator Response - Configuration Guide

### Initial Setup Steps:

1. **WooCommerce API Configuration**
   ```
   Settings → Integrations → WooCommerce
   ```
   - Store URL: https://your-store.com
   - Consumer Key: wc_xxxxxxxxxx
   - Consumer Secret: cs_xxxxxxxxxx
   - API Version: wc/v3 (recommended)

2. **Webhook Setup**
   - Go to WooCommerce → Settings → Advanced → Webhooks
   - Create webhooks for:
     - Order created
     - Order updated
     - Product updated (if bidirectional)
   - Webhook URL format:
     ```
     https://[odoo-url]/woocommerce/webhook/[type]
     ```

3. **Field Mapping Configuration**
   - Map Odoo fields to WooCommerce attributes
   - Special mappings for paint products:
     - Tikkurila codes → Custom attributes
     - Paint sizes → Variations
     - B2B prices → Wholesale prices

4. **Job Queue Setup**
   ```bash
   # Start job queue workers
   python odoo-bin worker --db-filter=^your_db$
   ```
   - Configure worker count
   - Set memory limits
   - Enable auto-restart

5. **Synchronization Settings**
   - Sync direction (one-way or bidirectional)
   - Automatic sync intervals
   - Manual sync triggers
   - Conflict resolution rules

### Paint-Specific Configuration:
- Enable variant sync for colors/sizes
- Map formula fields to product meta
- Configure B2B customer groups
- Set inventory sync for paint stock

### Testing Checklist:
✓ API connection test
✓ Webhook delivery test
✓ Sample product sync
✓ Test order creation
✓ Inventory update verification

---
*Configuring reliable paint product synchronization*"""
    
    def general_response(self, title):
        """General response for other queries"""
        return f"""## 🛒 WooCommerce Sync Coordinator Response

I manage the integration between Odoo and WooCommerce for the paint business.

### Current Request: {title}

### Module Capabilities:
1. **Product Synchronization**
   - Simple and variable products
   - Paint colors and sizes
   - Tikkurila formula data
   - Image synchronization

2. **Order Management**
   - Real-time webhook import
   - B2B/B2C customer handling
   - Automatic workflow triggers
   - Payment status sync

3. **Inventory Control**
   - Stock level updates
   - Multi-warehouse support
   - Low stock notifications
   - Batch processing

4. **Job Queue System**
   - Asynchronous processing
   - Bulk operations
   - Error recovery
   - Performance optimization

### Architecture Overview:
- Module: `integration_woocommerce`
- Dependencies: `queue_job`, `integration`
- Processing: Webhook + Job Queue
- Direction: Bidirectional sync

### Business Impact:
This integration ensures your paint products are accurately represented online, orders flow seamlessly to Odoo, and inventory stays synchronized across channels.

How can I help with your specific WooCommerce integration need?

---
*E-commerce integration for paint manufacturing excellence*"""
    
    def process_issues(self):
        """Process GitHub issues requiring WooCommerce expertise"""
        try:
            if not self.github_token:
                logger.error("GITHUB_TOKEN not set")
                return
            
            g = Github(self.github_token)
            cross_g = Github(self.cross_repo_token)
            
            # Check our own repository
            repo = g.get_repo('jayo2005/paint-woocommerce-operations')
            for issue in repo.get_issues(state='open'):
                if not self.already_responded(issue):
                    response = self.analyze_request(issue.title, issue.body)
                    issue.create_comment(response)
                    logger.info(f"Responded to issue #{issue.number}")
            
            # Monitor other repos for WooCommerce/e-commerce requests
            repos_to_monitor = [
                'jayo2005/paint-odoo-operations',
                'jayo2005/paint-project-orchestration',
                'jayo2005/paint-wordpress-operations'
            ]
            
            for repo_name in repos_to_monitor:
                try:
                    other_repo = cross_g.get_repo(repo_name)
                    for issue in other_repo.get_issues(state='open'):
                        # Check if issue mentions WooCommerce or e-commerce
                        if any(keyword in issue.title.lower() + ' ' + issue.body.lower() 
                               for keyword in ['woocommerce', 'ecommerce', 'e-commerce', 'online store', 
                                               'webhook', 'shop sync', 'product sync']):
                            if not self.already_responded(issue):
                                response = self.analyze_request(issue.title, issue.body)
                                issue.create_comment(response)
                                logger.info(f"Responded to {repo_name} issue #{issue.number}")
                except Exception as e:
                    logger.error(f"Error monitoring {repo_name}: {str(e)}")
        
        except Exception as e:
            logger.error(f"Agent error: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
    
    def already_responded(self, issue):
        """Check if we already responded to this issue"""
        for comment in issue.get_comments():
            if 'WooCommerce Sync Coordinator' in comment.body:
                return True
        return False

def main():
    """Main entry point"""
    agent = WooCommerceSyncCoordinator()
    logger.info("WooCommerce Sync Coordinator starting - Managing e-commerce integration")
    agent.process_issues()

if __name__ == "__main__":
    main()