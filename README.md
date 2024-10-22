# FastAPI Project

## Описание проекта

Это простой API, разработанный с использованием FastAPI, который включает следующие функции:

- Получение суммы чисел от 1 до N.
- Получение N-го числа в последовательности Фибоначчи.
- Реверсирование строки.
- Добавление элементов в список и получение списка.
- Выполнение простых математических операций.
  
## Установка и запуск проекта

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на вашу локальную машину:

```bash
git clone github.com/Nurlan-JS/TechOrda/tree/api
cd api
```

### 2. Установка виртуального окружения

``` bash
python3 -m venv venv
source venv/bin/activate  # Для Linux/macOS
# или
venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей

``` bash
pip install -r requirements.txt
```

### 4. Запуск приложения

``` bash
uvicorn main:app --reload
```

## Приложение будет доступно по адресу http://127.0.0.1:8000

### 5. Примеры использования API

1. Получение приветственного сообщения
GET запрос к корню:

``` bash
Copy code
curl http://127.0.0.1:8000/
Ответ:
```
```
json
Copy code
{
  "Hello": "World"
}
```
2. Сумма чисел от 1 до N
GET запрос:

``` bash
Copy code
curl http://127.0.0.1:8000/sum1n/10
```
Ответ:
```
json
Copy code
{
  "result": 55
}
```

3. N-е число Фибоначчи
GET запрос:

``` bash
Copy code
curl http://127.0.0.1:8000/fibo?n=10
```
Ответ:

``` json
Copy code
{
  "result": 55
}
```
4. Реверс строки
POST запрос с заголовком:

``` bash
Copy code
curl -X POST -H "string: hello" http://127.0.0.1:8000/reverse
```
Ответ:

``` json
Copy code
{
  "result": "olleh"
}
```
5. Добавление элемента в список
PUT запрос с телом запроса:

``` bash
Copy code
curl -X PUT -d '{"element":"Apple"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/list
```
Ответ:

``` json
Copy code
{
  "message": "Element added"
}
```
6. Получение списка элементов
GET запрос:

``` bash
Copy code
curl http://127.0.0.1:8000/list
```
Ответ:

``` json
Copy code
{
  "result": ["Apple"]
}
```

7. Калькулятор
POST запрос с математическим выражением:

``` bash
Copy code
curl -X POST -d '{"expr":"10,+,5"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/calculator
```
Ответ:

``` json
Copy code
{
  "result": 15
}
```
### Postman запросы:

- GET / - Проверка статуса и приветственного сообщения
- GET /sum1n/{n} - Сумма от 1 до N
- GET /fibo - Получение N-го числа Фибоначчи
- POST /reverse - Реверс строки
- PUT /list - Добавление элемента в список
- GET /list - Получение списка элементов
- POST /calculator - Калькулятор выражений
