'''Задача 3.
1) Написать программу, в которой есть главный класс Games со статическим полем Year.
2) Опишите конструктор присваивающий значение полю Year.
3) Также опишите метод getName, который возвращает имя игры.
4) На основе главного класса путем наследования опишите четыре класса PCGames,
PS4Games, XboxGames, MobileGames.
5) Добавьте каждому классу дополнительные поля и переопределите у всех классов
метод getName.
'''
#include modul
from abc import ABC, abstractmethod
from typing import Union

#main class initialization
class Games(ABC):

    _Year = None

    #initialization method yearGame
    @abstractmethod
    def yearGame(self, value: int) -> None:
        ...

    #initialization method getName
    @abstractmethod
    def getName(self) -> str:
        ...

#PCGames class initialization
class PCGames(Games):
    
    def __init__(self, name: str, genre: str, price: Union[str, list]):    
        self._name = name
        self._genre = genre
        self._price = price

    #initialization method yearGame
    def yearGame(self, value: int) -> None:
        self._Year = value   

    #initialization method getName
    def getName(self) -> str:
        return self._name

#PS4Games class initialization
class PS4Games(Games):
    
    def __init__(self, name: str, genre: str, price: Union[str, list]):    
        self._name = name
        self._genre = genre
        self._price = price

    #initialization method yearGame
    def yearGame(self, value: int) -> None:
        self._Year = value   

    #initialization method getName
    def getName(self) -> str:
        return self._name       

#XboxGames class initialization
class XboxGames(Games):
    
    def __init__(self, name: str, genre: str, price: Union[str, list]):    
        self._name = name
        self._genre = genre
        self._price = price

    #initialization method yearGame
    def yearGame(self, value: int) -> None:
        self._Year = value   

    #initialization method getName
    def getName(self) -> str:
        return self._name   

#MobileGames class initialization
class MobileGames(Games):
    
    def __init__(self, name: str, genre: str, price: Union[str, list]):    
        self._name = name
        self._genre = genre
        self._price = price

    #initialization method yearGame
    def yearGame(self, value: int) -> None:
        self._Year = value   

    #initialization method getName
    def getName(self) -> str:
        return self._name  


obj = PCGames('GTA', 'RPG', 2000)
print(f'Игра: {obj.getName()}')   
