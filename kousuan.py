import random as r
import time as t
flag = True
huihe = 0
yes = 0
no = 0
print('口算\n游戏说明: 请口算出正确的答案，有十道题目。(除法很难！)\n')
 
a = input ('请说出你想做什么类型\n请回答加法，减法，乘法，除法 : ')
if (a == '加法') :
    fuhao = 1
elif (a == '减法') :
    fuhao = 2
elif (a == '乘法') :
    fuhao = 3
elif (a == '除法') :
    fuhao = 4
 
print('请拿出草稿纸和笔，做好准备!')
t.sleep(1)
print('3')
t.sleep(1)
print('2')
t.sleep(1)
print('1')
t.sleep(1)
print('GO!\n')
 
while flag :
    x = r.randint(21,40)
    y = r.randint(1,20)
    
    if (fuhao == 1) :
        ans = x+y
        answer = int(input(str(x) + '+' + str(y) + '=?\n请回答 : '))
        if (answer == ans) :
            print('答对了')
            yes += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
        else :
            print('很遗憾，答错了。正确答案是: ' + str(ans))
            no += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
 
    elif (fuhao == 2) :
        ans = x-y
        answer = int(input(str(x) + '-' + str(y) + '=?\n请回答 : '))
        if (answer == ans) :
            print('答对了')
            yes += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
        else :
            print('很遗憾，答错了。正确答案是: ' + str(ans))
            no += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
 
    elif (fuhao == 3) :
        ans = x*y
        answer = int(input(str(x) + '*' + str(y) + '=?\n请回答 : '))
        if (answer == ans) :
            print('答对了')
            yes += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
        else :
            print('很遗憾，答错了。正确答案是: ' + str(ans))
            no += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
 
    elif (fuhao == 4) :
        ans = x/y
        answer = float(input(str(x) + '/' + str(y) + '=?\n请回答 : '))
        if (answer == ans) :
            print('答对了')
            yes += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
        else :
            print('很遗憾，答错了。正确答案是: ' + str(ans))
            no += 1
            print('答对次数: ' + str(yes) + '\n答错次数: ' + str(no))
            huihe += 1
            print(str(huihe) + '/10\n')
 
    if (huihe == 10) :
        print('提问结束\n您总共答对了: ' + str(yes) + ' 答错了: ' + str(no))
        if (yes == 10) :
            print('Wow!全部答对!是个天才!')
        elif (yes >= 5 and yes != 10) :
            print('答对的挺多，很不错')
        elif (yes < 5 and yes != 0) :
            print('答错的有点多，继续加油!')
        elif (yes == 0) :
            print('怎么全答错了？我不敢相信!')
        flag = False
 
#制作:权家乐  想法提供:权家乐
#版权所有 侵权必究
