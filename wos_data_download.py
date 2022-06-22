"""
Created on Tue Jun 14 03:54:22 2022

@author: Superdong
"""

import time
import pyautogui
import pyperclip
import numpy as np

# 请输入数据长度,强制转换为整数
len = int(input("请输入文献条目数："))

# 请打开web of science界面
print("请打开web of science界面")
print("6.6秒后开始运行")

# 延时几秒
time.sleep(6.6)

# 一共len条数据
max_num = np.arange(1, len, 500)

# 计算数组的长度
num = max_num.size
# print(max_num,num,max_num[num-1])

# 开始下载数据
i = 1
index = 1
while i < max_num[num - 1]:
    # 单击导出按钮
    pyautogui.click(1291, 1041)
    time.sleep(1)

    # 单击纯文本文件
    pyautogui.click(1360, 457)
    time.sleep(1)

    # 单击记录前的圆圈
    pyautogui.click(852, 1073)
    time.sleep(1)

    # 双击第1个数字
    pyautogui.doubleClick(1002, 1094)
    time.sleep(1)

    # 输入第1个数字
    pyperclip.copy(i)
    pyautogui.hotkey("ctrl", "v", interval=0.5)

    # 双击第2个数字
    pyautogui.doubleClick(1182, 1100)
    time.sleep(1)

    # 输入第2个数字
    j = i + 499
    pyperclip.copy(j)
    pyautogui.hotkey("ctrl", "v", interval=0.5)
    time.sleep(1)

    # 单击空白
    pyautogui.click(900, 850)
    time.sleep(1)

    # 向下按一下
    pyautogui.press("down")
    time.sleep(1)

    # 点击选择
    pyautogui.click(1396, 1189)
    time.sleep(2)

    # 单击全纪录与参考文献
    pyautogui.click(1295, 1222)
    pyautogui.click(1295, 1222)
    time.sleep(1.5)

    # 单击导出
    pyautogui.click(898, 1130)
    pyautogui.click(898, 1130)

    # 等待16秒
    time.sleep(30)

    # 单击空白
    pyautogui.click(1576, 605)
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("up")

    print("恭喜您：", "第", index, "条数据", i, "-", j, "数据下载成功", "！")

    # 下一个
    i = i + 500
    index = index + 1

else:
    # 单击导出按钮
    pyautogui.click(1291, 1041)
    time.sleep(1)

    # 单击纯文本文件
    pyautogui.click(1360, 457)
    time.sleep(1)

    # 单击记录前的圆圈
    pyautogui.click(852, 1073)
    time.sleep(1)

    # 双击第1个数字
    pyautogui.doubleClick(1002, 1094)
    time.sleep(1)

    # 输入第1个数字
    pyperclip.copy(i)
    pyautogui.hotkey("ctrl", "v", interval=0.5)

    # 双击第2个数字
    pyautogui.doubleClick(1182, 1100)
    time.sleep(1)

    # 输入第2个数字
    j = len
    pyperclip.copy(j)
    pyautogui.hotkey("ctrl", "v", interval=0.5)
    time.sleep(1)

    # 单击空白
    pyautogui.click(900, 850)
    time.sleep(1)

    # 向下按一下
    pyautogui.press("down")
    time.sleep(1)

    # 点击选择
    pyautogui.click(1396, 1189)
    time.sleep(2)

    # 单击全纪录与参考文献
    pyautogui.click(1295, 1222)
    pyautogui.click(1295, 1222)
    time.sleep(1.5)

    # 单击导出
    pyautogui.click(898, 1130)
    pyautogui.click(898, 1130)

    # 等待16秒
    time.sleep(30)

    # 单击空白
    pyautogui.click(1576, 605)
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("up")

    # 下载成功
    print("恭喜您：", "第", index, "条数据", i, "-", j, "数据下载成功", "！")
