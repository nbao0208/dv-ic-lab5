"""
pages/1_Dashboard.py
Dashboard Báo Cáo Doanh Số Bán Giấy Phép Phần Mềm
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json

# =============================================================================
# CẤU HÌNH TRANG
# =============================================================================
st.set_page_config(
    page_title="Dashboard - Báo Cáo Doanh Số Giấy Phép Phần Mềm",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS TÙY CHỈNH
# =============================================================================
st.markdown("""
<style>
    /* Container chính */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Thẻ metric */
    .stMetric {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #e9ecef;
    }
    
    /* Label metric */
    .stMetric label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #495057;
    }
    
    /* Giá trị metric */
    .stMetric div[data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
        color: #212529;
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #212529;
        font-weight: 700;
    }
    
    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HÀM LOAD DỮ LIỆU
# =============================================================================
@st.cache_data
def load_data():
    """
    Load tất cả dữ liệu từ các file CSV
    
    Returns:
        dict: Dictionary chứa tất cả các dataframe
    """
    base_path = Path(__file__).parent.parent
    
    try:
        # Load từng file CSV
        kpi_df = pd.read_csv(base_path / 'kpi_data.csv')
        running_totals_df = pd.read_csv(base_path / 'running_totals_data.csv')
        quarterly_metrics_df = pd.read_csv(base_path / 'quarterly_metrics_data.csv')
        orders_df = pd.read_csv(base_path / 'orders_data.csv')
        country_df = pd.read_csv(base_path / 'country_data.csv')
        
        # Load tùy chọn filter
        with open(base_path / 'filters.json', 'r', encoding='utf-8') as f:
            filters = json.load(f)
        
        return {
            'kpi': kpi_df,
            'running_totals': running_totals_df,
            'quarterly_metrics': quarterly_metrics_df,
            'orders': orders_df,
            'country': country_df,
            'filters': filters
        }
    
    except FileNotFoundError as e:
        st.error(f"❌ Không tìm thấy file: {e}")
        st.info("💡 Vui lòng chạy `python dataset_creator.py` trước để tạo dữ liệu")
        return None
    
    except Exception as e:
        st.error(f"❌ Lỗi khi load dữ liệu: {e}")
        return None


# =============================================================================
# HÀM HỖ TRỢ
# =============================================================================
def format_currency(value, currency='USD'):
    """Format số tiền thành chuỗi dễ đọc"""
    if value >= 1000000:
        return f"${value/1000000:.2f}M"
    elif value >= 1000:
        return f"${value/1000:.0f}K"
    else:
        return f"${value:,.0f}"


def format_number(value):
    """Format số thành chuỗi với dấu phẩy"""
    return f"{value:,.0f}"


