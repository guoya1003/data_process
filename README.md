# data_process


详解见我csdn博客
1、图片的裁剪和合并 https://blog.csdn.net/weixin_38517705/article/details/82703252
2、
### clip_merge_picture
1、当要使用裁剪图片的功能时，取消掉clip_one_picture函数前的注释即可
```
"""调用裁剪函数示例"""
path='.\\input\\origin\\test\\'   #要裁剪的图片所在的文件夹
filename='2015_rgbn.tif'    #要裁剪的图片名
cols=1024        #小图片的宽度（列数）
rows=1024        #小图片的高度（行数）
#clip_one_picture(path,filename,1024,1024)
```
2、当要使用合并图片的功能时，取消掉merge_picture函数前的注释即可
```
"""调用合并图片的代码"""
merge_path=".\\input\\origin\\test\\crop1024_1024\\"   #要合并的小图片所在的文件夹
num_of_cols=13    #列数
num_of_rows=9     #行数
#merge_picture(merge_path,num_of_cols,num_of_rows)
```
