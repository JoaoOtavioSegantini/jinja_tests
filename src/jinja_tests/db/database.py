import pyodbc
from dotenv import load_dotenv, get_key


class Database:
    """retorna uma instância do banco de dados"""
    
    load_dotenv()
    
    def __init__(self) -> None:
        self.__server = 'sqlserver'
        self.__database = 'FakeStore'
        self.__username = 'sa'
        self.__password = get_key(key_to_get='SQL_SERVER_PASS', dotenv_path='.env')
        

    def connect(self) -> pyodbc.Connection:
        """abre a conexao com o banco de dados"""

        conexao = f"""
            Driver={{ODBC Driver 18 for SQL Server}};
            Server={self.__server};
            Database={self.__database};
            UID={self.__username};
            PWD={self.__password};
            TrustServerCertificate=yes;
        """

        return pyodbc.connect(conexao)
    
    def fechar_conexao(self, cursor: pyodbc.Cursor, conexao: pyodbc.Connection) -> None:
        """fecha a conexao com o banco de dados"""

        cursor.close()
        conexao.close()
