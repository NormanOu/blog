#!/usr/bin/env python3
"""
为博客文章生成数据可视化图表
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置字体（使用系统字体）
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置风格
plt.style.use('seaborn-v0_8-darkgrid')

output_dir = '/Users/norman/clawd/blog/static/images/charts/'

# 图表1：中日车企销量对比
def chart_sales_comparison():
    countries = ['中国', '日本']
    sales = [2700, 2500]
    colors = ['#FF6B6B', '#4ECDC4']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(countries, sales, color=colors, width=0.6, edgecolor='black', linewidth=1.5)
    
    # 添加数值标签
    for bar, sale in zip(bars, sales):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{sale}万辆',
                ha='center', va='bottom', fontsize=16, fontweight='bold')
    
    ax.set_ylabel('销量（万辆）', fontsize=14)
    ax.set_title('2025年全球汽车销量对比', fontsize=18, fontweight='bold', pad=20)
    ax.set_ylim(0, 3000)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}china-japan-sales.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ 图表1已生成：china-japan-sales.png')

# 图表2：全球Top 10车企销量排名
def chart_top_automakers():
    companies = ['丰田', '大众', '现代-起亚', 'Stellantis', '通用', 
                 '比亚迪', '福特', '吉利', '本田', '日产']
    sales = [1120, 920, 730, 640, 590, 427, 397, 332, 374, 337]
    colors = ['#FF6B6B' if c in ['比亚迪', '吉利'] else '#4ECDC4' for c in companies]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = np.arange(len(companies))
    
    bars = ax.barh(y_pos, sales, color=colors, edgecolor='black', linewidth=1)
    
    # 添加数值标签
    for i, (bar, sale) in enumerate(zip(bars, sales)):
        ax.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2,
                f'{sale}万辆',
                ha='left', va='center', fontsize=12, fontweight='bold')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(companies, fontsize=13)
    ax.set_xlabel('销量（万辆）', fontsize=14)
    ax.set_title('2025年全球汽车厂商销量Top 10', fontsize=18, fontweight='bold', pad=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()  # 最大值在顶部
    
    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#FF6B6B', label='中国车企'),
                      Patch(facecolor='#4ECDC4', label='其他车企')]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}global-top10-automakers.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ 图表2已生成：global-top10-automakers.png')

# 图表3：全球Top 20中各国车企数量占比
def chart_country_distribution():
    countries = ['中国', '日本', '德国', '美国', '韩国', '其他']
    counts = [6, 5, 3, 3, 2, 1]
    colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#F38181', '#FCE38A', '#C7C7C7']
    explode = (0.05, 0, 0, 0, 0, 0)  # 突出显示中国
    
    fig, ax = plt.subplots(figsize=(10, 10))
    wedges, texts, autotexts = ax.pie(counts, labels=countries, colors=colors, explode=explode,
                                       autopct=lambda pct: f'{pct:.1f}%\n({int(pct*20/100)}家)',
                                       startangle=90, textprops={'fontsize': 13})
    
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    
    ax.set_title('全球Top 20车企各国占比', fontsize=18, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}country-distribution.png', dpi=150, bbox_inches='tight')
    plt.close()
    print('✅ 图表3已生成：country-distribution.png')

# 执行所有图表生成
if __name__ == '__main__':
    print('🎨 开始生成图表...\n')
    chart_sales_comparison()
    chart_top_automakers()
    chart_country_distribution()
    print('\n✨ 所有图表生成完成！')
