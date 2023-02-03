import pandas as pd
import json
import pymysql
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'yuemaifang',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor
}

def con_sql(sql):
	db = pymysql.connect(**config)
	cursor = db.cursor()
	cursor.execute(sql)
	result = cursor.fetchall()
	df = pd.DataFrame(list(result))
	db.close()
	return df

data = con_sql('select * from data')
data.columns = ['楼盘名', 'data', '市', '开盘日期', '联系电话', '地址', '售卖状态', '房产类型', '售价', 'Tag']
data.drop('data', axis=1, inplace=True)

def h_task1():
    df1 = data.groupby(['市']).count()
    df2 = df1['Tag']
    tmp1 = pd.DataFrame(df2)
    n = tmp1.index.tolist()
    v = tmp1.values.tolist()
    c = []
    for i in range(len(n)):
        d = {"name":n[i], "value":v[i][0]}
        c.append(d)
    return c

def h_task2():
    df1 = data.groupby(['市']).count()
    a = df1.index.tolist()
    a[0]
    p = []
    for i in range(len(a)):
        df1 = data[data['市'] == a[i]]
        e = a[i].strip('市')
        df2 = df1['售卖状态'].value_counts()
        df3 = df2.index.tolist()
        df4 = df2.values.tolist()
        c = []
        for i in range(len(df3)):
            d = df4[i]
            c.append(d)
        g = e, c
        p.append(g)
    return p

def h_task3():
    counter = {}
    a = data['Tag'].values.tolist()
    for tag_str in a:
        tags = tag_str.split(' ')
        for tag in tags:
            counter[tag] = counter.get(tag, 0) + 1
    c = []
    value = []
    name = []
    for i in range(len(counter)):
        for item in counter.values():
            value.append(item)
        for item in counter.keys():
            name.append(item)
    for i in range(len(counter)):
        d = {"name": name[i], "value": value[i]}
        c.append(d)
    return c

def h_task4():
    df1 = data[data['售卖状态'] == '售完']
    df2 = df1[df1['售价'] != '售价待定']
    df3 = df2['市'].value_counts()
    shi1 = df3.index.tolist()
    i = []
    j = []
    for a in shi1:
        h = a.strip('市')
        b = df2[df2['市'] == a]
        c = b['售价'].values.tolist()
        e = 0
        for d in c:
            e += int(d)
        f = len(c)
        g = e / f
        j.append(str(h))
        i.append(str(round(g, 2)))
        pricing = {
            "city": j,
            "price": i
        }
        pricing_list = list(zip(pricing['city'], pricing['price']))
        pricing_list.sort(key=lambda x: float(x[1]), reverse=True)


    return {
        "name": [i[0] for i in pricing_list],
        "value": [i[1] for i in pricing_list]
    }

def h_task5():
    df1 = data[data['售卖状态'] == '在售']
    df2 = df1[df1['售价'] != '售价待定']
    df3 = df2['市'].value_counts()
    shi1 = df3.index.tolist()
    i = []
    j = []
    for a in shi1:
        h = a.strip('市')
        b = df2[df2['市'] == a]
        c = b['售价'].values.tolist()
        e = 0
        for d in c:
            e += int(d)
        f = len(c)
        g = e / f
        j.append(str(h))
        i.append(str(round(g, 2)))
        pricing = {
            "city": j,
            "price": i
        }
        pricing_list = list(zip(pricing['city'], pricing['price']))
        pricing_list.sort(key=lambda x: float(x[1]), reverse=True)


    return {
        "name": [i[0] for i in pricing_list],
        "value": [i[1] for i in pricing_list]
    }

def h_task6():
    df1 = data[data['售卖状态'] == '待售']
    df2 = df1[df1['售价'] != '售价待定']
    df3 = df2['市'].value_counts()
    shi1 = df3.index.tolist()
    i = []
    j = []
    for a in shi1:
        h = a.strip('市')
        b = df2[df2['市'] == a]
        c = b['售价'].values.tolist()
        e = 0
        for d in c:
            e += int(d)
        f = len(c)
        g = e / f
        j.append(str(h))
        i.append(str(round(g, 2)))
        pricing = {
            "city": j,
            "price": i
        }
        pricing_list = list(zip(pricing['city'], pricing['price']))
        pricing_list.sort(key=lambda x: float(x[1]), reverse=True)
    return{
        "name": [i[0] for i in pricing_list],
        "value": [i[1] for i in pricing_list]
    }

def h_task7():
    df1 = data['房产类型'].value_counts()
    n = df1.index.tolist()
    v = df1.values.tolist()
    l = []
    for a in range(len(n)):
        b = n[a]
        c = v[a]
        l.append({'name':b, 'value':c})
    return {'data':l}




if __name__=='__main__':
    with open('h_task1.json','w',encoding='utf-8') as f:
        json.dump(h_task1(),f,ensure_ascii=False)
    with open('h_task2.json', 'w', encoding='utf-8') as f:
        json.dump(h_task2(), f, ensure_ascii=False)
    with open('h_task3.json', 'w', encoding='utf-8') as f:
        json.dump(h_task3(), f, ensure_ascii=False)
    with open('h_task4.json', 'w', encoding='utf-8') as f:
        json.dump(h_task4(), f, ensure_ascii=False)
    with open('h_task5.json', 'w', encoding='utf-8') as f:
        json.dump(h_task5(), f, ensure_ascii=False)
    with open('h_task6.json', 'w', encoding='utf-8') as f:
        json.dump(h_task6(), f, ensure_ascii=False)
    with open('h_task7.json', 'w', encoding='utf-8') as f:
        json.dump(h_task7(), f, ensure_ascii=False)

