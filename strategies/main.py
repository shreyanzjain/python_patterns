from mathContext import Context
from add import MathAdd
from sub import MathSub
from mul import MathMul


class MainApp:
    context = Context()
    a_in = int(input(f"Enter a number: "))
    b_in = int(input(f"Enter another number: "))
    stratChc = input(f"1.Add\n2.Sub\n3.Multiply\nChoose a strategy: ")

    if stratChc == '1':
        context.setStrategy(MathAdd)
    elif stratChc == '2':
        context.setStrategy(MathSub)
    elif stratChc == '3':
        context.setStrategy(MathMul)
    else:
        print(f"Invalid Choice")

    print(context.executeStrategy(a=a_in, b=b_in))
