"""
home.py
Trang chủ giới thiệu Dashboard Software License Sales Report
Với danh sách chi tiết các câu hỏi kinh doanh được giải quyết
"""

import streamlit as st
from pathlib import Path
from datetime import datetime
import pandas as pd

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Trang Chủ - Software License Sales Report",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CUSTOM CSS
# =============================================================================
st.markdown("""
<style>
    /* Main container */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 60px 40px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* Question cards */
    .question-card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin: 15px 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .question-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .question-number {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        text-align: center;
        line-height: 35px;
        font-weight: bold;
        margin-right: 10px;
    }
    
    .question-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #2d3748;
        margin: 10px 0;
    }
    
    .question-detail {
        font-size: 0.9rem;
        color: #4a5568;
        line-height: 1.7;
        margin-left: 45px;
    }
    
    .question-metric {
        font-size: 0.85rem;
        color: #667eea;
        background: #f0f4ff;
        padding: 5px 12px;
        border-radius: 20px;
        display: inline-block;
        margin-top: 10px;
        margin-left: 45px;
    }
    
    /* Category header */
    .category-header {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0 20px 0;
        border-left: 5px solid #4a5568;
    }
    
    .category-icon {
        font-size: 2rem;
        margin-right: 15px;
    }
    
    .category-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d3748;
        display: inline-block;
    }
    
    /* CTA Button */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Stats */
    .stat-box {
        background: white;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #718096;
        margin-top: 5px;
    }
    
    /* Answer box */
    .answer-box {
        background: #f0fff4;
        border: 1px solid #48bb78;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
        margin-left: 45px;
    }
    
    .answer-label {
        color: #276749;
        font-weight: 600;
        font-size: 0.85rem;
        margin-bottom: 5px;
    }
    
    .answer-text {
        color: #2f855a;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">📊 Software License Sales Report</h1>
    <p class="hero-subtitle">
        Dashboard phân tích và theo dõi doanh số bán giấy phép phần mềm<br>
        Giải quyết 20+ câu hỏi kinh doanh quan trọng
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# CTA BUTTON TO DASHBOARD
# =============================================================================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 VÀO DASHBOARD PHÂN TÍCH", use_container_width=True, type="primary"):
        st.switch_page("pages/app.py")

# =============================================================================
# BUSINESS QUESTIONS SECTION
# =============================================================================
st.markdown("---")
st.markdown("""
## 🎯 Các Câu Hỏi Kinh Doanh Được Giải Quyết

Dashboard này được thiết kế để trả lời **các câu hỏi cụ thể** mà đội ngũ sales, marketing và quản lý thường xuyên đối mặt:
""")

# -----------------------------------------------------------------------------
# CATEGORY 1: DOANH SỐ & KPI
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">💰</span>
    <span class="category-title">Danh Mục 1: Doanh Số & KPI Tổng Quan</span>
</div>
""", unsafe_allow_html=True)

questions_kpi = [
    {
        "number": "1",
        "title": "Doanh số bán hàng trong quý hiện tại là bao nhiêu?",
        "detail": "Theo dõi tổng doanh thu QTD (Quarter-to-Date) để đánh giá hiệu suất bán hàng và so sánh với mục tiêu đã đề ra.",
        "metric": "QTD Sales",
        "answer": "Hiển thị số liệu real-time với định dạng tiền tệ ($)"
    },
    {
        "number": "2",
        "title": "Còn bao nhiêu ngày nữa đến cuối quý?",
        "detail": "Biết được thời gian còn lại giúp lên kế hoạch đẩy mạnh bán hàng, chạy campaign hoặc điều chỉnh chiến lược kịp thời.",
        "metric": "Days Left EOQ",
        "answer": "Đếm ngược số ngày còn lại đến End of Quarter"
    },
    {
        "number": "3",
        "title": "Có bao nhiêu giao dịch đã được xử lý trong quý?",
        "detail": "Số lượng transaction phản ánh mức độ hoạt động của đội sales và tần suất mua hàng của khách.",
        "metric": "QTD Transactions",
        "answer": "Tổng số giao dịch thành công trong quý"
    },
    {
        "number": "4",
        "title": "Có bao nhiêu khách hàng đang hoạt động?",
        "detail": "Số lượng active clients cho thấy mức độ giữ chân khách hàng và thị phần hiện tại.",
        "metric": "QTD Active Clients",
        "answer": "Số khách hàng có hoạt động trong quý"
    },
    {
        "number": "5",
        "title": "Có bao nhiêu SAMs (Software Asset Managers) đang hoạt động?",
        "detail": "SAMs là chỉ số quan trọng cho thấy mức độ triển khai và sử dụng phần mềm tại khách hàng.",
        "metric": "QTD SAMs",
        "answer": "Số lượng SAMs active trong hệ thống"
    }
]

