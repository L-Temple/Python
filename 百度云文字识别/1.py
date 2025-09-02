# -*- coding: utf-8 -*-
import csv

def txt_to_csv(input_file, output_file, delimiter='|'):
    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        # 创建 CSV 写入器
        csv_writer = csv.writer(outfile, delimiter=delimiter)

        # 逐行读取 .txt 文件
        for line in infile:
            # 去除行首尾的空白字符
            line = line.strip()
            # 按空格或其他分隔符拆分字段
            fields = line.split()  # 默认按空格拆分，如果需要其他分隔符，可以修改 split() 的参数
            # 将字段写入 CSV 文件
            csv_writer.writerow(fields)

    print(f"转换完成！结果已保存到 {output_file}")

# 输入文件和输出文件路径
input_file = '涡轮.txt'  # 替换为你的 .txt 文件路径
output_file = 'output.csv'  # 替换为你的 .csv 文件路径

# 调用函数进行转换
txt_to_csv(input_file, output_file)