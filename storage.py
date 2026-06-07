from abc import ABC, abstractmethod


class BaseTable(ABC):

    @abstractmethod
    def add(self, record): 
        pass

    @abstractmethod
    def get_all(self): 
        pass

    @abstractmethod
    def filter(self, **filters): 
        pass

    @abstractmethod
    def update(self, record_id, name, age): 
        pass

    @abstractmethod
    def delete(self, record_id): 
        pass

    @abstractmethod
    def sort_by(self, field, reverse=False): 
        pass
