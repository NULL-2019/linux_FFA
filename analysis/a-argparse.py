'''
argparse 模块可以让人轻松编写用户友好的命令行接口。
程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。
argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。
'''
#1-引入模块
import argparse
# 2-建立解析对象
parser = argparse.ArgumentParser()

# -增加属性：给xx实例增加一个aa属性 # xx.add_argument(“aa”)

#parser.add_argument('__steps',type= int ,default= 1000)
parser.add_argument('--steps',type=int,default=10000)#迭代次数


parser.add_argument('--name',type=str,default="zheng")
parser.add_argument('--last name',type=str,default="Qiang")

#设置参数

# 4 属性给与args实例： 把parser中设置的所有"add_argument"给返回到args子类实例当中， 那么parser中增加的属性内容都会在args实例中，使用即可

args = parser.parse_args()

print(args)



