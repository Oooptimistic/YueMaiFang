from multiprocessing.dummy import Pool
from pypinyin import lazy_pinyin
from pyquery import PyQuery as pq
import re
import parsel
import pymysql
import requests
import time
# 延时
# sleep_time = random.randrange(2,5)
sleep_time= 1
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
# 配置数据库
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'yuemaifang',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor
}

# 数据库插入语句
def insertdate(name ,province , city, date, phone, addres, status, property_types, sellingPrice, tag):
    # 定义cursor 来操作数据库
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = """insert into """+(province)+"""(name, province, city ,date ,phone ,addres ,status ,property_types ,sellingPrice, tag) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (name, province, city, date, phone, addres, status, property_types, sellingPrice, tag))
    db.commit()
    db.close()

def createtable(province):
    # 定义cursor 来操作数据库
    db = pymysql.connect(**config)
    cursor = db.cursor()
    # 创表
    d_sql = "create table (\w+)"
    sql = """create table """ + (province) + """(
            name varchar(128) not null,
            province varchar(128) not null,
            city varchar(128) not null,
            date varchar(128) not null,
            phone varchar(128) not null,
            addres varchar(128) not null,
            status varchar(128) not null,
            property_types varchar(128) not null,
            sellingPrice varchar(128) not null,
            tag varchar(128) not null
        )"""
    try:
        cursor.execute(sql)
        print('已创建' + re.search(d_sql, sql).group(1) + '表')
    except:
        print(re.search(d_sql, sql).group(1) + '表已存在')
    print(sql)
    db.close()

def index_page(url):
    for i in range(0, 20):
        try:
            response = requests.get(url, headers=header)
            time.sleep(sleep_time)
            html_data = response.text
            selectors = parsel.Selector(html_data)
            pq_tag = pq(url)
            # 页面前五条有特殊样式
            if i < 5:
                name = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[2]/text()').get()
            else:
                name = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[1]/text()').get()
            date = selectors.xpath(
                '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[3]/text()').get()
            phone = selectors.xpath(
                '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[5]/text()').get()
            addres = selectors.xpath(
                '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[2]/text()').get()
            if i < 5:
                status = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[3]/span[1]/text()').get()
                property_types = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[3]/span[2]/text()').get()
            else:
                status = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[2]/span[1]/text()').get()
                property_types = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                    i + 1) + ']/a/div[2]/div[1]/span[2]/span[2]/text()').get()
            sellingPrice = selectors.xpath(
                '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/div/div/span/text()').get()
            tag = pq_tag(
                'body > div.content > div > div.maincon.clearfix >div.left.fl > div.listcon > ul > li:nth-child(' + str(
                    i + 1) + ') > a > div.text > div.tag.clearfix').children('span').text()
            if tag == "":
                tag = ("暂无标签")
            # 去除后缀新盘
            city = pq_tag('body > div.content > div > h3').text().strip('新盘')+'市'
            insertdate(name, province, city, date, phone, addres, status, property_types, sellingPrice, tag)
            print(
                  '宅名:' + name, '\n',
                  '省份:' + province, '\n',
                  '城市:' + city, '\n',
                  '开盘日期:' + date, '\n',
                  '联系方式:' + phone, '\n',
                  '地址:' + addres, '\n',
                  '销售状态:' + status, '\n',
                  '物业类型:' + property_types, '\n',
                  '价格:' + sellingPrice + '元/㎡', '\n',
                  '房产属性标签:' + tag
                )
        # 如果数据为空跳过当前条数继续下一条
        except pymysql.err.IntegrityError:
            continue

def two_page (two_url):
    # 控制条数
    a = 0
    i = 0
    while True:
        i += 1
        if a > 3:
            break
        elif i == 20:
            break
        else:
            print('continue次数', a)
            print('页面第', i, '条')
            response = requests.get(two_url, headers=header)
            html_data = response.text
            time.sleep(sleep_time)
            selectors = parsel.Selector(html_data)
            pq_tag = pq(two_url)
            try:
                # 页面前五条有特殊样式
                if i < 5:
                    name = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[2]/text()').get()
                else:
                    name = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[1]/text()').get()
                date = selectors.xpath(
                    '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[3]/text()').get()
                phone = selectors.xpath(
                    '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[5]/text()').get()
                addres = selectors.xpath(
                    '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/a/div[2]/div[2]/text()').get()
                if i < 5:
                    status = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[3]/span[1]/text()').get()
                    property_types = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[3]/span[2]/text()').get()
                else:
                    status = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[2]/span[1]/text()').get()
                    property_types = selectors.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(
                        i + 1) + ']/a/div[2]/div[1]/span[2]/span[2]/text()').get()
                sellingPrice = selectors.xpath(
                    '/html/body/div[2]/div/div[2]/div[1]/div[2]/ul/li[' + str(i + 1) + ']/div/div/span/text()').get()
                tag = pq_tag(
                    'body > div.content > div > div.maincon.clearfix >div.left.fl > div.listcon > ul > li:nth-child(' + str(
                        i + 1) + ') > a > div.text > div.tag.clearfix').children('span').text()
                if tag == "":
                    tag = ("暂无标签")
                # 去除后缀新盘
                city = pq_tag('body > div.content > div > h3').text().strip('新盘') + '市'
                insertdate(name, province, city, date, phone, addres, status, property_types, sellingPrice, tag)
                print(
                      '宅名:' + name, '\n',
                      '省份:' + province, '\n',
                      '城市:' + city, '\n',
                      '开盘日期:' + date, '\n',
                      '联系方式:' + phone, '\n',
                      '地址:' + addres, '\n',
                      '销售状态:' + status, '\n',
                      '物业类型:' + property_types, '\n',
                      '价格:' + sellingPrice + '元/㎡', '\n',
                      '房产属性标签:' + tag
                      )
                # 如果数据为空跳过当前条数继续下一条
            except pymysql.err.IntegrityError:
                a += 1
                continue

# 城市表
city_chinese = {'jiangmen':'江门', 'gz':'广州'
                , 'huizhou':'惠州', 'qingyuan':'清远', 'zhongshan':'中山', 'zhanjiang':'湛江', 'dongguan':'东莞'
                , 'heyuan':'河源', 'foshan':'佛山', 'shaoguan':'韶关', 'sz':'深圳'
                , 'maoming':'茂名', 'yangjiang':'阳江', 'yunfu':'云浮', 'zhuhai':'珠海'
                , 'zhaoqing':'肇庆'
                }

# 第一页url列表
url_list= []
for city_pinyin in city_chinese:
    city = city_chinese.get(city_pinyin)
    url = 'http://' + str(city_pinyin) + '.yuemaifang.com/loupan'
    url_list.append(url)

# 第2页到99页面url列表:
two_url_list=[]
for city_pinyin in  city_chinese:
    for page in  range(2, 100):
        two_url = 'http://'+str(city_pinyin)+'.yuemaifang.com/loupan/list-page'+str(page)+'.html'
        two_url_list.append(two_url)

if __name__ == '__main__':
    # 表名 pypinyin转换拼音
    province = ''.join(lazy_pinyin('data'))
    createtable(province)
    # 线程数
    pool = Pool(7)
    # 第一页多线程爬虫
    pool.map(index_page, url_list)
    # 第2页到99页多线程爬虫
    pool.map(two_page, two_url_list)