for q in questions_kpi:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CATEGORY 2: XU HƯỚNG & TIẾN ĐỘ
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">📈</span>
    <span class="category-title">Danh Mục 2: Xu Hướng & Tiến Độ Bán Hàng</span>
</div>
""", unsafe_allow_html=True)

questions_trend = [
    {
        "number": "6",
        "title": "Doanh số tuần này so với các tuần trước như thế nào?",
        "detail": "Biểu đồ Running Totals cho phép so sánh tiến độ bán hàng theo tuần giữa quý hiện tại và các quý trước.",
        "metric": "Running Totals Chart",
        "answer": "Line chart so sánh 4 loại: Current, Previous, This Q previous year, Older"
    },
    {
        "number": "7",
        "title": "Quý này có đang đạt tiến độ tốt hơn quý trước không?",
        "detail": "So sánh đường biểu diễn của quý hiện tại với quý trước để đánh giá cải thiện hay suy giảm.",
        "metric": "Current vs Previous Quarter",
        "answer": "Overlay 2 đường trên cùng biểu đồ để so sánh trực quan"
    },
    {
        "number": "8",
        "title": "So với cùng kỳ năm ngoái, chúng ta đang làm tốt hơn hay tệ hơn?",
        "detail": "Year-over-year comparison giúp đánh giá tăng trưởng thực sự, loại bỏ yếu tố mùa vụ.",
        "metric": "This Q, Previous Year",
        "answer": "Đường màu tím thể hiện cùng kỳ năm trước"
    },
    {
        "number": "9",
        "title": "Tuần nào trong quý có doanh số cao nhất?",
        "detail": "Xác định peak weeks để hiểu mẫu hình bán hàng và lên kế hoạch resource phù hợp.",
        "metric": "Weekly Peak Analysis",
        "answer": "Hover vào biểu đồ để xem giá trị từng tuần"
    },
    {
        "number": "10",
        "title": "Dự báo doanh số cuối quý sẽ đạt bao nhiêu?",
        "detail": "Dựa trên xu hướng hiện tại và tốc độ tăng trưởng, có thể extrapolate để dự báo kết quả cuối quý.",
        "metric": "Trend Projection",
        "answer": "Phân tích độ dốc đường biểu đồ để dự báo"
    }
]

for q in questions_trend:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CATEGORY 3: PHÂN TÍCH THEO THỜI GIAN
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">📅</span>
    <span class="category-title">Danh Mục 3: Phân Tích Theo Thời Gian (2012-2016)</span>
</div>
""", unsafe_allow_html=True)

questions_time = [
    {
        "number": "11",
        "title": "Doanh số có xu hướng tăng hay giảm qua các năm?",
        "detail": "Heatmap Amount cho thấy xu hướng dài hạn, giúp đánh giá chiến lược kinh doanh có hiệu quả không.",
        "metric": "Amount Heatmap (2012-2016)",
        "answer": "Màu đậm hơn = giá trị cao hơn, dễ dàng nhận ra xu hướng"
    },
    {
        "number": "12",
        "title": "Quý nào trong năm thường có doanh số cao nhất?",
        "detail": "Phân tích seasonal pattern để biết Q1, Q2, Q3 hay Q4 là peak season.",
        "metric": "Quarterly Pattern Analysis",
        "answer": "So sánh 4 hàng Q1-Q4 trên heatmap"
    },
    {
        "number": "13",
        "title": "Số lượng giao dịch có tăng đều qua các năm không?",
        "detail": "Transactions metric cho thấy mức độ hoạt động bán hàng, độc lập với giá trị đơn hàng.",
        "metric": "Transactions Heatmap",
        "answer": "Tab Transactions trong Quarterly Metrics"
    },
    {
        "number": "14",
        "title": "Số lượng khách hàng active có tăng trưởng ổn định không?",
        "detail": "Active clients trend phản ánh khả năng mở rộng thị trường và giữ chân khách hàng.",
        "metric": "Active Clients Heatmap",
        "answer": "Tab Active clients trong Quarterly Metrics"
    },
    {
        "number": "15",
        "title": "Tài nguyên hệ thống (Admins, Designers, Servers) có tăng tương ứng với doanh số không?",
        "detail": "So sánh tăng trưởng resource với doanh số để đánh giá hiệu quả vận hành.",
        "metric": "Resource Metrics (Admins, Designers, Servers)",
        "answer": "3 tabs riêng cho từng metric resource"
    }
]