# =============================================================================
# ỨNG DỤNG CHÍNH
# =============================================================================
def main():
    # Load dữ liệu
    data = load_data()
    
    if data is None:
        st.stop()
    
    # =========================================================================
    # THANH ĐIỀU HƯỚNG
    # =========================================================================
    col_nav1, col_nav2, col_nav3 = st.columns([1, 10, 1])
    with col_nav1:
        if st.button("🏠 Trang Chủ", use_container_width=True, key="nav_home"):
            st.switch_page("home.py")
    
    # =========================================================================
    # SIDEBAR - BỘ LỌC
    # =========================================================================
    with st.sidebar:
        st.header("🔍 Bộ Lọc Dữ Liệu")
        st.markdown("---")
        
        # Bộ lọc sản phẩm
        product_filter = st.selectbox(
            "Sản Phẩm",
            options=data['filters']['products'],
            index=data['filters']['products'].index('All') if 'All' in data['filters']['products'] else 0
        )
        
        # Bộ lọc loại license
        license_filter = st.selectbox(
            "Loại Giấy Phép",
            options=data['filters']['license_types'],
            index=0
        )
        
        # Bộ lọc khu vực
        region_filter = st.selectbox(
            "Khu Vực",
            options=data['filters']['regions'],
            index=0
        )
        
        st.markdown("---")
        
        # Hộp thông tin
        st.info("""
        **💡 Mẹo Sử Dụng:**
        - Sử dụng bộ lọc để lọc dữ liệu theo nhu cầu
        - Di chuột vào biểu đồ để xem chi tiết
        - Dữ liệu được cập nhật tự động
        """)
        
        # Thời gian cập nhật
        st.markdown("---")
        st.caption(f"Cập nhật lần cuối: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # =========================================================================
    # NỘI DUNG CHÍNH
    # =========================================================================
    
    # Tiêu đề
    st.title("📈 BÁO CÁO DOANH SỐ BÁN GIẤY PHÉP PHẦN MỀM")
    st.markdown("---")
    
    # =====================================================================
    # HÀNG 1: CÁC CHỈ SỐ KPI
    # =====================================================================
    st.subheader("📌 Các Chỉ Số Hiệu Suất Chính (KPI)")
    
    kpi_df = data['kpi']
    kpi_cols = st.columns(8)
    
    # Mapping tên tiếng Việt cho các metric
    kpi_names_vi = {
        'Days Left EOQ': 'Ngày Còn Lại Cuối Quý',
        'QTD Transactions': 'Giao Dịch Quý',
        'QTD Active Clients': 'Khách Hàng Hoạt Động',
        'QTD SAMs': 'Quản Lý Tài Sản',
        'QTD Sales': 'Doanh Thu Quý',
        'Admins': 'Quản Trị Viên',
        'Designers': 'Thiết Kế Viên',
        'Servers': 'Máy Chủ'
    }
    
    kpi_icons = {
        'Days Left EOQ': '⏱️',
        'QTD Transactions': '📝',
        'QTD Active Clients': '👥',
        'QTD SAMs': '📋',
        'QTD Sales': '💰',
        'Admins': '👨‍💼',
        'Designers': '🎨',
        'Servers': '🖥️'
    }
    
    for i, (_, row) in enumerate(kpi_df.iterrows()):
        with kpi_cols[i]:
            # Format giá trị theo đơn vị
            metric_name = row['metric']
            vi_name = kpi_names_vi.get(metric_name, metric_name)
            icon = kpi_icons.get(metric_name, '📊')
            
            if row['unit'] == 'USD':
                value_display = f"${row['value']:,.0f}"
            elif row['unit'] == 'days':
                value_display = f"{int(row['value'])}"
            else:
                value_display = f"{int(row['value']):,}"
            
            st.metric(
                label=f"{icon} {vi_name}",
                value=value_display,
                delta=None
            )
    
    st.markdown("---")
    
    # =====================================================================
    # HÀNG 2: BIỂU ĐỒ XU HƯỚNG + CÁC PANEL BÊN
    # =====================================================================
    col_main, col_side = st.columns([2.5, 1])
    
    with col_main:
        st.subheader("📊 Tổng Tích Lũy Theo Tuần")
        
        running_df = data['running_totals'].copy()
        
        # Mapping màu sắc
        color_map = {
            'Current': '#8B4513',
            'Previous': '#E9967A',
            'This Q, previous year': '#DDA0DD',
            'Older': '#D3D3D3'
        }
        
        # Mapping tên tiếng Việt
        quarter_type_vi = {
            'Current': 'Quý Hiện Tại',
            'Previous': 'Quý Trước',
            'This Q, previous year': 'Cùng Kỳ Năm Ngoái',
            'Older': 'Các Quý Cũ'
        }
        
        # Tạo biểu đồ
        fig_running = go.Figure()
        
        # Vẽ từng loại quý
        for qt in ['Current', 'Previous', 'This Q, previous year', 'Older']:
            subset = running_df[running_df['quarter_type'] == qt]
            
            # Group theo quarter_id cho loại Older
            if qt == 'Older':
                for qid in subset['quarter_id'].unique():
                    q_subset = subset[subset['quarter_id'] == qid]
                    fig_running.add_trace(go.Scatter(
                        x=q_subset['week'],
                        y=q_subset['value'],
                        mode='lines',
                        name=f'{quarter_type_vi[qt]}',
                        line=dict(color=color_map.get(qt, 'gray'), width=1.5),
                        opacity=0.3,
                        showlegend=False,
                        hoverinfo='skip'
                    ))
            else:
                # Tổng hợp cho các loại không phải Older
                agg_subset = subset.groupby('week')['value'].mean().reset_index()
                fig_running.add_trace(go.Scatter(
                    x=agg_subset['week'],
                    y=agg_subset['value'],
                    mode='lines',
                    name=quarter_type_vi[qt],
                    line=dict(color=color_map.get(qt, 'gray'), width=3),
                    opacity=0.9 if qt == 'Current' else 0.6,
                    hovertemplate='<b>%{fullData.name}</b><br>Tuần: %{x}<br>Giá trị: $%{y:,.0f}<extra></extra>'
                ))
        
        # Thêm chú thích cho 2016 Q2
        fig_running.add_annotation(
            x=7,
            y=726000,
            text="2016 Q2<br>$726K",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#8B4513",
            bgcolor="white",
            bordercolor="#8B4513",
            borderwidth=1,
            borderpad=4
        )
        
        fig_running.update_layout(
            height=550,
            xaxis_title="Số Tuần",
            yaxis_title="Giá Trị",
            hovermode='x unified',
            legend_title="So Sánh Với?",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            template="plotly_white",
            yaxis=dict(
                tickformat=',.0f',
                tickprefix='$',
                range=[0, 1500000]
            ),
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=2
            ),
            margin=dict(l=60, r=40, t=60, b=60)
        )
        
        st.plotly_chart(fig_running, use_container_width=True)
    
    with col_side:
        # 5 Đơn Hàng Gần Nhất
        st.subheader("📋 5 Đơn Hàng Gần Nhất")
        
        orders_df = data['orders'].copy()
        orders_display = orders_df[['company', 'amount']].copy()
        orders_display['amount'] = orders_display['amount'].apply(lambda x: f"${x:,.0f}")
        orders_display.columns = ['Công Ty', 'Giá Trị']
        
        st.dataframe(
            orders_display,
            use_container_width=True,
            hide_index=True,
            height=180
        )
        
        st.markdown("---")
        
        # Hiệu Suất Theo Quốc Gia
        st.subheader("🌍 Hiệu Suất Theo Quốc Gia")
        
        country_df = data['country'].copy()
        country_df = country_df.sort_values('amount', ascending=True)
        
        # Mapping tên quốc gia tiếng Việt
        country_names_vi = {
            'UK': '🇬 Anh',
            'NO': '🇳🇴 Na Uy',
            'GR': '🇬🇷 Hy Lạp',
            'IT': '🇮🇹 Ý',
            'SP': '🇪 Tây Ban Nha',
            'LU': '🇱 Luxembourg'
        }
        
        country_df['country_vi'] = country_df['country'].map(country_names_vi)
        
        fig_country = go.Figure()
        fig_country.add_trace(go.Bar(
            y=country_df['country_vi'],
            x=country_df['amount'],
            orientation='h',
            marker_color='#4682B4',
            text=country_df['amount'].apply(lambda x: f"${x/1000:.0f}K"),
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Giá trị: $%{x:,.0f}<extra></extra>'
        ))
        
        fig_country.update_layout(
            height=350,
            xaxis_title="Giá Trị",
            showlegend=False,
            template="plotly_white",
            margin=dict(l=80, r=60, t=20, b=20),
            xaxis=dict(
                tickformat=',.0f',
                tickprefix='$'
            )
        )
        
        st.plotly_chart(fig_country, use_container_width=True)
    
    st.markdown("---")
    
    # =====================================================================
    # HÀNG 3: CÁC CHỈ SỐ THEO QUÝ
    # =====================================================================
    st.subheader("📊 Chỉ Số Theo Quý (2012-2016)")
    
    quarterly_df = data['quarterly_metrics'].copy()
    
    # Mapping tên metric tiếng Việt
    metric_names_vi = {
        'Amount': '💰 Doanh Thu',
        'Transactions': '📝 Số Giao Dịch',
        'Active clients': '👥 Khách Hàng Hoạt Động',
        'Active SAMs': '📋 Quản Lý Tài Sản',
        'Designers': '🎨 Thiết Kế Viên',
        'Admins': '👨‍💼 Quản Trị Viên',
        'Servers': '🖥️ Máy Chủ'
    }
    
    # Tạo tabs cho từng metric
    metrics_list = quarterly_df['metric'].unique()
    tabs = st.tabs([metric_names_vi.get(m, f'📊 {m}') for m in metrics_list])
    
    for i, metric in enumerate(metrics_list):
        with tabs[i]:
            metric_df = quarterly_df[quarterly_df['metric'] == metric].copy()
            
            # Tạo pivot table cho heatmap
            pivot_data = metric_df.pivot_table(
                index='quarter',
                columns='year',
                values='value',
                aggfunc='mean'
            )
            
            # Sắp xếp lại thứ tự quý
            quarter_order = ['Q1', 'Q2', 'Q3', 'Q4']
            pivot_data = pivot_data.reindex(quarter_order)
            
            # Tạo heatmap
            fig_quarterly = go.Figure(data=go.Heatmap(
                z=pivot_data.values,
                x=pivot_data.columns.astype(str),
                y=pivot_data.index,
                colorscale='Blues',
                text=pivot_data.values.round(0).astype(int),
                texttemplate="%{text}",
                textfont={"size": 11, "color": "white"},
                hovertemplate='Năm: %{x}<br>Quý: %{y}<br>Giá trị: %{z:,.0f}<extra></extra>',
                colorbar=dict(title="Giá trị")
            ))
            
            fig_quarterly.update_layout(
                height=400,
                xaxis_title="Năm",
                yaxis_title="Quý",
                template="plotly_white",
                margin=dict(l=60, r=40, t=40, b=60)
            )
            
            st.plotly_chart(fig_quarterly, use_container_width=True)
    
    # =====================================================================
    # HÀNG 4: THÔNG TIN CHI TIẾT BỔ SUNG
    # =====================================================================
    st.markdown("---")
    st.subheader("📌 Thông Tin Chi Tiết Bổ Sung")
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        st.markdown("""
        ### 💡 Nhận Xét Chính
        
        - **Doanh thu quý** đạt $726K trong quý hiện tại
        - **76 ngày** còn lại đến cuối quý
        - **90 giao dịch** đã được xử lý
        - Tăng trưởng ổn định qua các tuần
        """)
    
    with insight_col2:
        st.markdown("""
        ### 🎯 Quốc Gia Dẫn Đầu
        
        | Quốc Gia | Giá Trị |
        |----------|---------|
        | 🇬🇧 Anh | $451K |
        | 🇳🇴 Na Uy | $241K |
        | 🇬🇷 Hy Lạp | $22K |
        | 🇮 Ý | $8K |
        """)
    
    with insight_col3:
        st.markdown("""
        ### 📈 Xu Hướng Tăng Trưởng
        
        - Tăng trưởng ổn định qua các năm
        - Quý 4 thường có hiệu suất cao nhất
        - Sản phẩm 1 chiếm thị phần lớn
        - Gia hạn bảo trì tăng mạnh
        """)
    
    # =====================================================================
    # HÀNG 5: TÓM TẮT SỐ LIỆU
    # =====================================================================
    st.markdown("---")
    st.subheader("📊 Tóm Tắt Số Liệu Dashboard")
    
    summary_cols = st.columns(4)
    
    summary_stats = [
        {"icon": "📌", "number": "8", "label": "Chỉ Số KPI"},
        {"icon": "📈", "number": "7", "label": "Chỉ Số Phân Tích"},
        {"icon": "📅", "number": "5", "label": "Năm Dữ Liệu"},
        {"icon": "🌍", "number": "6", "label": "Quốc Gia"}
    ]
    
    for i, stat in enumerate(summary_stats):
        with summary_cols[i]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 20px; 
                        text-align: center; border: 1px solid #e2e8f0;">
                <div style="font-size: 2.5rem;">{stat['icon']}</div>
                <div style="font-size: 2.5rem; font-weight: 700; color: #667eea;">
                    {stat['number']}
                </div>
                <div style="font-size: 0.9rem; color: #718096; margin-top: 5px;">
                    {stat['label']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =====================================================================
    # FOOTER
    # =====================================================================
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: #6c757d; padding: 20px;">
        <small>
            <b>Báo Cáo Doanh Số Bán Giấy Phép Phần Mềm</b> | 
            Xây dựng với Streamlit & Plotly | 
            Cập nhật: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </small>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# CHẠY ỨNG DỤNG
# =============================================================================
if __name__ == "__main__":
    main()