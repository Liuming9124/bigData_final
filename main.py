
import matplotlib.pyplot as plt
import pandas as pd

m1 = pd.read_csv('./01.csv',index_col=0)
m2 = pd.read_csv('./02.csv',index_col=0)
m4 = pd.read_csv('./04.csv',index_col=0)
m5 = pd.read_csv('./05.csv',index_col=0)
m6 = pd.read_csv('./06.csv',index_col=0)
m7 = pd.read_csv('./07.csv',index_col=0)
m8 = pd.read_csv('./08.csv',index_col=0)
# empty = pd.read_csv('./ety.csv',index_col=0)

data = {'1':m1,'2':m2, '4':m4,'5':m5,'6':m6,'7':m7,'8':m8}
# '3': empty,

city = ['全市','大廈','透天厝','中西區','安平區','南區','北區','永康區','安南區','東區','仁德區','歸仁區','南科區域','善化區','新市區','佳里區','新營區']
eng_city = ['all city','building','house','central and western district','anping district','south district','north district','yongkang district','annan district','east district','rende district','gui ren district','nanke district','shan hua district','xin shi district','jiali district','xin ying district']

datas = {'全市':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'大廈':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'透天厝':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'中西區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'安平區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'南區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'北區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'永康區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'安南區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'東區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'仁德區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'歸仁區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'南科區域':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'善化區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'新市區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'佳里區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]},'新營區':{'住宅價格月指數':[],'月變動率':[],'季變動率':[],'年變動率':[]}}


for i in data:
    for j in city:
        datas[j]['住宅價格月指數'].append(data[i].loc[j,'住宅價格月指數'])
        datas[j]['月變動率'].append(data[i].loc[j,'月變動率'])
        datas[j]['季變動率'].append(data[i].loc[j,'季變動率'])
        datas[j]['年變動率'].append(data[i].loc[j,'年變動率'])


# print(datas.keys())
# print(datas['全市'].keys())
# print(datas['全市']['住宅價格月指數'])

count = int(input('input count: '))

find = ['住宅價格月指數','月變動率','季變動率','年變動率']
for i in find:
    print(f'{find.index(i)}:{i}')
showData = int(input('input number: '))

while count>0:
    count-=1

    for i in city:
        print(f'{city.index(i)}:{i}')

    zone = int(input('input number: '))

    # 繪製曲線圖
    plt.plot(datas[city[zone]][find[showData]], label=eng_city[zone])
    months = ['Jan', 'Feb', 'Apr', 'May', 'Jun', 'Jul', 'Aug'] #  , 'Mar'
    plt.xticks(range(len(months)), months)

# 添加標題和標籤
if showData==0:
    plt.title('Citywide housing price monthly index')
    plt.ylabel('housing price index')
elif showData==1:
    plt.title('Citywide housing price monthly change rate')
    plt.ylabel('change rate')
elif showData==2:
    plt.title('Citywide housing price quarterly change rate')
    plt.ylabel('change rate')
elif showData==3:
    plt.title('Citywide housing price annual change rate')
    

plt.xlabel('month')

plt.legend()

# 顯示圖形
plt.show()

# print(data['1'].keys())
