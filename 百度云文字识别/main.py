# -*- coding: utf-8 -*-
from aip import AipOcr
import os
import pandas as pd

# 百度 OCR 配置
APP_ID = '6281638'
API_KEY = 'fMUhqQhqCGcvZj69FEeadcxM'
SECRET_KEY = 'otOfPgx5nXJwPaXwjXCvG5LdS40yaAlI'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 图片文件夹路径
image_folder = "源图片"  # 替换为你的图片文件夹路径

# 识别结果保存路径
output_excel = "output.xlsx"

# 初始化结果列表
results = []

# 遍历文件夹中的图片
for filename in os.listdir(image_folder):
    if filename.endswith((".png", ".jpg", ".jpeg", ".bmp")):
        # 读取图片
        image_path = os.path.join(image_folder, filename)
        with open(image_path, 'rb') as f:
            image = f.read()

        # 调用百度 OCR 识别文字
        response = client.basicGeneral(image)
        text = "\n".join([item['words'] for item in response.get('words_result', [])])

        # 将结果添加到列表
        results.append({"文件名": filename, "识别内容": text})

# 将结果保存到 Excel
df = pd.DataFrame(results)
df.to_excel(output_excel, index=False)

print(f"识别完成，结果已保存到 {output_excel}")