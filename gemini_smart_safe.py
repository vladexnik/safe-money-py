class Safe:
    # Класс - сейф с деньгами 
    def __init__(self, pin_code, initial_money):
        
        if not Safe.validate_pin(pin_code):
            raise ValueError("Пин-код должен состоять ровно из 4 символов!") # проверка, после raise код не выполняется
        
        self.__pin_code = pin_code     # приватный уровень доступа, переменная видна только внутри класса
        self.__initial_money = initial_money


    def __verify_pin(self, pin):
        if pin != self.__pin_code:
            return 'Пинкод введен неверно!'
        return None
    
    def get_balance(self, pin):        # выводит количество денег на балансе, если пинкод верный
        error = self.__verify_pin(pin)
        if error:
            return error
        return self.__initial_money
        
    def deposit(self, pin, amount):    # пополняет баланс, если пинкод верный
        error = self.__verify_pin(pin)
        if error:
            return error
        self.__initial_money += self.amount
    
    def withdraw(self, pin, amount): # снимает деньги, если пинкод верный
        error = self.__verify_pin(pin)
        if error:
            return error
        self.__initial_money -= self.amount   
     
    @classmethod 
    def create_default_safe(cls): # класс принимает себя как аргумент и создает объект своего класса
        return cls("0000", 1000) # писать обязательно "0000" иначе выдаст ошибку
    
    @staticmethod
    def validate_pin(pin):
        return isinstance(pin, str) and len(pin) == 4 and pin.isdigit()
    
    def add_note(self, pin, note_name, note_text):
        error = self.__verify_pin(pin)
        if error:
            return error
        
        if note_name.startswith('_'):
            return "Ошибка: имя заметки не может начинаться с подчеркивания!"
        
        setattr(self, note_name, note_text)
        return f"Заметка '{note_name}' успешно сохранена!"

    def get_note(self, pin, note_name):
        error = self.__verify_pin(pin)
        if error:
            return error
        return getattr(self, note_name, 'Заметка не найдена!')
    def __str__(self): # магический метод, возвращает данные про объект
        return f"Сейф защищен пин-кодом, баланс: {self.__initial_money} руб."

    def get_history(self, pin):
        error = self.__verify_pin(pin)
        if error:
            return error
        return self.__history
    

my_safe = Safe('1234', 5000)
print(my_safe.add_note('1234', 'чюпеп', 'я скебоб'))
print(my_safe.get_note('1234', 'чюпеп'))

