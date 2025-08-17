def summa(a, b) -> int:
    """
    Эта функция делает a + b
    """

    return a + b

#print("привет из модуля")


print(2, __name__)

if __name__ == "__main__":
    print("самостоятельный запуск")
else:
    print(__name__, "был импортирован")