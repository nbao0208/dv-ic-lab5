"""
dataset_creator.py
Tạo tất cả file CSV cần thiết cho dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from pathlib import Path

def create_dashboard_dataset():
    """Tạo và lưu toàn bộ dataset vào CSV files"""
    
    base_path = Path(__file__).parent
    random.seed(42)  # Để kết quả reproducible
    np.random.seed(42)
    
    print("🔄 Đang tạo dataset...")
    
    # =========================================================================
    # 1. KPI DATA
    # =========================================================================
    kpi_data = {
        'metric': [
            'Days Left EOQ', 'QTD Transactions', 'QTD Active Clients', 
            'QTD SAMs', 'QTD Sales', 'Admins', 'Designers', 'Servers'
        ],
        'value': [76, 90, 3, 37, 726225, 170, 109, 16],
        'unit': ['days', 'count', 'count', 'count', 'USD', 'count', 'count', 'count'],
        'icon': ['⏱️', '📝', '👥', '📋', '💰', '‍💼', '🎨', '🖥️']
    }
    kpi_df = pd.DataFrame(kpi_data)
    kpi_df.to_csv(base_path / 'kpi_data.csv', index=False)
    print("  ✓ kpi_data.csv")
    
    # =========================================================================
    # 2. RUNNING TOTALS DATA (Weekly trends for multiple quarters)
    # =========================================================================
    weeks = list(range(0, 15))
    running_totals_data = []
    
    quarter_configs = [
        {'type': 'Current', 'base': 100000, 'growth': 50000, 'color_order': 0},
        {'type': 'Previous', 'base': 90000, 'growth': 45000, 'color_order': 1},
        {'type': 'This Q, previous year', 'base': 80000, 'growth': 30000, 'color_order': 2},
    ]
    
    # Thêm các quarter "Older" (nhiều đường mờ)
    for i in range(10):
        quarter_configs.append({
            'type': 'Older',
            'base': random.randint(30000, 70000),
            'growth': random.randint(15000, 35000),
            'color_order': 3 + i
        })
    
    for config in quarter_configs:
        for week in weeks:
            noise = random.randint(-15000, 15000)
            value = config['base'] + (week * config['growth']) + noise
            value = max(0, value)
            
            running_totals_data.append({
                'week': week,
                'value': round(value, 2),
                'quarter_type': config['type'],
                'quarter_id': f"Q{config['color_order'] + 1}"
            })
    
    # Thêm điểm đánh dấu cho 2016 Q2
    running_totals_data.append({
        'week': 7,
        'value': 726000,
        'quarter_type': 'Current',
        'quarter_id': '2016 Q2',
        'is_annotation': True
    })
    
    running_totals_df = pd.DataFrame(running_totals_data)
    running_totals_df.to_csv(base_path / 'running_totals_data.csv', index=False)
    print("  ✓ running_totals_data.csv")
    
    # =========================================================================
    # 3. QUARTERLY METRICS DATA (2012-2016)
    # =========================================================================
    years = [2012, 2013, 2014, 2015, 2016]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    metrics = ['Amount', 'Transactions', 'Active clients', 'Active SAMs', 
               'Designers', 'Admins', 'Servers']
    
    quarterly_metrics_data = []
    
    # Base values cho từng metric
    base_values = {
        'Amount': 200000,
        'Transactions': 25,
        'Active clients': 1,
        'Active SAMs': 5,
        'Designers': 30,
        'Admins': 50,
        'Servers': 5
    }
    
    for year in years:
        for quarter in quarters:
            for metric in metrics:
                # Year growth multiplier
                year_mult = 1 + (year - 2012) * 0.4
                
                # Quarter multiplier (Q4 thường cao nhất)
                quarter_mult = {'Q1': 0.85, 'Q2': 0.95, 'Q3': 1.0, 'Q4': 1.2}[quarter]
                
                # Base value
                base = base_values[metric]
                
                # Calculate value with some randomness
                value = base * year_mult * quarter_mult * random.uniform(0.85, 1.15)
                
                # Product type
                if year >= 2015 and quarter in ['Q3', 'Q4']:
                    product = random.choice(['Product 1', 'Product 2'])
                else:
                    product = 'All'
                
                # License type
                if year >= 2015:
                    license_type = random.choice(['Invoice', 'Maintenance Renewal', 'All'])
                else:
                    license_type = 'All'
                
                quarterly_metrics_data.append({
                    'year': year,
                    'quarter': quarter,
                    'period': f"{year} {quarter}",
                    'metric': metric,
                    'value': round(value, 2),
                    'product': product,
                    'license_type': license_type
                })
    
    quarterly_metrics_df = pd.DataFrame(quarterly_metrics_data)
    quarterly_metrics_df.to_csv(base_path / 'quarterly_metrics_data.csv', index=False)
    print("  ✓ quarterly_metrics_data.csv")
    
    # =========================================================================
    # 4. ORDERS DATA (Last 5 orders)
    # =========================================================================
    companies = ['Company 1', 'Company 2', 'Company 3']
    orders_data = []
    
    for i in range(5):
        orders_data.append({
            'order_id': i + 1,
            'company': companies[i % len(companies)],
            'amount': round(random.uniform(1299, 1300), 2),
            'date': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
            'product': random.choice(['Product 1', 'Product 2']),
            'status': 'Completed'
        })
    
    orders_df = pd.DataFrame(orders_data)
    orders_df.to_csv(base_path / 'orders_data.csv', index=False)
    print("  ✓ orders_data.csv")
    
    # =========================================================================
    # 5. COUNTRY PERFORMANCE DATA
    # =========================================================================
    country_data = [
        {'country': 'UK', 'country_name': 'United Kingdom', 'amount': 451000},
        {'country': 'NO', 'country_name': 'Norway', 'amount': 241000},
        {'country': 'GR', 'country_name': 'Greece', 'amount': 22000},
        {'country': 'IT', 'country_name': 'Italy', 'amount': 8000},
        {'country': 'SP', 'country_name': 'Spain', 'amount': 2000},
        {'country': 'LU', 'country_name': 'Luxembourg', 'amount': 2000},
    ]
    
    # Add some variation
    for row in country_data:
        row['amount'] = row['amount'] * random.uniform(0.95, 1.05)
        row['currency'] = 'USD'
    
    country_df = pd.DataFrame(country_data)
    country_df.to_csv(base_path / 'country_data.csv', index=False)
    print("  ✓ country_data.csv")
    
    # =========================================================================
    # 6. FILTER OPTIONS (JSON)
    # =========================================================================
    import json
    filters = {
        'products': ['Product 1', 'Product 2', 'All'],
        'license_types': ['All', 'Invoice', 'Maintenance Renewal'],
        'regions': ['All', 'Europe', 'North America', 'Asia Pacific'],
        'comparison_types': ['Current', 'Previous', 'This Q, previous year', 'Older']
    }
    
    with open(base_path / 'filters.json', 'w') as f:
        json.dump(filters, f, indent=2)
    print("  ✓ filters.json")
    
    print("\n✅ Tất cả file CSV đã được tạo thành công!")
    print(f"📁 Vị trí: {base_path}")
    
    return base_path


if __name__ == "__main__":
    create_dashboard_dataset()