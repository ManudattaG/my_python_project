from abc import ABCMeta, abstractmethod


class AbstractClientsDAO(metaclass=ABCMeta):
    """
    Defines the interface for the Client data access objects
    """

    @abstractmethod
    def find_client_by_last_name(self, client_id):
        raise NotImplementedError

    @abstractmethod
    def find_client_by_postal_code(self, postal_code):
        raise NotImplementedError

    @abstractmethod
    def find_client_by_city(self, city):
        raise NotImplementedError

    @abstractmethod
    def find_client_by_country(self, country):
        raise NotImplementedError

    @abstractmethod
    def find_client_by_cityandcountry(self, city, country):
        raise NotImplementedError

    @abstractmethod
    def get_all_clients(self):
        raise NotImplementedError