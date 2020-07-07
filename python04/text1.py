import os


try:
    os.mkdir("gy_C")
except Exception:
    print("文件夹已存在")
else:
    print("文件夹创建成功")