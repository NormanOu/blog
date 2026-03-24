#!/usr/bin/env python3
"""
为博客文章生成数据可视化图表（英文版，避免中文字体问题）
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置字体
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置风格
plt.style.use('seaborn-v0_8-darkgrid')

output_dir = '/Users/norman/clawd/blog/static/images/charts/'

# 图表1：中日车企销量对比
def chart_sales_comparison():
    countries = ['China', 'Japan']
    sales = [2700, 2500]
    colors = ['#FF6B6B', '#4ECDC4']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(countries, sales, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
    
    # 添加数值标签
    for bar, sale in zip(bars, sales):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{sale}',
                ha='center', va='bottom', fontsize=16, fontweight='bold')
    
    ax.set_ylabel('Sales (10K units)', fontsize=14)
    ax.set_title('2025 Global Auto Sales: China vs Japan', fontsize=18, fontweight='bold', pad=20)
    ax.set_ylim(0, 3000)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # 添加注释
    ax.text(0.5, 0.95, 'China surpassed Japan for the first time in 20 years',
            ha='center', transform=ax.transAxes, fontsize=11, style='italic',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}china-japan-sales.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ Chart 1: china-japan-sales.png')

# 图表2：全球Top 10车企销量排名
def chart_top_automakers():
    companies = ['Toyota', 'VW Group', 'Hyundai-Kia', 'Stellantis', 'GM',
                 'BYD', 'Ford', 'Honda', 'Geely', 'Nissan']
    sales = [1120, 920, 730, 640, 590, 427, 397, 374, 332, 337]
    colors = ['#FF6B6B' if c in ['BYD', 'Geely'] else '#4ECDC4' for c in companies]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = np.arange(len(companies))
    
    bars = ax.barh(y_pos, sales, color=colors, edgecolor='black', linewidth=1)
    
    # 添加数值标签
    for i, (bar, sale) in enumerate(zip(bars, sales)):
        ax.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2,
                f'{sale}',
                ha='left', va='center', fontsize=12, fontweight='bold')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(companies, fontsize=13)
    ax.set_xlabel('Sales (10K units)', fontsize=14)
    ax.set_title('2025 Global Top 10 Automakers by Sales', fontsize=18, fontweight='bold', pad=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#FF6B6B', label='Chinese Automakers'),
                      Patch(facecolor='#4ECDC4', label='Others')]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}global-top10-automakers.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ Chart 2: global-top10-automakers.png')

# 图表3：全球Top 20中各国车企数量占比
def chart_country_distribution():
    countries = ['China (6)', 'Japan (5)', 'Germany (3)', 'USA (3)', 'Korea (2)', 'Others (1)']
    counts = [6, 5, 3, 3, 2, 1]
    colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181', '#FCE38A', '#C7C7C7']
    explode = (0.05, 0, 0, 0, 0, 0)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    wedges, texts, autotexts = ax.pie(counts, labels=countries, colors=colors, explode=explode,
                                       autopct='%1.1f%%',
                                       startangle=90, textprops={'fontsize': 13})
    
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    
    ax.set_title('Top 20 Automakers by Country', fontsize=18, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}country-distribution.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ Chart 3: country-distribution.png')

# 执行所有图表生成
if __name__ == '__main__':
    print('🎨 Generating charts...\n')
    chart_sales_comparison()
    chart_top_automakers()
    chart_country_distribution()
    print('\n✨ All charts generated successfully!')
