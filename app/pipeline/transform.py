import duckdb


def conexão_duckdb() -> duckdb.DuckDBPyConnection:
    """
        Função que retorna a conexão do duckdb.

        return:
        - retorna a conexão com o motherduck.
    """
    import os

    motherduck_token = os.getenv('motherduck_token')

    # initiate the MotherDuck connection through a service token through
    con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

    return con

def select(query:str):
    """
        Função que recebe uma $query e executa a consulta no banco de dados.

        args:
        - query (str): consulta em sql.

        return:
        - resultado da $query pelo banco de dados.
    """
    con = conexão_duckdb()

    # run a query to check verify that you are connected
    return con.sql(query).show()