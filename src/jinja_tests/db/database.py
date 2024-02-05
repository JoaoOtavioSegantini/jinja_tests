import pyodbc
from dotenv import load_dotenv, get_key


class Database:

    def connect() -> pyodbc.Connection:

        load_dotenv()

        server = 'sqlserver;'
        database = 'FakeStore'
        username = 'sa'
        password = get_key(key_to_get='SQL_SERVER_PASS', dotenv_path='.env')

        conexao = f"""
        Driver={{ODBC Driver 18 for SQL Server}};
        Server={server};
        Database={database};
        UID={username};
        PWD={password};
        TrustServerCertificate=yes;
      """

        return pyodbc.connect(conexao)
