# *_*coding:utf-8 *_*
# by oneskey
#购物车程序
#启动程序后让用户输入工资，然后打印商品列表
#允许用户根据商品编号购买商品
#用户可以一直购买商品，也可随时退出，退出时打印已购买的商品和余额

shopping_car=[]
products=[('iphone8',6888),
          ('macpro',14800),
          ('小米6',2499),
          ('coffee',31),
          ('book',80),
          ('nike shose',799),
          ]
salary=input("请输入您的工资：")
if  salary.isdigit():
    salary=int(salary)
while   True:
    #打印商品列表菜单
    print("----------商品列表----------")
    for index,v in  enumerate(products):
        print("%s.  %s  %s"%(index,v[0],v[1]))
    choie=input("请输入您要购买的商品编号：")
    if  choie.isdigit():
        choie=int(choie)
        if  choie>=-1 and choie   <=len(products):
            p_istm=products[choie]
            if  p_istm[1]<=salary:
                shopping_car.append(p_istm)
                salary-=p_istm[1]
                print("您已购买%s，还剩%s元。"%(p_istm,salary))
            else:
                print("您的钱不够哦，还剩下%s元"%(salary))
        else:
            print("您的商品不存在")
    elif    choie=="q"or"Q":
        print("---------已购买----------")
        for i   in shopping_car:
            print(i[0])
        print("您还剩下%s元"%(salary))
        exit()
    else:
        print("您的输入无效")
