import matplotlib.pyplot as plt

# 设置图像大小
plt.figure(figsize=(8, 6))

# 定义颜色
application_color = '#FFC107'
ml_scheduling_color = '#2196F3'
edge_infrastructure_color = '#4CAF50'

# 绘制第一层
plt.text(-0.5, 0.8, 'Application', fontsize=14, fontweight='bold')
plt.text(-0.5, 0.7, 'Industry IoT', fontsize=12, color=application_color)
plt.text(0.2, 0.7, 'Video Surveillance', fontsize=12, color=application_color)

# 绘制第二层
plt.text(-0.5, 0.5, 'ML-based Scheduling', fontsize=14, fontweight='bold')
plt.text(-0.5, 0.4, 'Machine Learning', fontsize=12, color=ml_scheduling_color)
plt.text(0.2, 0.4, 'Online Collaborative Scheduling', fontsize=12, color=ml_scheduling_color)

# 绘制第三层
plt.text(-0.5, 0.2, 'Edge Infrastructure', fontsize=14, fontweight='bold')
plt.text(-0.5, 0.1, 'Mobile Devices', fontsize=12, color=edge_infrastructure_color)
plt.text(0.2, 0.1, 'Edge Nodes', fontsize=12, color=edge_infrastructure_color)
plt.text(0.6, 0.1, 'Servers', fontsize=12, color=edge_infrastructure_color)
plt.text(1.0, 0.1, 'Sensors', fontsize=12, color=edge_infrastructure_color)

# 绘制子工作
# 工作1
plt.arrow(-0.2, 0.7, 0, -0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=application_color)
plt.arrow(0.0, 0.4, 0, 0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=ml_scheduling_color)
plt.arrow(0.0, 0.4, 0.2, 0, length_includes_head=True, head_width=0.02, head_length=0.02, color=ml_scheduling_color)
plt.arrow(0.2, 0.2, 0, 0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=edge_infrastructure_color)
plt.arrow(0.2, 0.2, 0.3, 0, length_includes_head=True, head_width=0.02, head_length=0.02, color=edge_infrastructure_color)
plt.text(0.0, 0.5, 'Dependency-aware Reinforcement\nLearning for Online Scheduling\nin Edge Computing', fontsize=10, ha='center', va='center')

# 工作2
plt.arrow(0.2, 0.7, 0.2, -0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=application_color)
plt.arrow(0.4, 0.4, 0, 0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=ml_scheduling_color)
plt.arrow(0.4, 0.4, 0.3, 0, length_includes_head=True, head_width=0.02, head_length=0.02, color=ml_scheduling_color)
plt.arrow(0.7, 0.2, 0, 0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=edge_infrastructure_color)
plt.arrow(0.7, 0.2, 0.3, 0, length_includes_head=True, head_width=0.02, head_length=0.02, color=edge_infrastructure_color)
plt.text(0.4, 0.5, 'Collaborative Reinforcement\nLearning for Edge Resource\nAllocation in Video Surveillance', fontsize=10, ha='center', va='center')

# 工作3
plt.arrow(0.7, 0.7, 0, -0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=application_color)
plt.arrow(0.7, 0.4, 0.3, 0, length_includes_head=True, head_width=0.02, head_length=0.02, color=ml_scheduling_color)
plt.arrow(1.0, 0.2, 0, 0.1, length_includes_head=True, head_width=0.02, head_length=0.02, color=edge_infrastructure_color)
plt.text(0.85, 0.5, 'Intelligent Offloading for\nMobile Edge Computing with\nDeep Reinforcement Learning', fontsize=10, ha='center', va='center')

# 设置坐标轴
plt.axis('off')

# 显示图像
plt.show()