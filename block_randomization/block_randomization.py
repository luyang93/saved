import pandas as pd
import random
import xlrd
import xlwt


try:
    df = pd.DataFrame(pd.read_excel('data.xls'))
    if df.shape[1] == 2:
        print('文件格式正确，继续进行\n')
        # 读取sheet1
        df = pd.DataFrame(pd.read_excel('data.xls'))

        # 按照观测指标排序
        df = df.sort_values(by=df.columns[1])

        # 确定组数
        group = int(input("你想分成几组？\n"))
        number = df.shape[0]
        group_orders = []

        # block_randomization
        if number % group == 0:
            group_num = int(number / group)
            print('分成 %d 组, 每组 %d 只' % (group, group_num))
            for i in range(group_num):
                group_orders.append(random.sample(range(group), group))
        else:
            group_res = number % group
            group_num = int(number // group)
            print('分成 %d 组, %d 组 %d 只, %d 组 %d 只' % (group, group_res, group_num + 1, group - group_res, group_num))
            for i in range(group_num):
                group_orders.append(random.sample(range(group), group))
            group_orders.append(random.sample(range(group_res), group_res))

        # 生成分组信息
        categories = []
        for orders in group_orders:
            for category in orders:
                categories.append(category + 1)
        # 添加列
        df['category'] = categories

        # 按照category进行排序
        df = df.sort_values(by=df.columns[2])

        # 保存到文件
        df.to_excel('category.xls', sheet_name='category')
    else:
        print('请确认只有两列数据，第一列为number，第二列为weight(分组依据观测指标)\n')
except:
    print('仔细阅读README，将数据文件命名为data.xls，并放在block_randomization文件夹内\n请安装pandas,xlrd,xlwt模块')