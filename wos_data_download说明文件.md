#### web of science文献题录python自动下载

#### 写在前面

- 通过python控制鼠标和键盘，来实现web of science上文献题录的自动下载
- 需要注意的是，在每一步的鼠标点击的<font color='#008B8B'>位置</font>，需要使用QQ等其他工具确定
- 下面是具体的操作步骤，仅供参考

1.打开web of science网站，输入检索词

![image-20220622235402918](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622235402918.png)

2.查看检索结果

![image-20220622132759695](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622132759695.png)



3.同时打开电脑上的QQ，需要使用这个来进行截图![image-20220622132722934](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622132722934.png)



4.使用PyCharm(或者Spyder或者Jupyter Notebook)打开python代码

![image-20220622133041409](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622133041409.png)



5.比如说我们现在需要控制鼠标点击导出按钮，需要修改代码

![image-20220622133238350](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622133238350.png)



6.按住`Ctrl + alt + A`截图，从电脑的左上角开始选中，拉到鼠标需要点击的位置，会出现一个像素（如1150 x 879），记住这个像素，然后更改代码中的数字（因为每个人的电脑不同，屏幕尺寸不同，因此这一步需要去做）

![image-20220622133449489](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622133449489.png)

![image-20220622133745537](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622133745537.png)



7.然后对应者将其他地方的像素也进行修改即可

![image-20220622133955734](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622133955734.png)



8.`else`后面的代码，也需要修改，跟while部分的像素位置一样

![image-20220622134133561](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622134133561.png)

![image-20220622134242694](https://cdn.jsdelivr.net/gh/Super-dong94/Picture/img/image-20220622134242694.png)



9.更改完成后，就可以按照提示运行代码了！对于不太懂的，我录制了视频文件，大家可以看视频！