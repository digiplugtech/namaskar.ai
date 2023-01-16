import abc

class databasesfactory(abc.ABC):
    def create_connection_string(self) -> str:
        pass
