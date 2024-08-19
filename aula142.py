# Classes abstradas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concetros. Também podem ter métodos concretos por elas mesmas.
# @abstractmethods são métodos que não tem corpo.
# As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.
# Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.
# É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorador mais interno
from abc import ABC, ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta):
#     ...

class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin('Oi')
l.log_error()