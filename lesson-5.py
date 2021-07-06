user_input_1 = input("Введите сумму кредита: ")
user_input_2 = input("Процент кредита: ")
a = ['q','w','e','r','t','y','u','i','o','p','a',
     's','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
try:
    print((int(user_input_1)/100) * int(user_input_2))
except TypeError:
    print("0")
except ValueError:
    if user_input_2 or user_input_1 in str:
        print('0.00')
    elif user_input_2 or user_input_1 in float:
        print((float(user_input_1)/100) * float(user_input_2))
except Exception:
    print("0.0")
