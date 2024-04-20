def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Пожалуйста, введите целое число.")
def num4():
    print("\nВы попали в мир, полный загадок и волшебства!")
    print("Выберите своего персонажа:\n1.Мина \n2.Александр ")
    name_1 = get_integer_input("")
    balance = 50
    my_list = ["Мину", "Александра"]
    if name_1 == 1:
       print(f"\nВы будете путешествовать за {my_list[0]}. Баланс: {balance}")
       num()
    elif name_1 == 2:
       print(f"\nВы будете путешествовать за {my_list[1]}. Баланс: {balance}")
       num()
    else:
        print("Пожалуйста, выберите 1 или 2.")
        return num4()
def num():
    print("Выберите, куда хотели бы отправиться:\n1.Город\n2.Лес\n3.Горы")
    name_2 = get_integer_input("")
    if name_2 == 1:
        num1()
    elif name_2 == 2:
        num2()
    elif name_2 == 3:
        num3()
    else:
        print("Пожалуйста, выберите 1 или 2 или 3.")
        return num()
def num1():
    print("\nВы отправились в город")
    print("Пока вы шли, вы увидели раненного незнакомца. Поможете ему?\n1.Да\n2.Нет")
    name_3 = get_integer_input("")
    while name_3 != 1 and name_3 != 2:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
        name_3 = get_integer_input("")
    if name_3 == 1:
        print("\nВы помогли ему и он рассказал вам, что недалеко отсюда находиться лавка\nОтправитесь туда?\n1.Да\n2.Нет")
        name_4 = get_integer_input("")
        while name_4 != 1 and name_4 != 2:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
            name_4 = get_integer_input("")
        if name_4 == 1:
            print("\nВы добрались до лавки и заметили, что в ней продаются травы. Хотите купить их?\n1.Да\n2.Нет")
            answer = get_integer_input("")
            while answer != 1 and answer != 2:
                print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
                answer = get_integer_input("")
            if answer == 1:
                balance = 50 
                print(f"\nВаш баланс: {balance}")
                cena = {'1.Травы для восстановления здоровья': 100, '2.Травы для восстановления силы' : 25, '3.Травы для воскрешения': 50}
                for key,value in cena.items(): 
                    print(key, ':', value)
                answer_1 = get_integer_input("")
                while answer_1 != 1 and answer_1 != 2 and answer_1 != 3:
                    print("Неправильный выбор. Пожалуйста, введите 1 или 2 или 3.")
                    answer_1 = get_integer_input("")
                if answer_1 == 1:
                    print("\nУ вас не хватает монет. Продавец разозлился и сильно ударил вас по голове.\nВы умерли от кровоизлияния.\nИгра закончена.")
                elif answer_1 == 2:
                    balance = balance - 25
                    print(f"\nВы купили травы для восстановления силы, но оно оказалось неисправным. Самое бесполезное приобритение.\nВаш баланс: {balance}")
                    print("Вы вышли на улицу и прочесали весь город, но ничего не нашли, поэтому решили вернуться домой.\nПоздравляю, вы избежали все опасные ситуации и прошли игру!")
                elif answer_1 == 3:
                    balance = balance - 50
                    print(f"\nВаш баланс: {balance}. Вы купили травы для восрешения и решили испробовать, но они оказалось отравленными, и вы умерли.\nИгра закончена")
            elif answer == 2:
                print("\nВас не заинтересовали травы, и вы ушли из лавки")
                print("Вы прочесали весь город, но ничего не нашли, поэтому решили вернуться домой.\nПоздравляю, вы избежали все опасные ситуации и прошли игру!")
        elif name_4 == 2:
            print("\nВы решили пойти в лес")
            num2()      
    elif name_3 == 2:
        print("\nВы забрали его деньги и решили пойти в лес ")
        num2()

def num2():
    print("\nПока вы шли в лес, в далеке вы увидели заброшенный дом.\nОтправитесь туда?\n1.Да\n2.Нет")
    name_5 = get_integer_input("")
    while name_5 != 1 and name_5 != 2:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
        name_5 = get_integer_input("")
    if name_5 == 1:
        print("\nПеред вами предстал огромный мужчина по имени Геннадий.")
        print("Он предложил купить вам меч. Согласитесь покупать?\n1.Да\n2.Нет")
        name_6 = get_integer_input("")
        while name_6 != 1 and name_6 != 2:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
            name_6 = get_integer_input("")
        if name_6 == 1:
            print("\nУ вас не хватает монет. Геннадий разгневался и схватил вас. Он запер вас в доме, навсегда...\nИгра закончена. ")
        elif name_6 ==2:
            print("\nГеннадий разгневался и схватил вас. Он запер вас в доме.\nИгра закончена.")
    elif name_5 == 2:
        print("\nВы продолжили своё путешествие.")
        num3()

def num3():
    print("\nВы отправились в горы. По дороге наверх, вы обнаружили сундук. Открыть его?\n1.Да\n2.Нет")
    name_7 = get_integer_input("")
    while name_7 != 1 and name_7 != 2:
        print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
        name_7 = get_integer_input("")
    if name_7 == 1:
        balance = 50
        balance = balance + 50
        print(f"\nВ сундуке были деньгии. Баланс: {balance}")
        print("После долгого подъёма вы наконец-то наверху. Хотите отдохнуть?\n1.Да\n2.Нет")
        name_8 = get_integer_input("")
        while name_8 != 1 and name_8 != 2:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
            name_8 = get_integer_input("")
        if name_8 == 1:
            print("\nВы уснули в горах.\nИ пока вы спали вас укусила змея. В результате вы погибли.\nИгра закончена.")
        elif name_8 == 2:
            print("\nВы продолжили своё путешествие")
            num1()
    elif name_7 == 2:
        print("\nВы продолжили своё путешествие по горам.")
        print("После долгого подъёма вы наконец-то наверху. Хотите отдохнуть?\n1.Да\n2.Нет")
        name_9 = get_integer_input("")
        while name_9 != 1 and name_9 != 2:
            print("Неправильный выбор. Пожалуйста, введите 1 или 2.")
            name_9 = get_integer_input("")
        if name_9 == 1:
            print("\nВы уснули в горах. И пока вы спали вас укусила змея. В результате вы погибли.\nИгра закончена.")
        elif name_9 == 2:
            print("\nВы продолжили своё путешествие")
            num1()


def main():
    print("Здравствуйте, хотите сыграть в игру?\n1.Да\n2.Нет")
    name = get_integer_input("")
    if name == 1:
        num4()
    elif name == 2:
        print("Всего хорошего! Обязательно найдите время, чтобы пройти эту замечательную игру.")
    else:
        print("Пожалуйста, выберите 1 или 2.")
        return main()
main()