## `img2braille`

将图片转化为盲文点字。

转换的代码来自：https://github.com/eugene-eeo/img2braille

做了如下改进：
 - 修改了图像加载方式，避免 opencv-python 在中文路径下加载图像报错
 - 根据盲文点字的编码规则修改了映射规则，将原本的6位改进到8位，显示效果更好
 - 设置了GUI，操作和参数设置更加直观方便
 
### 环境:
 - opencv-python
 - numpy
 - PySide2
 - QTdesigner.exe
 
将输入的图像转化为盲文点阵图像，bsize=11, width=30，效果如下：

⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠉⠀⠀⠈⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠁⠀⡠⢐⣂⣤⣬⣥⣄⣒⠠⢀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠀⡠⣠⣾⣿⠿⠿⠿⣿⣿⣿⣿⣶⣄⠢⡀⠀⠙⣿⣿⣿⣿⣿
⣿⣿⡿⠿⠇⠀⠠⢰⣿⢋⣶⠉⠻⠟⣶⡝⣿⣿⣿⣿⣷⣌⢀⠀⠈⠿⣿⣿⣿
⠋⠁⠀⢀⣀⠀⠀⠿⠏⠾⠇⢸⣴⠀⣿⡗⣽⣿⣿⣿⣿⣿⣧⡠⠀⠀⠀⠉⠙
⡠⣂⣥⣶⣶⣾⣿⣷⣶⣶⣶⣶⣤⣭⣍⣚⡻⠿⣿⣿⣿⣿⣿⣷⣭⣭⣄⡢⡀
⢔⡋⠁⠀⠀⠀⠀⢨⣭⣝⣛⠿⢿⣿⣿⣿⣿⣿⣶⣝⡻⣿⣿⣿⣿⣿⣿⣿⡔
⠀⠀⠉⠙⣂⡄⠀⠞⠙⣿⡿⠋⢻⣶⣭⣝⣛⣛⣛⣛⡅⠈⠻⣿⣿⣿⣿⣿⡇
⠀⡀⣪⣴⣶⣤⣜⠀⣰⣿⡇⠀⣸⣿⣿⡿⣿⣿⣿⠟⠀⠀⠀⣽⣶⠶⣶⣶⣅
⠈⣼⣿⣿⣿⣿⣿⣷⣿⣿⣷⣾⣿⠟⠋⠀⢸⣿⠃⠀⠀⠀⣰⣿⢃⣬⣽⣿⣿
⠀⡙⢿⣿⣿⣿⣿⣿⠟⠙⠋⠉⢀⣴⡟⠁⣸⣿⣿⣄⣤⣾⣿⣿⣸⣿⣿⣿⠟
⠀⠈⡆⠉⠉⠉⠉⠀⠀⣀⣴⣾⣿⠟⢀⣴⣿⣿⣿⣿⡿⢁⠭⠙⣛⣛⡋⠅⠊
⡄⠀⠘⠷⣶⣶⡄⠒⠋⠉⠀⠀⢀⣠⣾⣿⣿⡿⠟⡋⠔⠁⠀⠀⠀⠀⠀⢀⣠
⣿⣦⣀⠀⠉⠛⠷⠶⠆⠤⠍⠛⠛⠛⠉⠭⠀⠂⠉⠀⢀⣠⣾⣿⣿⣾⣿⣿⣿

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠘⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡰⠍⠯⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢸⣅⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⠹⠯⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣇⠀⡝⢶⡄⢩⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⡩⢔⠊⠁⠾⢳⣥⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⢛⡩⣐⣌⡶⣾⣟⣠⣤⠂⠿⢿⠂⠸⣿⣿⣿⣿⣿⣿⣿⣽
⣽⡿⣿⣿⣿⡟⠀⠁⠐⣏⣧⡿⠻⠛⣉⣠⠰⡶⣤⣌⡁⣕⠝⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⣤⠼⠚⢉⣡⣤⡶⢫⠝⡶⠁⣷⡔⡄⣷⡈⢯⢘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣯⠀⠴⢶⠿⡟⢹⡇⣸⣿⡆⣇⠀⢿⠇⡇⣿⠝⡌⢃⠈⢹⣿⣿⣿
⣿⡏⠀⢹⣿⠀⢰⣽⡼⢧⢸⣃⢿⠯⣆⡻⢰⢘⣑⠋⢻⠀⣽⣦⠑⢸⣿⣿⣿
⣿⡇⣀⡏⠛⠀⠬⠻⡐⣾⣄⠐⣨⡏⢴⣿⢸⢸⡂⡇⡆⡣⣿⢸⢓⠌⣿⣿⣿

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢛⠃⢒⠿⢿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀⠀⠠⣄⢐⣠⣄⢦⠈⡻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢟⣿⣿⠃⠀⠀⠀⠀⠀⠂⡨⠛⠀⠄⠀⠀⠈⡏⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢿⣺⠇⠀⢀⣤⣤⣴⣶⣶⣾⣿⣿⣿⣿⣷⡄⠅⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡍⠩⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠀⢰⣿⠛⠉⠛⠛⠿⣿⣿⡟⠛⠛⠛⢿⡇⠀⠨⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡁⠀⢸⣿⣟⣉⣉⣍⣀⢹⣿⠀⣉⣍⣉⠚⣧⠐⠴⢿⠿⠿⠿⣿
⣀⡀⢀⣀⠹⢿⣇⠀⣿⣿⣿⣿⣿⡿⠈⣿⡈⢿⣿⣿⣿⣿⠀⣾⠇⠀⠄⣠⣌
⡿⣿⠛⠛⠀⠀⣿⡆⢩⡿⢿⣻⣿⠚⠒⠿⠿⢣⣝⠿⠻⣿⣶⡏⠀⣴⣿⠿⠿
⠄⢸⡖⠀⠸⣷⡎⡉⢸⣷⣿⡀⠨⣾⣷⠤⣦⠄⢀⣷⢀⡟⠛⠀⢠⣠⣿⢸⣿
⠆⢹⣷⣴⣦⣾⡇⢖⣆⠹⢻⣿⣷⢶⡯⡯⠧⣺⣿⡛⣸⠁⣰⡇⣿⣿⣿⣶⣶
⠒⠉⠀⠈⣹⣿⣇⢸⣿⣆⠈⢿⣿⣿⣿⣷⣿⣷⡿⠀⣿⠀⢹⡧⣍⣉⣙⠩⣭
⣶⣾⣷⣾⠿⠻⠋⢸⣿⣿⡆⠀⡙⠛⠿⠛⠛⠉⢃⠀⣿⣄⠈⡇⢘⠋⣠⣴⣬
⠟⠋⠉⠀⠂⠀⡀⢸⣿⣿⣿⣧⣿⣿⣿⡷⠞⣾⣿⣤⡿⠘⡷⡕⡾⢄⣿⣿⣿

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠉⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣀⡠⠠⠤⠄⠀⢤⣤⣀⡀⠀⠀⠈⠛⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠉⠈⠀⠐⢀⠀⠀⠀⠹⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢠⣴⣾⣿⡿⠋⣡⠤⠉⠀⠀⠀⠀⠀⠀⠀⠹⣿
⣿⣿⣿⣿⣿⡇⠀⠀⠀⣠⣴⣿⣿⣿⣿⣵⣬⣥⣄⣠⣤⣶⣶⣶⠀⣀⠀⠀⢹
⣿⣿⣿⣿⣿⠁⠀⠀⢘⣿⣿⡿⢿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡆⠀⠈
⣿⣿⣿⣿⠗⢤⠀⠀⣹⣿⣿⣿⡿⠿⢿⣾⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⡇⠀⠀
⣿⣿⣿⠃⠔⠛⢧⢀⣿⣿⣿⠿⢷⣿⣶⡄⠈⠛⣿⣿⣿⠿⠿⣿⣿⣿⡇⠀⢠
⣿⣿⣿⡇⢀⡒⢺⣯⣿⣿⣿⣷⣶⠄⠈⠙⠃⠀⠻⠹⣴⣶⣶⣦⣽⣿⠃⠀⣾
⣿⣿⣿⣧⢸⣿⣾⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣤⣧⣀⣉⣙⣿⣿⡀⢰⣿
⣿⣿⣿⣿⣦⣌⡙⢿⣿⣏⠉⠉⠉⠉⠀⠸⠿⠿⢿⡿⢿⣿⣿⣿⣿⠋⠀⣼⣿
⣿⣿⣿⣿⣿⣿⠇⣸⣿⣿⣾⣷⡄⠐⠿⢷⣶⣤⣤⣤⠀⠙⠿⠻⠗⠀⣼⣿⣿
⣿⣿⣿⣿⠟⠉⠀⢿⣿⣅⣍⣉⣵⣿⣦⡂⠀⠈⣉⣹⣧⣶⡆⠀⢠⣾⣿⣿⣿
⣿⡿⠏⠁⠀⣤⡀⠘⣿⣏⠙⠛⢿⣿⣿⣷⣶⣾⣿⣿⣿⠏⢀⣴⣿⣿⣿⣿⣿

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣡⣤⣶⣶⣶⣤⣌⣉⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⢉⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣶⣄⠙⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⠟⠋⣡⣶⣾⡿⠛⢷⡄⢻⣿⣿⣿⣿
⣿⣿⣿⣿⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⡏⢱⣶⣾⣿⠀⣿⣿⣿⣿
⣿⣿⣿⡿⢰⣿⣿⣿⣿⣿⡿⠋⣻⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⠀⣿⣿⣿⣿
⣿⣿⣿⡇⢸⣿⣿⣿⠟⢋⣤⣤⣿⣿⣿⣿⣿⣿⣿⠏⣰⣿⣿⠏⣰⣿⣿⣿⣿
⣿⣿⣿⣧⠘⣿⣟⢁⣴⣿⡟⠻⣿⣿⣿⣿⣿⠟⢁⣴⣿⠿⠋⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣦⠘⣿⣿⠛⠻⣷⣦⣌⣉⣉⣉⣤⣶⣿⣿⠁⣴⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠛⢶⣾⣿⣿⣿⣿⡿⠟⠋⢁⣼⣿⣧⠈⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣤⣈⣉⣉⣉⣁⣤⣾⠇⣸⣿⣿⣿⣧⠘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣟⣋⣀⢠⢠⣿⣿⣿⣿⣿⣿⠟⠓⠲⡙⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠈⢸⣿⣿⠛⠉⠙⠇⢰⣿⠀⣷⣡⣼⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠀⣸⣿⡇⠀⣿⣷⡀⣸⡿⠀⣷⣿⠛⣿⠋⡽⠛⠶⢻⣿⠓⣿⣿⣿
⣿⣿⣿⡇⠀⣿⣿⣷⡀⠘⣿⣿⡿⠃⣰⣿⣿⣧⠈⢠⠰⣿⠀⠸⠋⡀⠾⣿⣿
⣿⣿⡿⠃⠀⠿⢿⣿⣷⣄⠈⠻⠁⣰⣿⣿⠿⠃⡠⣿⣦⣤⣴⣖⣚⣿⣶⣩⣾
⣿⣿⣿⣶⣶⡦⢄⡻⣻⣿⣿⠀⣼⣿⣿⣤⣤⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣏⣵⣾⣯⣾⣿⣿⣇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

tips：
 - 最好使用背景单一的动漫图像，会有更好的效果
 - 根据显示的宽度限制来设置，如微信、评论区。设置的大一点分辨率就更高，显示效果就更好。
 - 可以提前将需要突出的信息先抠出来
 
 设计的GUI效果：
![GUI效果](imgs\test.png)
