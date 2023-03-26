flag = True
print('AA制计算器')
print('欢迎使用AA制计算器')
print('输入人数和数量，将为您计算出AA结果')
while flag :
    people = input('\n请输入人数： ')
    num = input('\n请输入平分物体的数量：')
    print('计算结果为' + str(int(num)/int(people)))
    answer = int(input('\n要继续计算吗？（0为不要，1为要）: '))
    if (answer == 0) :
        print('欢迎下次使用！')
        flag = False
    elif (answer == 1) :
        print('[程序继续]')
    else :
        print('默认为继续')

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