for q in questions_time:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CATEGORY 4: PHÂN TÍCH THEO KHU VỰC
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">🌍</span>
    <span class="category-title">Danh Mục 4: Phân Tích Theo Khu Vực & Quốc Gia</span>
</div>
""", unsafe_allow_html=True)

questions_region = [
    {
        "number": "16",
        "title": "Quốc gia nào đóng góp doanh số cao nhất?",
        "detail": "Country Performance chart xếp hạng các quốc gia theo doanh số, giúp xác định thị trường trọng điểm.",
        "metric": "Country Performance Bar Chart",
        "answer": "Horizontal bar chart với UK dẫn đầu ($451K)"
    },
    {
        "number": "17",
        "title": "Những thị trường nào đang có tiềm năng tăng trưởng?",
        "detail": "Các quốc gia có doanh số thấp nhưng có thể chưa được khai thác hết tiềm năng.",
        "metric": "Low Performing Countries",
        "answer": "GR, IT, SP, LU có thể là thị trường cần đầu tư thêm"
    },
    {
        "number": "18",
        "title": "Có thể lọc dữ liệu theo region không?",
        "detail": "Sidebar filter cho phép xem dữ liệu theo Europe, North America, Asia Pacific.",
        "metric": "Region Filter",
        "answer": "Dropdown filter trong sidebar"
    }
]

for q in questions_region:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CATEGORY 5: ĐƠN HÀNG & KHÁCH HÀNG
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">📋</span>
    <span class="category-title">Danh Mục 5: Đơn Hàng & Khách Hàng</span>
</div>
""", unsafe_allow_html=True)

questions_orders = [
    {
        "number": "19",
        "title": "Những đơn hàng gần nhất là gì?",
        "detail": "Last 5 Orders table hiển thị thông tin các đơn hàng mới nhất để theo dõi hoạt động sales thời gian thực.",
        "metric": "Last 5 Orders Table",
        "answer": "Company, Amount, Date cho 5 đơn gần nhất"
    },
    {
        "number": "20",
        "title": "Khách hàng nào đang mua nhiều nhất?",
        "detail": "Phân tích frequency và value của các công ty trong orders list.",
        "metric": "Customer Analysis",
        "answer": "Company 1 xuất hiện nhiều lần trong top orders"
    },
    {
        "number": "21",
        "title": "Giá trị đơn hàng trung bình là bao nhiêu?",
        "detail": "Tính toán average order value từ danh sách đơn hàng.",
        "metric": "Average Order Value",
        "answer": "Khoảng $1,300 dựa trên last 5 orders"
    }
]

for q in questions_orders:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CATEGORY 6: SẢN PHẨM & LICENSE
# -----------------------------------------------------------------------------
st.markdown("""
<div class="category-header">
    <span class="category-icon">🏷️</span>
    <span class="category-title">Danh Mục 6: Sản Phẩm & Loại License</span>
</div>
""", unsafe_allow_html=True)

questions_product = [
    {
        "number": "22",
        "title": "Sản phẩm nào (Product 1 vs Product 2) bán chạy hơn?",
        "detail": "Product filter cho phép so sánh doanh số giữa các sản phẩm.",
        "metric": "Product Filter",
        "answer": "Filter dropdown trong sidebar"
    },
    {
        "number": "23",
        "title": "License mới hay Maintenance Renewal đóng góp nhiều hơn?",
        "detail": "License Type filter phân biệt giữa Invoice (mới) và Maintenance Renewal (gia hạn).",
        "metric": "License Type Filter",
        "answer": "3 lựa chọn: All, Invoice, Maintenance Renewal"
    },
    {
        "number": "24",
        "title": "Tỷ lệ gia hạn (renewal rate) có cao không?",
        "detail": "So sánh số lượng Maintenance Renewal với Invoice để đánh giá customer retention.",
        "metric": "Renewal vs New License",
        "answer": "Filter và so sánh 2 loại license"
    }
]

