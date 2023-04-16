class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self._validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def _validate(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'Значение {self.param_name} должно быть строкой')
        if not value.istitle() or not value.isalpha():
            raise ValueError(
                f'Значение {self.param_name} должно быть строкой с первой буквой заглавной и содержать только буквы')