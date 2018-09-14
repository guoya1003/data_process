import cv2
import os
import numpy as np

def file_name(root_path,picturetype):
    filename=[]
    for root,dirs,files in os.walk(root_path):
        for file in files:
            if os.path.splitext(file)[1]==picturetype:
                filename.append(os.path.join(root,file))
    return filename

'''
输入：包含图片的文件夹，每次的旋转角度(直到360度),图片格式如：'.jpg'
输出：通过旋转后得到的所有图片
'''
def rotate(root_path,rotation,picturetype):
    filetxt=file_name(root_path,picturetype)
    for j in range(len(filetxt)):
        img=cv2.imread(filetxt[j],1)#读取彩色图像，图像的透明度(alpha通道)被忽略，默认参数;灰度图像;读取原始图像，包括alpha通道;可以用1，0，-1来表示
        print(filetxt[j])
        rows=img.shape[0]
        cols=img.shape[1]
        print("正在旋转第"+str(j)+"张图片")
        for i in range(int(360/rotation)):
            M=cv2.getRotationMatrix2D((cols/2,rows/2),rotation*i,1)
            # 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
            #可以通过设置旋转中心，缩放因子(可选)，以及窗口大小来防止旋转后超出边界的问题
            dst=cv2.warpAffine(img,M,(cols,rows))   #第一个参数源图像，第二个参数变换矩阵，第三个是变换后尺寸（先列后行）
            cv2.imwrite(os.path.splitext(filetxt[j])[0]+'_'+str(i)+os.path.splitext(filetxt[j])[1],dst)


    print("已全部旋转完毕")



root_path='D:\pycharm\BuildingChangeDetector\dataenhancement'  #包含图片的文件夹
rotation=30              #每次的旋转角度(直到360度)
picturetype='.png'           #图片格式如：'.jpg'
rotate(root_path,rotation,picturetype)

