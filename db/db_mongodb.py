
from constants.urls import URL
from db.databases import databasesfactory


class MongoNDB(databasesfactory):
    """
        MongoDB class will do following


    """
    def __init__(self,db_host:str,db_port:str):
        self.__host = db_host
        self.__port = db_port
        self._create_connection_string = self.create_connection_string()


    def create_connection_string(self) -> str:
        return "mongodb://" + self.__host + ":" + str(self.__port) + "/"

    @property
    def conn_string(self):
        return self._create_connection_string




