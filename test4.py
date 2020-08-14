import cla

cla.ZhConversion.zh2Hant

str="我是徐聖凱"


for i in range(len(str)):
    try:
        print(cla.ZhConversion.zh2Hans[str[i]])
    except Exception as e:
        print(str[i])
    