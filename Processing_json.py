import json

# 打开保存的json文件
with open('1.json', 'r', encoding="utf-8")as f:
    data = json.load(f)


# 利用层级关系处理数据
data = data["data"]["continent"]
Asia = data[0]["country"]
Europe = data[1]["country"]
NorthAmerica = data[2]["country"]
SouthAmerica = data[3]["country"]
Africa = data[4]["country"]
Oceania = data[5]["country"]
country = Asia + Europe + NorthAmerica + SouthAmerica + Africa + Oceania
print(country)

countryList = []
list = []


for i in range(len(country)):
    name = country[i]["provinceName"]
    value = country[i]["confirmedCount"]

# 将国家名称中文转英文
    with open('country.json', 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    try:
        countryDict = {}
        countryDict["name"] = data2[name]
        countryDict["value"] = value
        countryList.append(countryDict)
    except:
        list.append(name)
print(countryList)
countryList1 = str(countryList).replace("'","")
print(countryList1)
# 数据保存
with open("global_epidemic_statistics_deal1.json", 'w', encoding="utf-8") as f:
    json.dump(countryList1, f)
    print("保存成功！")