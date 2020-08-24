import numpy as np
from collections import defaultdict
import time
from pyecharts.charts import Sankey, Page
from pyecharts import options as opt

dict_card = defaultdict(list)


def random_shuffle(n):  # method one 随机洗牌算法
    global B, A
    B = list(range(1, n + 1))
    A = ['a', 'b', 'c', 'd' , 'e']
    a = A[:]
    print(A)
    print(B)
    print(dict(zip(A,B)))
    # method one  随机洗牌
    for i in range(len(B) - 1, 0, -1):
        r = np.random.randint(0, i + 1)
        B[i], B[r] = B[r], B[i]
        print(dict(zip(A,B)))
    if len(a) <= len(B):
        for k in range(len(a)):
            dict_card[a[k]] = B[k * (len(B) // len(a)):(k + 1) * (len(B) // len(a))]
    if len(B) % len(a):
        for k in range(-(len(B) % len(a)), 0):
            r = np.random.choice(a)
            dict_card[r].append(B[k])
            a.remove(r)
            print(dict_card)


def random_assign(n):  # method two  随机发牌函数
    global B, A
    B = list(range(1, n + 1))
    A = ['a', 'b', 'c', 'd','e']
    b = B[:]
    a = A[:]
    mod = len(B) % len(A)
    r = 0
    length = len(b)
    C = []
    for i in range(length - mod):
        k = np.random.randint(0, len(b))
        C.append(b[k])
        b.pop(k)
    print(C)
    if len(A) <= len((B)):
        for j in range(len(A)):
            dict_card[A[j]] = C[j * (len(C) // len(A)):(j + 1) * (len(C) // len(A))]
    if mod:
        for k in range(-mod, 0):  # 多余的数随机分配
            r = np.random.choice(a)  # 避免被重复分配
            a.remove(r)
            dict_card[r].append(b[k])


def value2str(dict):  # 将字典中的value转换为str格式
    dict['source'] = str(dict['source'])
    return dict


# 制作桑吉图
def make_sanky():
    links = []
    nodes1 = [{'name': i} for i in A]
    nodes2 = [{'name': j} for j in B]
    nodes1.sort(key=lambda x: x['name'])
    nodes2.sort(key=lambda x: x['name'])
    nodes1.extend(nodes2)  # 制作节点图

    for j in dict_card.keys():
        for k in dict_card[j]:
            links.append({'source': k, 'target': j, 'value': np.random.randint(15)})
    links.sort(key=lambda x: x['source'])
    links = list(map(value2str, links))  # 制作关系图

    # 绘制桑吉图
    C = (Sankey(init_opts=opt.InitOpts(width='1100px', height='600px')).add('',
                                                                            nodes1,
                                                                            links,
                                                                            linestyle_opt=opt.LineStyleOpts(opacity=0.5,
                                                                                                            curve=0.5,
                                                                                                            color='target',
                                                                                                            type_='dotted'),
                                                                            label_opts=opt.LabelOpts(
                                                                                position='left', ), ).set_global_opts(
        title_opts=opt.TitleOpts(title='随机分配'))

    )
    C.render('random assignments.html')


# 主程序运行
n = 5
random_shuffle(n)
for item in dict_card:
    print('{0}:{1}'.format(item, dict_card[item]))
make_sanky()

# 我新增了一列