from matplotlib import pyplot as plt
import random
import matplotlib

# 设置x轴刻度的字体，大小和粗细
font = {'family':'MicroSoft YaHei',
        'weight':'bold',
        'size':12}
matplotlib.rc("font",**font)
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold",size=8)

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

# 设置x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(0,60)]
_xtick_labels += ["11点{}分".format(i) for i in range(0,60)]

# 取步长，数字和字符串的个数一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)  # ratation 旋转的度数

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位（℃）")
plt.title("10点到12点的温度变化")

plt.show()
