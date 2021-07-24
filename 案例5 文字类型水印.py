import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
font = FontProperties(fname="c:\\windows\\fonts\\simsun.ttc", size=15)
# img_src
def TextWatermark(img_src, dest, text, loc, fontsize=20, alpha=0.5):
    fig = plt.figure()
    # 读取图像
    plt.imshow(plt.imread(img_src))
    # 添加文字水印
    plt.text(loc[0], loc[1], text, fontsize=fontsize, alpha=alpha, color='gray',fontproperties=font)
    # 隐藏坐标轴
    plt.axis('off')
    # 保存图像
    plt.savefig(dest, dpi=fig.dpi, bbox_inches='tight')
    return fig

for img in ['shanghai.jpg', 'shenzhen.jpg' ,'taibei.jpg']:
    # TextWatermark(img_src=img, dest='wm_%s'%img, text='江西水利', loc=[60, 60]);
    TextWatermark(img_src='./images/'+img,dest='./images2/'+img, text='江西水利', loc=[60, 60]);