for q in questions_product:
    st.markdown(f"""
    <div class="question-card">
        <div>
            <span class="question-number">{q['number']}</span>
            <span class="question-title">{q['title']}</span>
        </div>
        <div class="question-detail">{q['detail']}</div>
        <div class="question-metric">📊 Metric: {q['metric']}</div>
        <div class="answer-box">
            <div class="answer-label">✅ Dashboard trả lời:</div>
            <div class="answer-text">{q['answer']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SUMMARY TABLE
# =============================================================================
st.markdown("---")
st.markdown("""
## 📊 Tổng Kết Các Câu Hỏi Được Giải Quyết
""")

summary_data = {
    "Danh Mục": [
        "💰 Doanh Số & KPI",
        "📈 Xu Hướng & Tiến Độ",
        "📅 Phân Tích Thời Gian",
        "🌍 Khu Vực & Quốc Gia",
        "📋 Đơn Hàng & Khách Hàng",
        "🏷️ Sản Phẩm & License"
    ],
    "Số Câu Hỏi": ["5", "5", "5", "3", "3", "3"],
    "Component Dashboard": [
        "KPI Cards",
        "Running Totals Chart",
        "Quarterly Heatmaps",
        "Country Bar Chart",
        "Orders Table",
        "Sidebar Filters"
    ]
}

summary_df = pd.DataFrame(summary_data)
st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True,
    height=200
)

st.markdown("""
<div style="background: #f0f4ff; padding: 20px; border-radius: 10px; margin: 20px 0; text-align: center;">
    <h3 style="color: #667eea; margin-bottom: 10px;">🎯 Tổng Cộng: 24 Câu Hỏi Kinh Doanh Được Giải Quyết</h3>
    <p style="color: #4a5568;">Tất cả trong 1 dashboard duy nhất</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# KEY METRICS OVERVIEW
# =============================================================================
st.markdown("---")
st.markdown("""
## 📈 Các Metric Chính Được Theo Dõi
""")

metric_cols = st.columns(4)

metrics_overview = [
    {"icon": "💰", "name": "QTD Sales", "value": "$726,225", "desc": "Doanh số quý"},
    {"icon": "📝", "name": "Transactions", "value": "90", "desc": "Giao dịch"},
    {"icon": "👥", "name": "Active Clients", "value": "3", "desc": "Khách hàng"},
    {"icon": "📋", "name": "SAMs", "value": "37", "desc": "Asset Managers"}
]

for i, metric in enumerate(metrics_overview):
    with metric_cols[i]:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 2rem;">{metric['icon']}</div>
            <div class="stat-number">{metric['value']}</div>
            <div class="stat-label">{metric['name']}</div>
            <div style="font-size: 0.8rem; color: #a0aec0;">{metric['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# HOW TO USE
# =============================================================================
st.markdown("---")
st.markdown("""
## 📖 Hướng Dẫn Sử Dụng Dashboard
""")

steps = [
    {
        "step": "1",
        "title": "Xem KPI Tổng Quan",
        "description": "8 thẻ KPI ở đầu trang cho cái nhìn nhanh về tình hình hiện tại"
    },
    {
        "step": "2",
        "title": "Phân Tích Xu Hướng",
        "description": "Running Totals chart so sánh quý hiện tại với các quý trước"
    },
    {
        "step": "3",
        "title": "Sử Dụng Filters",
        "description": "Sidebar bên trái để lọc theo Product, License Type, Region"
    },
    {
        "step": "4",
        "title": "Khám Phá Heatmaps",
        "description": "7 tabs Quarterly Metrics cho phân tích chi tiết theo thời gian"
    },
    {
        "step": "5",
        "title": "Kiểm Tra Đơn Hàng",
        "description": "Last 5 Orders và Country Performance cho thông tin chi tiết"
    }
]

for i, step in enumerate(steps):
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; width: 40px; height: 40px; 
                    border-radius: 50%; display: flex; align-items: center; 
                    justify-content: center; font-weight: bold; font-size: 1.2rem;">
            {step['step']}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        **{step['title']}**
        
        {step['description']}
        """)
    if i < len(steps) - 1:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

# =============================================================================
# FINAL CTA
# =============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 15px; margin-top: 40px; color: white;">
    <h2 style="margin-bottom: 15px;">🚀 Sẵn Sàng Phân Tích Dữ Liệu?</h2>
    <p style="font-size: 1.1rem; opacity: 0.95; margin-bottom: 30px;">
        Truy cập dashboard để khám phá toàn bộ 24 câu hỏi kinh doanh được giải quyết
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(" VÀO DASHBOARD PHÂN TÍCH ", use_container_width=True, type="primary", key="final_cta"):
        st.switch_page("pages/app.py")

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #718096; padding: 30px;">
    <small>
        <b>Software License Sales Report Dashboard</b><br>
        Built with Streamlit & Plotly | 
        Version 1.0 | 
        Cập nhật: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </small>
</div>
""", unsafe_allow_html=True)