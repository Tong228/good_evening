class Player:
    money = 1000
    name = ""
    inventory = []
    progress = set()


def Malibu():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Напротив тебя магазин Малибу")
        print("\nВыберите вариант ответа:"
              "\n1.Войти в магазин"
              "\n2.Идти на налево"
              "\n3.Идти направо")

        UserInput = input()

        if UserInput == "1":
            In_Malibu()
        elif UserInput == "2":
            Pizza()
        elif UserInput == "3":
            Druzjba()
        else:
            print("Пожалуйста введите цифры")


def In_Malibu():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print(f"Ты в магазине Малибу.И что тебе тут надо?")
        print("\nВыберите вариант ответа:"
              "\n1.Выйти из магазина"
              "\n2.Купить что-нибудь вкусное")

        UserInput = input()

        if UserInput == "1":
            Malibu()
        elif UserInput == "2":
            In_Malibu_Buy()
        else:
            print("Пожалуйста введите цифры")


def In_Malibu_Buy():
    options = ["1", "2"]
    UserInput = ""
    while UserInput not in options:
        print("Из вкусного в магазине только птичье молоко. Божечки, они доят птиц???"
              f"\n Стоит этот деликатес 500 рублей. У тебя с собой {Player.money} рублей")
        print("\nВыберите вариант ответа:"
              "\n1.Ну уж нет, это какое-то варварство!"
              "\n2.Покупаю")
        UserInput = input()
        if UserInput == "1":
            In_Malibu()
        elif UserInput == "2":
            if Player.money < 500:
                print("Оу, к сожалению денег не хватате(")
                In_Malibu()
            else:
                Player.money -= 500
                Player.inventory.append("Конфеты 'Птичье молоко'")
                print("Конфеты у тебя, надеюсь оно того стоило")
                In_Malibu()


def Pizza():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Напротив тебя Пиццерия")
        print("\nВыберите вариант ответа:"
              "\n1.Войти в пиццерию"
              "\n2.Идти на налево"
              "\n3.Идти направо")

        UserInput = input()

        if UserInput == "1":
            In_Pizza()
        elif UserInput == "2":
            BusStation()
        elif UserInput == "3":
            Malibu()
        else:
            print("Пожалуйста введите цифры")


def In_Pizza():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Заходя в Пиццерию в замечаешь в дальнем углу двух своих друзей - Ивана и Степана")
        print("\nВыберите вариант ответа:"
              "\n1.Подойти к друзьям"
              "\n2.Выйти из пиццерии")

        UserInput = input()

        if UserInput == "1":
            In_Pizza_Dialog()
        elif UserInput == "2":
            Pizza()
        else:
            print("Пожалуйста введите цифры")


def In_Pizza_Dialog():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print(f"\nИван: О! Привет {Player.name}, давненько не виделись. А мы тут со Стёпкой последний день отмечаем"
              f"\nСтепан: Да, вот решили немного покуражиться, пиццы поесть. Хочешь пиццы?")
        if Player.inventory == ["Конфеты 'Птичье молоко'"]:
            print("\nВыберите вариант ответа:"
                  "\n1.Последний день?"
                  "\n2.Да, конечно хочу, а с чем пицца?"
                  "\n3.Ребят, будете конфеты птичье молоко?")
        else:
            print("\nВыберите вариант ответа:"
                  "\n1.Последний день?"
                  "\n2.Да, конечно хочу, а с чем пицца?")

        UserInput = input()

        if UserInput == "1":
            print(f"\nИван: Да, завтра ведь всё, все разъедутся кто куда, кто учиться, кто работать")
            print("\nВыберите вариант ответа:"
                  "\n1.И что, мы теперь не сможем гулять, ходить на море и... теперь не будет так как раньше?"
                  "\n2.Эх.. а с чем пицца?")
            UserInput = input()
            if UserInput == "1":
                print(f"\nИван: Да, к сожалению так, {Player.name}"
                      f"\n Но пока ещё все в городе, сбегай к ним, поговори. А мы пока тут посидим")
                print("\n Ты выходишь из пиццерии")
                Player.progress.add(1)
                Pizza()
            elif UserInput == "2":
                print("\nСтепан: Тут пару кусочков пиццы '4 сыра ' осталось, угощайся")
                print(f"\n{Player.name}: Спасибо")
                Pizza()
            else:
                print("Пожалуйста введите цифры")
        elif UserInput == "2":
            print("\nСтепан: Тут пару кусочков пиццы '4 сыра ' осталось, угощайся")
            print(f"\n{Player.name}: Спасибо")
            Pizza()
        elif UserInput == "3":
            print("\nИван: Птичье молоко? Нет уж, спасибо"
                  "\nСтепан: Да, я пожалуй откажусь")
            In_Pizza_Dialog()
        else:
            print("Пожалуйста введите цифры")


