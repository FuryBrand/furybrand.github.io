import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pygetwindow as gw
import tkinter as tk
from tkinter import messagebox

# 全局Tkinter root实例
root = tk.Tk()
root.withdraw()  # 隐藏Tkinter主窗口
# 设置窗口始终在最前面
root.attributes("-topmost", True)

# 创建一个函数来显示提示信息
def show_message(title, message):
    # 创建一个顶级窗口来显示消息
    top = tk.Toplevel(root)
    top.title(title)
    tk.Label(top, text=message, width=40, height=10).pack()
    top.lift()
    top.attributes('-topmost', True)
    top.after(6000, top.destroy)  # 6秒后自动关闭提示窗口

# 在主线程的Tkinter loop中调度显示消息
def display_message(title, message):
    root.after(0, show_message, title, message)
    root.update()  # 强制Tkinter更新界面

# 创建一个函数来显示最终的确认对话框
def show_final_confirmation():
    # 使用全局root实例显示对话框
    result = messagebox.showinfo("操作完成", "所有操作已完成，您可以继续了。", parent=root)
    return result

def confirm_close_chrome():
    # 初始化Tkinter
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()

    # 弹出对话框提醒用户关闭所有Chrome窗口
    user_response = messagebox.askokcancel(
        "确认",
        "请确保所有Chrome均已关闭!!！\n否则自动化脚本执行可能会出现故障。\n点击“确定”后脚本将继续执行，点击“取消”后脚本将终止"
    )

    # 关闭Tkinter窗口
    root.destroy()

    return user_response

if __name__ == "__main__":
    try:
        # 在脚本开始时调用函数
        if confirm_close_chrome():
            # 用户点击了确认，继续执行脚本
            print("脚本继续执行...")

            # 设置Chrome选项...
            # 设置Chrome选项，使其打开特定的屏幕/显示器
            options1 = Options()
            options1.add_argument("--start-maximized") #不能生效，因为--window-position指定了窗口的起始位置
            options1.add_argument("--window-position=0,0") # 屏幕1的位置
            options1.add_experimental_option("excludeSwitches", ['enable-automation'])
            options1.add_experimental_option("detach", True)

            options2 = Options()
            options2.add_argument("--window-position=1920,0") # 屏幕2的位置，假设屏幕1的分辨率为1920x1080
            options2.add_argument("--start-maximized")
            options2.add_experimental_option("excludeSwitches", ['enable-automation'])
            options2.add_experimental_option("detach", True)

            # 路径和登录信息
            url = 'http://192.168.0.129:8080/login'
            username = 'admin'
            password = '123456'

            # 启动第一个Chrome实例并执行操作
            display_message("操作提示", "正在处理浏览器窗体1...")
            driver1 = webdriver.Chrome(service=Service('chromedriver126.exe'), options=options1)
            driver1.get(url)
            time.sleep(2)  # 等待页面加载
            # 输入用户名和密码
            driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/div/div/div/input').send_keys(username)
            driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/div/div/input').send_keys(password)
            driver1.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/button').click()
            time.sleep(2)  # 等待登录

            # 导航到指定菜单
            driver1.find_element(By.XPATH, '/html/body/div[1]/div/section/aside/div/div[2]/div[1]').click()
            time.sleep(10)  # 等待页面加载
            
            # 启动第二个Chrome实例并执行操作
            display_message("操作提示", "正在处理浏览器窗体2...")
            driver2 = webdriver.Chrome(service=Service('chromedriver126.exe'), options=options2)
            driver2.get(url)
            time.sleep(2)  # 等待页面加载
            # ... 登录和导航代码 ...
            # 输入用户名和密码
            driver2.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/div/div/div/input').send_keys(username)
            driver2.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/div/div/input').send_keys(password)
            driver2.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/button').click()
            time.sleep(10)  # 等待登录

            # 导航到指定菜单
            driver2.find_element(By.XPATH, '/html/body/div[1]/div/section/aside/div/div[2]/div[1]').click()
            time.sleep(2)  # 等待页面加载
            driver2.find_element(By.XPATH, '/html/body/div[1]/div/section/main/section/footer/div[1]/ul/li[2]').click() # 翻页

            display_message("操作提示", "正在最大化窗体")
            time.sleep(10) 

            window1 = gw.getWindowsWithTitle('边缘XXXX系统')[0]
            print(window1)
            window1.maximize()
            window2 = gw.getWindowsWithTitle('边缘XXXX系统')[1]
            print(window2)
            window2.maximize()

            if show_final_confirmation():
                print("操作提示", "用户已确认，脚本结束。")
            else:
                print("操作提示", "用户已取消，脚本结束。")

        else:
            # 用户点击了取消，终止脚本
            print("脚本已终止。")
    except Exception as e:
        display_message("错误", f"发生错误：{e}")
