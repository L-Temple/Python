import math
def jia(x, y):
    return x + y
def jian(x, y):
    return x - y
def cheng(x, y):
    return x * y
def chu(x, y):
    return x / y
def mi(x,y):
    return x**y
while True:
    print("选择运算：")
    print("1、相加","2、相减","3、相乘","4、相除","5、次方",
          "6、正弦","7、余弦","8、正切","9、对数","10、阶乘",
          "11、平方根")
    choice = input("输入你的选择(1/2/3/4/5/6/7/8/9/10/11):")
    calcul = ["6", "7", "8", "10", "11"]
    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))
    if choice == '1':
        print(num1, "+", num2, "=", jia(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", jian(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", cheng(num1, num2))
    elif choice == '4':
      print(num1, "/", num2, "=", chu(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", mi(num1, num2))
    elif choice == '6':
        print('sin(x)=',math.sin(num1))
    elif choice == '7':
        print('cos(x)=',math.cos(num1))
    elif choice == '8':
        print('tan(x)=', math.tan(num1))
    elif choice == '9':
        print(math.log(num1,num2))
    elif choice == '10':
        print('x的阶乘为', math.factorial(num1))
    elif choice == '11':
        print('x的平方根为', math.sqrt(num1))
    else:
        print("非法输入")