def BusStation():
    options = ["1", "2"]
    UserInput = ""
    while UserInput not in options:
        print("Пройдя налево ты видишь автобусную остановку. Неужели пора уезжать?")
        print("\nВыберите вариант ответа:"
              "\n1.Да,тут больше нечего делать"
              "\n2.Ну уж нет, у меня ещё есть дела")

        UserInput = input()

        if UserInput == "1":
            if len(Player.progress) == 4:
                end_gud()
            else:
                end_norm()
        elif UserInput == "2":
            Pizza()

        else:
            print("Пожалуйста введите цифры")


def Druzjba():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Ты приходишь к ресторану 'Дружба'")
        print("\nВыберите вариант ответа:"
              "\n1.Войти в ресторан"
              "\n2.Идти на налево"
              "\n3.Идти направо")

        UserInput = input()

        if UserInput == "1":
            In_Druzjba()
        elif UserInput == "2":
            Malibu()
        elif UserInput == "3":
            Cinema()
        else:
            print("Пожалуйста введите цифры")


def In_Druzjba():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Заходя в 'Дружбу', ты  замечаешь своих друзей - Егора и Юлю")
        print("\nВыберите вариант ответа:"
              "\n1.Подойти к друзьям"
              "\n2.Выйти из ресторана")

        UserInput = input()

        if UserInput == "1":
            In_Druzjba_Dialog()
        elif UserInput == "2":
            Druzjba()
        else:
            print("Пожалуйста введите цифры")


def In_Druzjba_Dialog():
    options = ["1", "2"]
    UserInput = ""
    while UserInput not in options:
        print(f"\nЕгор: Ах, какие люди.Привет {Player.name}, а мы тут проводы устраиваем, хочешь с нами?"
              f"\nЮля: Привет")
        if Player.inventory == ["Конфеты 'Птичье молоко'"]:
            print("\nВыберите вариант ответа:"
                  "\n1.Какие ещё проводы?"
                  "\n2.Ребят, будете конфеты птичье молоко?")
        else:
            print("\nВыберите вариант ответа:"
                  "\n1.Какие ещё проводы?")

        UserInput = input()

        if UserInput == "1":
            print(f"\nЕгор: В армейку меня забирают.Так что увидимся ещё не скоро ")
            print("\nВыберите вариант ответа:"
                  "\n1.Летом? Получается никаких больше тусовок не будет?"
                  "\n2.Эх.. я пожалуй пойду")
            UserInput = input()
            if UserInput == "1":
                print(f"\nЕгор: Да, к сожалению так {Player.name}.Когда-нибдуь мы обязательно встретимся снова"
                      f"\n Но пока ещё все в городе, сбегай к ним, поговори. А мы пока тут посидим")
                print("\n Ты выходишь из ресторана")
                Player.progress.add(2)
                Druzjba()
            elif UserInput == "2":
                print("\nЕгор: Да, сходи к остальным, пока ещё никто не уехал и это .. Удачи")
                print(f"\n{Player.name}: Спасибо")
                Druzjba()
            else:
                print("Пожалуйста введите цифры")
        elif UserInput == "2":
            print(f"\nЕгор: Птичье молоко? Нет спасибо")
            In_Druzjba_Dialog()
        else:
            print("Пожалуйста введите цифры")


def Cinema():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Пройдя направо ты приходишь к Кинотеатру."
              "\nПохоже оттуда выходит твой друг.")
        print("\nВыберите вариант ответа:"
              "\n1.Подойти к другу"
              "\n2.Идти налево"
              "\n3.Идти вперёд")

        UserInput = input()

        if UserInput == "1":
            Cinema_Dialog()
        elif UserInput == "2":
            Druzjba()
        elif UserInput == "3":
            Osaka()
        else:
            print("Пожалуйста введите цифры")


def Cinema_Dialog():
    options = ["1", "2"]
    UserInput = ""
    while UserInput not in options:
        print(f"\nКостя: О, {Player.name}, это ты? Привет, а ты чего тут?")
        if Player.inventory == ["Конфеты 'Птичье молоко'"]:
            print("\nВыберите вариант ответа:"
                  "\n1.Да так, мимо прохожу. Как у тебя дела?"
                  "\n2.Да так, мимо прохожу. Птичье молоко будешь?")
        else:
            print("\nВыберите вариант ответа:"
                  "\n1.Да так, мимо прохожу. Как у тебя дела?")

        UserInput = input()

        if UserInput == "1":
            print(f"\nКостя: Всё хорошо, завтра улетаю в другой город учиться.Так что встреимся ещё не скоро")
            print("\nВыберите вариант ответа:"
                  "\n1.Уже завтра? И мы этим летом больше не соберёмся как раньше?"
                  "\n2.Эх.. я пожалуй пойду")
            UserInput = input()
            if UserInput == "1":
                print(f"\nКостя: Да, к сожалению так {Player.name}.Настала пора взрослеть, создавать свою собственную "
                    f"жизнь. "
                    f"\n Это может показаться грустным, но все самое лучшее ещё впереди. "
                    f"\n Я очень рад что провёл свои подростковые годы вместе с тобой. А теперь мне пора идти, "
                    f"счастливо!")
                print(f"\n{Player.name}: Спасибо за такие слова, пока!")
                Player.progress.add(3)
                Cinema()
            elif UserInput == "2":
                print("\nКостя: Да, сходи к остальным, пока ещё никто не уехал")
                print(f"\n{Player.name}: Спасибо")
                Player.progress.add(3)
                Cinema()
            else:
                print("Пожалуйста введите цифры")
        elif UserInput == "2":
            print("\nКостя: Не очень их люблю, но спасибо что предложила")
            Cinema_Dialog()
        else:
            print("Пожалуйста введите цифры")


