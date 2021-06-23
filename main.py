print("Мифы Скандинавии")
print("\t\t\t\t\t\t\t\t Правила"
      "\n1. Отгадывание слов производится побуквенно!!! То есть после вопроса "
      "Вам необходимо ввести 1 букву и получить ответ о её наличии в слове."
      "\n2. У Вас есть 5 попыток угадать букву, иначе проиграете."
      "\n3. При переходе к новому слову у Вас снова будет 5 попыток.\n\n")
print("Внезапно Вы очнулись в комнате. Она была пустой и никого кроме Вас в ней"
      " не было.\nОсматривая комнату, Вы обнаружили две двери. Введите направо, если"
      " хотите открыть правую дверь, \nналево - левую дверь")
flag = 1
while flag == 1:
    napravlenie = input()
    if napravlenie == "направо":
        print("Открыв правую дверь, Вы очутились в коридоре, в конце которого была"
              " таблица. \n На ней было написанно: Назови имя волка, сына Локи, чтобы путь "
              "тебе открылся.")
        mistake = 0
        otvet = "фенрир"
        otvet1 = ""
        array = []
        for i in range(0, len(otvet)):
            array.append("-")
        while mistake < 5 and otvet1.join(array) != otvet:
            flag1 = 0
            bykva = input()
            for i in range(0, len(otvet)):
                if otvet[i] == bykva:
                    array[i] = bykva
                    flag1 = 1
            print(otvet1.join(array))
            if flag1 == 0:
                mistake += 1
                print("Такой буквы в слове нет")
        if mistake == 5:
            print("Вы проиграли...")
            flag = 0
        else:
            print("Вы смогли решить первую задачу. Поздравляю!!!")
            print("Правильно решённая задача позволила Вам попасть в новую комнату."
                  "\n В этой комнате вы увидели свою возлюбленную, которая висела в клетке над"
                  " углублением в котором виднелась лава. \n Так же была табличка на которой "
                  "написано: Назови дочь Локи, ту что правит подземным миром")
            mistake = 0
            otvet = "хель"
            otvet1 = ""
            array = []
            for i in range(0, len(otvet)):
                array.append("-")
            while mistake < 5 and otvet1.join(array) != otvet:
                flag1 = 0
                bykva = input()
                for i in range(0, len(otvet)):
                    if otvet[i] == bykva:
                        array[i] = bykva
                        flag1 = 1
                print(otvet1.join(array))
                if flag1 == 0:
                    mistake += 1
                    print("Такой буквы в слове нет")
            if mistake == 5:
                print("Вы проиграли и Ваша возлюбленная упала. В порыве чувств Вы кинулись за"
                      " ней и тоже погибли...")
                flag = 0
            else:
                print("Вам удалось спасити свою возлюбленную. На Вашем пути осталось последнее "
                      "испытание. \n На двери, что вела к выходу, красовалась таблица с таким "
                      "соержанием:\n Лишь верховный бог в праве выпустить Вас. Назовите имя его и "
                      "будет Вам воля.")
                mistake = 0
                otvet = "один"
                otvet1 = ""
                array = []
                for i in range(0, len(otvet)):
                    array.append("-")
                while mistake < 5 and otvet1.join(array) != otvet:
                    flag1 = 0
                    bykva = input()
                    for i in range(0, len(otvet)):
                        if otvet[i] == bykva:
                            array[i] = bykva
                            flag1 = 1
                    print(otvet1.join(array))
                    if flag1 == 0:
                        mistake += 1
                        print("Такой буквы в слове нет")
                if mistake == 5:
                    print("Вы проиграли. Теперь вы навечно останетесь в этом не понятном и "
                          "ужасном месте")
                    flag = 0
                else:
                    print("Поздравляю Вас!!! Вы смогли выбраться из этого непонятного места и "
                          "спасти свою возлюбленную.")
                    flag = 0
    elif napravlenie == "налево":
        print("Открыв левую дверь, Вы очутились в тёмном коридоре. Сделав пару шагов, "
              "Вы провалились в дыру. \nПридя в себя после падения, Вы увидели перед собой "
              "табличку.\n На ней было написанно: Назови имя бога-громовержца, одного из "
              "сыновей Одина, чтобы путь тебе открылся.")
        mistake = 0
        otvet = "тор"
        otvet1 = ""
        array = []
        for i in range(0, len(otvet)):
            array.append("-")
        flag2 = 0
        while mistake < 5 and otvet != otvet1.join(array):
            flag1 = 0
            bykva = input()
            for i in range(0, len(otvet)):
                if otvet[i] == bykva:
                    array[i] = bykva
                    flag1 = 1
            print(otvet1.join(array))
            if flag1 == 0:
                mistake += 1
                print("Такой буквы в слове нет")
        if mistake == 5:
            print("Вы проиграли...")
            flag = 0
        else:
            print("Вы смогли решить первую задачу. Поздравляю!!!")
            print("В стене открылся проход и Вы пошли в него и попали в комнату."
                  "\n В этой комнате было много золота и различных изделий из него. Вы подумали "
                  "что попали в сказку. \n Но как только Вы подняли кубок, потолок начал "
                  "медленно опускаться. Вы оказались в ловушке. \n В панике Вы начали "
                  "осматривать комнату и увидели табличку, на которой написано:"
                  "Как называется конец света в Скандинафских мифах?")
            mistake = 0
            otvet = "рагнарёк"
            otvet1 = ""
            array = []
            for i in range(0, len(otvet)):
                array.append("-")
            while mistake < 5 and otvet1.join(array) != otvet:
                flag1 = 0
                bykva = input()
                for i in range(0, len(otvet)):
                    if otvet[i] == bykva:
                        array[i] = bykva
                        flag1 = 1
                print(otvet1.join(array))
                if flag1 == 0:
                    mistake += 1
                    print("Такой буквы в слове нет")
            if mistake == 5:
                print("Вы проиграли и были раздавлены...")
                flag = 0
            else:
                print("Угадав слово, Вы увидели открывшийся в полу тайный ход. \n"
                      "Забравшись в него и дойдя до конца, Вы очутились перед дверью, котороя вела "
                      "на волю.\n А рядом с дверью таблица со следующим содержанием: Как называется "
                      "древо, что соединяет все девять миров?")
                mistake = 0
                otvet = "иггдрасиль"
                otvet1 = ""
                array = []
                for i in range(0, len(otvet)):
                    array.append("-")
                while mistake < 5 and otvet1.join(array) != otvet:
                    flag1 = 0
                    bykva = input()
                    for i in range(0, len(otvet)):
                        if otvet[i] == bykva:
                            array[i] = bykva
                            flag1 = 1
                    print(otvet1.join(array))
                    if flag1 == 0:
                        mistake += 1
                        print("Такой буквы в слове нет")
                if mistake == 5:
                    print("Вы проиграли. Теперь вы навечно останетесь в этом не понятном "
                          "и ужасном месте")
                    flag = 0
                else:
                    print("Поздравляю Вас!!! Вы смогли выбраться из этого непонятного места.")
                    flag = 0
    else:
        print("Вы не правильно выбрали направление")
