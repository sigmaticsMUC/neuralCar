from abc import abstractmethod, ABCMeta


class abstractVehicle():

    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_next_pos(self):
        pass

    @abstractmethod
    def update_direction(self):
        pass

    @abstractmethod
    def to_string(self):
        pass