def Osaka():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Пройдя вперёд ты приходишь к сушебару 'Осака'")
        print("\nВыберите вариант ответа:"
              "\n1.Войти в Осаку"
              "\n2.Пойти назад")

        UserInput = input()

        if UserInput == "1":
            In_Osaka()
        elif UserInput == "2":
            Cinema()
        else:
            print("Пожалуйста введите цифры")


def In_Osaka():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print("Заходя в 'Осаку', ты  замечаешь своих друзей которые тут работают- Макса и Марка")
        print("\nВыберите вариант ответа:"
              "\n1.Подойти к друзьям"
              "\n2.Выйти из ресторана")

        UserInput = input()

        if UserInput == "1":
            In_Osaka_Dialog()
        elif UserInput == "2":
            Druzjba()
        else:
            print("Пожалуйста введите цифры")


def In_Osaka_Dialog():
    options = ["1", "2", "3"]
    UserInput = ""
    while UserInput not in options:
        print(f"\nМакс: О, {Player.name}, ты какими судьбами тут?"
              f"\nМарк: {Player.name} Здарова!")
        if Player.inventory == ["Конфеты 'Птичье молоко'"]:
            print("\nВыберите вариант ответа:"
                  "\n1.Привет ребятки, покормите меня?"
                  "\n2.Я пожалуй пойду"
                  "\n3.Друзья, птичье молоко будете?")
        else:
            print("\nВыберите вариант ответа:"
                  "\n1.Привет ребятки, покормите меня?"
                  "\n2.Я пожалуй пойду")

        UserInput = input()

        if UserInput == "1":
            print(
                f"\nМакс: Конечно покормим, присаживайся. Последний день работаем , так что за счёт заведения")
            print("\nВыберите вариант ответа:"
                  "\n1.Последний день? Вы увольняетесь?"
                  "\n2.Эх ладно, я пожалуй пойду")
            UserInput = input()
            if UserInput == "1":
                print(
                    f"\nМакс: Да,  {Player.name}.Мы с Марком уезжаем учиться, так что увидимся не скоро"
                    f"\nМарк: Надо потихоньку семью строить, машину купить ну и так далее"
                    f"\nМакс: Ты бы сначала на права сдал, машину он хочет"
                    f"\nМарк: Дай помечтать немного, права само собой разумеющееся.{Player.name}, вот твои "
                    f"роллы.Приятного))")
                print(f"\n{Player.name}: Спасибо")
                Player.progress.add(4)
                Osaka()
            elif UserInput == "2":
                Osaka()
            else:
                print("Пожалуйста введите цифры")
        elif UserInput == "2":
            Osaka()
        elif UserInput == "3":
            print("\nМакс: Конфеты эти? Неее, я не буду"
                  "\nМарк: Я тоже откажусь, спасибо")
            In_Osaka_Dialog()

        else:
            print("Пожалуйста введите цифры")

def end_gud():
    print("\nСпасибо моим друзьм. Грустно прощаться с беззаботной жизнью, "
          "\n но пора переходить в взрослый мир, бороться, сталкиваться с неизвестностью, достигать высот."
          "\n Ты уезжаешь из этого города, из свеого детства.")
    print("Твой смелый путь в незвестность только начинается...")
    input("\nНАЖМИТЕ ЛЮБУЮ КНОПКУ ДЛЯ ВЫХОДА")
def end_norm():
    print(
        "\nТы уежаешь из этого города. Не зная зачем и за что , ты идёшь в неизвестность.Твой путь "
        "начинается...")
    input("\n////НАЖМИТЕ ЛЮБУЮ КНОПКУ ДЛЯ ВЫХОДА////")

def start():
    print("Ты находишься в центре оживлённого города.")
    print("Совсем рядом находится автобусная остановка, ")
    print("В далеке видно большой жёлтый кран на котором написнао 'Звезда',")
    print("А твой взор падает на информационное табло с надписью от которого память вновь возвращается к тебе.")
    print("Написан там город в котором ты прожил всю свою сознательную жизнь - Большой Камень")
    print("Как тебя зовут?")
    print("\nВыберите вариант ответа(Цифрами пожалуйста):"
          "\n1.Ты кто?"
          "\n2.Где ты?"
          "\n3.Моё имя..")
    try:
        text = int(input())
    except Exception:
        print("Ну что тут непонятного, вводи только цифры :/")
    Player.name = input("Моё имя: ")
    print(f"Так, {Player.name}:, что ты делаешь в 18:00 в центре города?")
    Malibu()



if __name__ == '__main__':
    start()
