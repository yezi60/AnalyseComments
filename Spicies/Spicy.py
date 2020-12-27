# encoding=utf-8
import requests
from os import path
import re
import json
import csv
import time
import jieba
import numpy
import os
import random
from PIL import Image
from wordcloud import WordCloud

from Spicies.Get_Id import get_Id

# json数据接口，需要两个恶参数，offset和limit，offset的增量为20，limit的固定为20，刚好抓取网页评论的20条评论
# http://music.163.com/api/v1/resource/comments/R_SO_4_1299557768?offset=40&limit=20

# 网页请求
def get_one_comment(offset, song_id):
    headers={
        'Cookie':'_ntes_nnid=cdc3b9982a7880e06800c0b35ac65aa1,1597759672725; _ntes_nuid=cdc3b9982a7880e06800c0b35ac65aa1; s_n_f_l_n3=bf7c7c8ed7c717fd1599669697023; _antanalysis_s_id=1599669701613; usertrack=ezq0J19/FIIC3WRvCCIUAg==; NMTID=00ODjYdWlGiAIPWAkJPnFQ3q-vXDywAAAF1Rhj1pA; playerid=68277340; P_INFO=yezidexiatian60@163.com|1603972436|1|study|00&99|null&null&null#shh&null#10#0#0|&0||yezidexiatian60@163.com; NTES_SESS=Coa.duao3RRSgfcfdQFbXqllgb5sD3XYbfJn_uhP9oPvMmy6MT5QSOxxJEgR6BodCBqIvG6ok0VVXqxxouA00LSOmtNJzM7bftxoxSg5gdZmKzjLLBw9OiFN23J_83hlTFTdNt5BItQHgr_y99yaYEjyK4BLbgr0nEJOrTv35wa8mLfmrh3c0XlbSaqcBh9I1cV_ZkkJmSH87e6LOmF2vJPRf; S_INFO=1604036956|1|0&0##|yezidexiatian60; NTES_CMT_USER_INFO=276314467%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0gu3Bz%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CeWV6aWRleGlhdGlhbjYwQDE2My5jb20%3D; WEVNSM=1.0.0; WNMCID=fhvqju.1605532049075.01.0; WM_TID=dbFtyj7EDk5FUVFQFFcuIFVTqSKoMNFg; ntes_kaola_ad=1; _iuqxldmzr_=32; ne_analysis_trace_id=1608991682586; vinfo_n_f_l_n3=bf7c7c8ed7c717fd.1.0.1599669697022.0.1608991762595; JSESSIONID-WYYY=cqonEdVs1ZRX%2BJq14ZtnoaA2QeXlOkMqBWXSx7Od%2FGtEGf2J1W4Nwd3g83Xp%5CrvknzCCaV0srl%2B6sX8%2F2mAs72O7KEJwpBBP5BFKxXwUB%2BEw6Tgd%2F%2BRrfHBBn6UuIopzBB8bxu7DIKw8GEHcJ6kjRueop2RFFrhn%2Byn73R5edS%5CpygYY%3A1609081632356; WM_NI=yvRGdkpcMuACeXfD9H1tOfawYR8W1LAeIu5qg3pGbmlspDv7VEA2u5fHgazKJMpp2oUNpMuqZokMH%2Bm4hb29iaGaHAN1iR0dieyDGCv8y9TqjjEQWJFfI2rmZnqMVkSuNGo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82d86f838de5bbdc7bbceb8ba7d15f829a8eabf46e9aa9b98ed46ef39d98d9cf2af0fea7c3b92abbaa9ea8e761b4bd8396c449a788aaa5bc44f3ac8187e47d9b8ef8b8b44883bb8796b87ba5edc0a8e167b0adc0a5f53d969b8fd3f83fa698a982f9418a93c091b1659792c0aef87b9ab1a5aecb21afeca883b133abbf8982cb4b8eefa7b3b370abbbb7a5c649b6e8b7dad77baab68bb2d64286ba87d3f1679ab2bfaed56191ab82a8ee37e2a3',
        #'Cookie':'_iuqxldmzr_=32; _ntes_nnid=bdaab01e87ee929b3a9a91ea44b5cd45,1534172699282; _ntes_nuid=bdaab01e87ee929b3a9a91ea44b5cd45; __utmc=94650624; WM_TID=M4E4ToHGUg4EetTbOjxEC5J%2BuODh%2B0jj; abt=66; WM_NI=cRw1E4mJtjv9dwKem8xCMaYzUgNNyu8qqM25igmzBYDj%2FJGjHnYTJFFFqen2XIq%2FlCdRUdQxmdIvxSl84%2BvraOwnH1lJboEwOdL6UrZhnx030tzRng9NfOIBNXgIUx7GMUI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6b15cf88bb8ade56a8eb48291f97ca5b9e1d2c45bf6ed9cb9e659b1be8e89ca2af0fea7c3b92aa18eb9d2c840af96bc8bf533a8a98586f034bc9d8382dc7297b982affc7ffcafbfaeb13fabb9a39bc15388b6e1abc6628cb297b5c94e869abf86ed3a9c97bfd0ef49a88e9b85d474afbc8797fb59b0e8fcccf57aa391b98fcb3bb096ae90c87d8dbc84d7d87a9ab8a299b339f4acb6b3ed6dfb92aab0cc4a8e88a9aad874f59983b6cc37e2a3; __utma=94650624.827593374.1534172700.1535852507.1535857189.3; __utmz=94650624.1535857189.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=kgbbgMKEcRf18SvvxZVqNTmWZD%2Fdn8BpA%2F7aMH7vv4mSpiDaE%5CfkC5xPu5hFv0nk5X7PpvlEJJ97%2BC3WyE5Qv50EW%2FdNPQQPenibqq%2F5IyHkuuMlCTkpkb7TRMl9oBEdFi68ktMI8m%2F5Ilyub4P204bpG0qBv4yx9vvw8CmCJ%2B9vCaSd%3A1535859527007; __utmb=94650624.7.10.1535857189',
        'Referer':'https://music.163.com/song?id='+str(song_id),
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 字符串拼接
    url='http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(song_id)+'?offset='+str(offset)+'&limit=20'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print('出错啦！')
        return None

# 解析数据
def parse_json_data(contents):
    if contents:
        # 编码格式转换
        #print(contents)
        contents = contents.decode('utf-8')
        # api接口返回的数据是json格式，把json格式转换为字典结构，获取评论信息
        comments = json.loads(contents)['comments']
        for comment in comments:
            content = comment['content']
            nickname = comment['user']['nickname']
            timeArray = time.localtime(comment['time']/1000)
            style_time = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
            yield{
                'time': style_time,
                'nickname': nickname,
                'comment': content
            }
        # print(nickname+','+content+','+style_time)

# csv保存数据
def save_csv_comments(messages,i):
    # encoding=utf_8_sig只能转换中文乱码和字母乱码，不能支持数字的乱码
    with open('comment_csv.csv', 'a', encoding='utf_8_sig', newline='')as f:
        csvFile = csv.writer(f)
        if i == 0:
            csvFile.writerow(['评论时间','昵称','评论内容'])
        csvdatas = []
        for message in messages:
            csvdata = []
            csvdata.append(message['time'])
            csvdata.append(message['nickname'])
            csvdata.append(message['comment'].replace('\n', ''))
            csvdatas.append(csvdata)
        csvFile.writerows(csvdatas)

# 读取csv文件的评论内容的一列
def read_csvFile(fileName):
    dir_p = "E:\\PycharmProjects\\Pybasic\\Del\\"
    word_path = os.path.join(dir_p,fileName)
    with open(word_path, 'r', encoding='utf_8_sig') as f:
        # 因为此csv文件并非二进制文件， 只是一个文本文件
        readerCSV = csv.reader(f)
        comment_column = [row[2] for row in readerCSV]
        return comment_column

# 词云生成
def make_word_cloud(text):
    comment_text = jieba.cut(''.join(text[1:]))
    print(comment_text)
    # list类型转换为str类型
    comment_text = ''.join(comment_text)
    #pattern = re.compile(r'(\[)(.*)(\])')
    #comment_text = pattern.sub(r'',comment_text)
    comment_text = re.sub('\[(.*?)\]','',comment_text)

    c_t = jieba.cut(comment_text, cut_all=False)
    comment_text = ""
    for ct in c_t:
        comment_text += ct + " "
    print(comment_text)

    stopwords = get_stopwords()

    animal = numpy.array(Image.open('E://PycharmProjects//Pybasic//Spicies//timg_meitu_1.jpg'))
    wc = WordCloud(scale=4, color_func= random_color_func,font_path='C:/Windows/Fonts/simsun.ttc', background_color="white", width=900, height=900, max_words=300, mask=animal, stopwords=stopwords)
    # 生成词云
    wc.generate(comment_text)
    #保存到本地
    wc.to_file("word_cloud.png")

#设置停用词
def get_stopwords():
    dir_path = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #获取停用词的路径
    #stopwords_path = os.path.join(dir_path,"cn_stopwords.txt")
    dir_p = "E:\\PycharmProjects\\Pybasic\\Spicies\\"
    stopwords_path = os.path.join(dir_p,"cn_stopwords.txt")
    #创建set集合来保存停用词
    stopwords = set()
    #读取文件
    f = open(stopwords_path,"r",encoding="utf-8")
    line_contents = f.readline()
    while line_contents:
        #去掉回车
        line_contents = line_contents.replace("\n","").replace("\t","").replace("\u3000","")
        stopwords.add(line_contents)
        line_contents = f.readline()
    return stopwords

#设置词云颜色
def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h1 = random.randint(0, 35)
    #h2 = random.randint(200, 220)
    h3 = random.randint(300, 340)
    cl = [h1, h3]
    h = cl[random.randint(0, 1)]
    #s = int(100.0 * 255.0 / 255.0)
    #l = int(100.0 * float(random.randint(0, 120)) / 255.0)
    s = 80
    l = 45
    return "hsl({}, {}%, {}%)".format(h, s, l)


def dele(strs):
    file_name = "E://PycharmProjects//Pybasic//Del//"+str(strs)
    if os.path.exists(file_name):
        os.remove(file_name)


# 程序主入口
def get_all(offset, i, song_id):

    save_csv_comments(parse_json_data(get_one_comment(offset, song_id)), i)

#if __name__ == "__main__":



def run_spicy(name):
    dele("word_cloud.png")
    dele("comment_csv.csv")
    #name = input("请输入歌曲名字：")
    song_id = get_Id(name)

    print(song_id)

    for i in range(200):
        get_all(i*20, i, song_id)
    make_word_cloud(read_csvFile('comment_csv.csv'))
