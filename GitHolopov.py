import random as r
import datetime as dt
import requests


answers = [ 'Всё отлично', 'Неплохо!', 'Балдёж всё', 'Хорошо', 'Круто', 'По-тихоньку, по-маленьку']
gamersp = ['Камень', 'Ножницы', 'Бумага']
randik = ['Да', 'Нет']
database = {
    'Данил':'Мурмино',
    'Артём' : 'Рязань',
    'Арина' : 'Санкт-Петербург',
    'Соня' : 'Рязань',
    'Кирилл' : 'Москва',
    'Кристина' : 'Сасово',
    'Гена' : 'Екатеринбург'
}
ListOfCities = {
    'Мурмино ' : 3,
    'Рязань' : 3,
    'Санкт-Петербург' : 3,
    'Москва' : 3,
    'Сасово' : 3,
    'Екатеринбург' : 5
}
def game():

    print('Давайте начнём игру!')
    while True:
        ans = str(input('Что выберете? Камень/Ножницы/Бумага \n'))
        anf = r.choice(gamersp)
        print(f'Я выбрала {anf}')


        if ans == 'Камень' and anf == 'Камень':
            print('Ничья!')
        elif ans == 'Камень' and anf == 'Ножницы':
            print('Вы выиграли!')
        elif ans == 'Камень' and anf == 'Бумага':
            print('Я победила!')
        elif ans == 'Бумага' and anf == 'Камень':
            print('Вы выиграли!')
        elif ans == 'Бумага' and anf == 'Ножницы':
            print('Я победила!')
        elif ans == 'Бумага' and anf == 'Бумага':
            print('Ничья!')
        elif ans == 'Ножницы' and anf == 'Бумага':
            print('Вы выиграли!')
        elif ans == 'Ножницы' and anf == 'Камень':
            print('Я выиграла!')
        elif ans == 'Ножницы' and anf == 'Ножницы':
            print('Ничья!')
        elif ans == '':
            print('Вы ничего не написали.')
        print('Сыграем ещё раз? Да/Нет \n')
        a = str(input())
        if a == 'Да':
            continue
        else:
            break



def time():
    CurrentDt = dt.datetime.now()
    TimeOnly = CurrentDt.time()
    StrTime = str(TimeOnly)
    CurrentTime = StrTime.split(':')
    ValueTime = int(CurrentTime[0])
    return Hello(ValueTime)
    
def Calc(query):
    math = input('Введите выражение формата ''a + b'': ')
    math = math.split(' ')
    a = float(math[0])
    b = float(math[2])
    if math[1] == '+':
        s = a+b
        return f'Результат: {s}'
    elif math[1] == "-":
        d = a-b
        return f'Результат: {d}'
    elif math[1] == '*':
        p = a*b
        return f'Результат: {p}'
    elif math[1]== '/':
        div = a / b
        return f'Результат: {div}'


def Hello(time):
    text = 'меня зовут Анфиса, и я Ваш голосовой помощник'
    if time > 0 and time < 6:
        return(f'Доброй ночи, {text} ')
    elif time > 6 and time <= 11:
        return f'Доброе утро, {text}'
    elif time > 11 and time < 17:
        return f'Добрый день, {text}'
    elif time >= 17 and time < 23:
        return f'Добрый вечер, {text}'
    else:
        return f'Доброй ночи, {text}'


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 1,
        'M': ''
    }
    headers_parameters = {
        'Accept-Language' : 'ru'
    }
    try:
        response = requests.get(url, params=weather_parameters, headers = headers_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return f'В городе Рязань сейчас - {response.text}' 
    else:
        return '<ошибка на сервере погоды>'
    

def queryToAnfisa(query):
    
    if query == 'Сколько времени?' or query == 'Который час?':
        timeNow = dt.datetime.now()
        timeText = timeNow.strftime('%H:%M')
        return f'Сейчас {timeText}'
    elif query == 'Где мои друзья?':
        text = ', '.join(set(database.values()))
        return f'Твои друзья в городах - {text}'
    elif query == 'Сгенерируй случайное число':
        print('Выберите диапазон')
        a = int(input('Первое число: '))
        b = int(input('Второе число: '))
        print('Генерирую...Секундочку...')
        rand = r.randint(a,b)
        return f'Готово - {rand}'
    elif query == 'Как погода?':
        return what_weather('Рязань')
    elif query == 'Калькулятор':
        return Calc(query)  
    elif query == 'Делать или нет?':
        answer = r.choice(randik)
        return answer
    elif query == 'Как дела?':
        return r.choice(answers)
    elif query == 'Играть':
        return game()
        
    else:
        querySplit = query.strip('?')
        querySplit = querySplit.split(' ')
        if querySplit[0] == 'Где':
            name = querySplit[1]
            if name in database:
                city = database[name]
                return f'{name} в городе {city}'
            else:
                return f'У Вас нет друга с именем {name}'
        else:
            return '<неккоректный запрос>'
    

            

def Start():
    print(time())
    print('На что я могу ответить - Сколько времени?/Который час?; Где мои друзья?; Где [Имя друга]?; Сгенерируй случайное число;')
    print('Как погода?; Калькулятор; Как дела?; Играть')
    print('Чего хотите узнать?')
    query = str(input())
    print(queryToAnfisa(query))

Start()


