from fastapi import FastAPI, Query, HTTPException, Header
from typing import Optional, List
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

elements =  []

class Element(BaseModel):
    element: str

class Expression(BaseModel):
    expr: str


@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/sum1n/{n}")
async def sum1n(n: int):
    result = sum(range(1, n + 1))
    return {"result": result}


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:  # Первое число последовательности (0)
        return 0
    if n == 1:  # Второе число последовательности (1)
        return 1
    
    a, b = 0, 1  # начинаем с 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@app.get("/fibo")
async def get_fibonacci(n: Optional[int] = None):
    if n is None:
        raise HTTPException(status_code=400, detail="Parameter 'n' is required")
    try:
        result = fibonacci(n)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.post("/reverse")
async def reverse_string(string: str = Header(...)):
    return JSONResponse (content={"result": string[::-1]})



@app.put("/list")
async def add_element(item: Element):
    elements.append(item.element)
    return JSONResponse(content={"message":"Element added"})

@app.get ("/list")
async def get_elements():
    return JSONResponse(content={"result": elements})



@app.post("/calculator")
async def calculate_expression(expression: Expression):
    try:
        # Разделяем строку по запятым
        num1_str, operator, num2_str = expression.expr.split(',')

        # Преобразуем числа из строки
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Выполняем операцию в зависимости от оператора
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                # Ошибка при делении на ноль
                raise HTTPException(status_code=403, detail={"error": "zerodiv"})
            result = num1 / num2
        else:
            # Неподдерживаемый оператор
            raise HTTPException(status_code=400, detail={"error": "invalid"})

        # Возвращаем результат
        return JSONResponse(content={"result": result})

    except ValueError:
        # Ошибка при конвертации или неправильном формате строки
        raise HTTPException(status_code=400, detail={"error": "invalid"})
    except Exception:
        # Обработка других ошибок
        raise HTTPException(status_code=400, detail={"error": "invalid"})