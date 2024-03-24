import duckdb
import os

motherduck_token = os.getenv('motherduck_token')

# initiate the MotherDuck connection through a service token through
con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

# run a query to check verify that you are connected
con.sql("SHOW DATABASES").show()