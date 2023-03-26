import random
number = random.randint(20,100)
err = 0
flag = True

print('猜数字')
print('游戏规则:输入一个20~100之间的数，若猜错10次则公布答案。')
print('_____________________________________________________')

while flag :
    answer = int(input('猜一个数字吧 : '))
	
    if (answer > 100) :
        print('有木有看规则？只能输入100以下的数！')
        print('________________________________________________')
    elif (answer < 20) :
        print('仔细看规则！输入一个20以上的数！')
        print('________________________________________________')
    elif (answer < number) :
        print('猜错了，猜的数字太小')
        err += 1
        print('错误次数:',str(err))
        print('________________________________________________')
    elif (answer > number) :
        print('猜错了，猜的数字太大')
        err += 1
        print('错误次数:',str(err))
        print('________________________________________________')
    elif (answer == number) :
        print('恭喜你，猜对了。正确数字就是:',str(number))
        print('你一共用了:',str(err + 1),'次才答对')
        flag = False

    if (err == 10) :
        print('你已猜错10次，正确答案是:',str(number))
        flag = False

#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
