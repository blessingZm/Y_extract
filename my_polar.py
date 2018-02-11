import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def my_polar(wind_preps, title):
    """
    :param wind_preps: 字典，key为16方位及C，value为各方位对应的频率值
    :param title: 玫瑰图的标题
    :return: None, 绘制风向频率玫瑰图
    """
    wind_direc = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'C']
    wd_preps = []
    for direc in wind_direc:
        wd_preps.append(wind_preps[direc])

    # 只画16个方位的频率，C的频率以标题形式给出
    wd_len = len(wind_direc[:-1])

    prep_max = max(wd_preps) + 2
    preps = np.array(wd_preps[:-1])
    # 设置极坐标x的范围
    angles = np.linspace(0, 2 * np.pi, wd_len, endpoint=False)
    # 设置极坐标及频率数据起止点的闭合
    angles = np.concatenate((angles, [angles[0]]))
    preps = np.concatenate((preps, [preps[0]]))
    # 开始绘制风向玫瑰图
    fig = plt.figure(figsize=(10, 8))
    # 创建极坐标
    ax = fig.add_subplot(122, projection='polar')
    # 画线
    ax.plot(angles, preps, 'k-', linewidth=1)
    # 设置极坐标0°对应位置
    ax.set_theta_zero_location('N')
    # 设置极坐标正方向，1：逆时针，-1：顺时针
    ax.set_theta_direction(-1)
    ax.fill(angles, preps, facecolor='r', alpha=0.25)
    # 设置坐标轴显示
    ax.set_thetagrids(angles * 180 / np.pi, labels=wind_direc[:-1],
                      fontsize=15, fontproperties="SimHei")
    # 设置极径网格线显示
    ax.set_rgrids(np.arange(2, prep_max, 4))
    # 设置极径的范围
    ax.set_rlim(0, 20)
    # 设置极径标签显示位置
    ax.set_rlabel_position('30')
    # 设置图题
    ax.text(angles[0], prep_max + 4, title,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=15, fontproperties="SimHei",
            bbox=dict(facecolor='white'))
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    db_file = r'.\db_files\Y_57461.db'
    db = sqlite3.connect(db_file)
    cu = db.cursor()
    data = cu.execute("select * from dif_wd_frequecy where ObserveTime == '2017-12'").fetchall()
    wdPrep = list(data[0][1:])
    windDirec = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW',
                 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'C']
    windDatas = {}
    for key, v in zip(windDirec, wdPrep):
        windDatas[key] = int(v)
    my_polar(windDatas, '静风频率:{}'.format(windDatas['C']))
