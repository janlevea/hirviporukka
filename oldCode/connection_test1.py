# TEST THE CONNECTION TO POSTGRESQL SERVER ON LOCALHOST

# LIBRARIES AND MODULES
import psycopg2  # For PostgreSQL

# Properties of the connection string
database = "metsastys"
user = "postgres"
password = "Q2werty"
host = "localhost"
port = "5432"

# Try to establish a connection to DB server
try:
    # Create a connection object
    dbaseconnection = psycopg2.connect(database=database, user=user, password=password,
                                      host=host, port=port)
    
    # Create a cursor to execute commands and retrieve result set
    cursor = dbaseconnection.cursor()
    cursor.execute("SELECT version();") # Executes version function on PG server and store result on cursor
    version_number = cursor.fetchone() # Read result from cursor (1 row)
    print("PostgreSQL:n versionumero on ", version_number) 

# Throw an error if connection or cursor creation fails                                     
except(Exception, psycopg2.Error) as error:
    print("Tietokantayhteydessä tapahtui virhe", error)

# If or if not successfull close the cursor and the connection   
finally:
    if dbaseconnection:
        cursor.close()
        dbaseconnection.close()
        print("Yhteys tietokantaan katkaistiin")
