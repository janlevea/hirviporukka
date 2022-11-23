# MODULE FOR PG CONNECTIONS AND OPERATIONS
# ========================================

# LIBRARIES AND MODULES
# ---------------------
import sys
import psycopg2  # For PostgreSQL
import datetime  # For handling date and time values
import decimal  # For handling decimal datatypes with extreme precision
import json  # For converting settings to JSON format

# CLASS DEFINITIONS
# -----------------
class DatabaseOperation():
    """Creates a connection to PostgreSQL database and
    executes various SQL commands"""

    # Constructor method: create a new object and set initial properties
    def __init__(self):
        self.errorCode = 0
        self.errorMessage = "OK"
        self.detailedMessage = "No errors"
        self.resultSet = []
        self.columnHeaders = []
        self.rows = 0
        self.columns = 0

    # - DatabaseOperation methods
    # -- Create connection arguments
    def createConnectionArgumentDict(self, database, role, pwd, host="localhost", port="5432"):
        """Creates a dictionary from connection arguments

        Args:
            database (str): Database name
            role (str): Role/Username
            pwd (str): DB-password
            host (str, optional): Server name or IP address. Defaults to "localhost".
            port (str, optional): Server's TCP port. Defaults to "5432".

        Returns:
            dict: Connection arguments as key-value pairs
        """
        connectionArgumentDict = {
            "server": host,
            "port": port,
            "database": database,
            "user": role,
            "password": pwd
        }
        return connectionArgumentDict

    # -- Save connection arguments to a settings file
    def saveDatabaseSettingsToFile(self, file, connectionArgs):
        """Saves connection arguments to JSON based settings file

        Args:
            file (str): Name of the JSON settings file
            connectionArgs (dict): Connection arguments in key-value pairs
        """
        settingsFile = open(file, 'w')
        json.dump(connectionArgs, settingsFile)
        settingsFile.close()

    # -- Read connection arguments from the settings file
    def readDatabaseSettingsFromFile(self, file):
        """Reads connection arguments frin JSON based settings file

        Args:
            file (str): Name of the settings file

        Returns:
            dict: Connection arguments in key-value pairs
        """
        settingsFile = open(file, 'r')
        connectionArgumentDict = json.load(settingsFile)
        settingsFile.close()
        return connectionArgumentDict

    # -- Get all rows from a given table
    def getAllRowsFromTable(self, connectionArgs, table):
        """Selects all rows from the table, view or SQL function's result set

        Args:
            connectionArgs (dict): Connection arguments in key-value pairs
            table (str): Name of the table, view or function to read from
        """
        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = "Yhdistettiin tietokantaan"
            self.detailedMessage = "Connected to database successfully"

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                sqlClause = 'SELECT * FROM ' + table + ';'
                cursor.execute(sqlClause)

                #Set object properties
                self.rows = cursor.rowcount
                self.resultSet = cursor.fetchall()
                self.columnHeaders = [cname[0] for cname in cursor.description]
                self.columns = len(self.columnHeaders)

                # Set error values
                self.errorCode = 0
                self.errorMessage = "Luettiin taulu onnistuneesti"
                self.detailedMessage = "Read all data from the table"

        except (Exception, psycopg2.Error) as error:
            # Set error values
            self.errorCode = 1
            self.errorMessage = "Tietokannan käsittely ei onnistunut"
            self.detailedMessage = str(error)
        finally:
            if self.errorCode == 0:
                dbconnection.close()

    # -- Insert a row to given table
    def insertRowToTable(self, connectionArgs, sqlClause):
        """Inserts a row to the table according to a SQL clause

        Args:
            connectionArgs (dict): Connection arguments in key-value pairs
            sqlClause (str): Insert clause
        """
        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = "Yhdistettiin tietokantaan"
            self.detailedMessage = "Connected to database successfully"

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                cursor.execute(sqlClause)

                # Set error values
                self.errorCode = 0
                self.errorMessage = "Lisättiin tietue onnistuneesti"
                self.detailedMessage = "Inserting to table was succesful"
                
                dbconnection.commit()

        except (Exception, psycopg2.Error) as error:
            # Set error values
            self.errorCode = 1
            self.errorMessage = "Tietokannan käsittely ei onnistunut"
            self.detailedMessage = str(error)
        finally:
            if self.errorCode == 0:
                dbconnection.close()

    # TODO: Finish writing methods for update and delete
    # -- Update a table
    def updateTable(self, connectionArgs, table, column, limit):
        """Updates a table

        Args:
            connectionArgs (dict): Connection arguments in key-value pairs
            table (str): Table name
            column (str): Column to be updated
            limit (str): WHERE SQL statement
        """
        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = 'Yhdistettiin tietokantaan'
            self.detailedMessage = 'Connected to database successfully'

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                sqlClause = f'UPDATE {table} SET {column} WHERE {limit}'
                cursor.execute(sqlClause)

                # Set error values
                self.errorCode = 0
                self.errorMessage = 'Päivitettiin tietue onnistuneesti'
                self.detailedMessage = 'Update was successful'
                dbconnection.commit()
                
        except (Exception, psycopg2.Error) as error:

            # Set error values 
            self.errorCode = 1 # TODO: Design a set of error codes to use with this module
            self.errorMessage = 'Tietokannan käsittely ei onnistunut'
            self.detailedMessage = str(error)
        finally:
            if self.errorCode == 0:
                dbconnection.close()

    # -- Delete a row from table
    def deleteFromTable(self, connectionArgs, table, limit):
        """Delete rows from a table using limiting SQL statement

        Args:
            connectionArgs (dict): Connection arguments in key-value pairs
            table (str): Table name
            limit (str): WHERE SQL statement
        """

        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = 'Yhdistettiin tietokantaan'
            self.detailedMessage = 'Connected to database successfully'

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                sqlClause = f'DELETE FROM {table} WHERE {limit}'
                cursor.execute(sqlClause)

                # Set error values
                self.errorCode = 0
                self.errorMessage = 'Poistettiin tietue onnistuneesti'
                self.detailedMessage = 'Deleting from table was successful'
                dbconnection.commit()
                
        except (Exception, psycopg2.Error) as error:

            # Set error values 
            self.errorCode = 1 # TODO: Design a set of error codes to use with this module
            self.errorMessage = 'Tietokannan käsittely ei onnistunut'
            self.detailedMessage = str(error)

        finally:
            if self.errorCode == 0:
                dbconnection.close()

    # Method to call a stored procedure and pass parameters
    def callProcedure(self, connectionArgs, procedure, params):
        """Calls a procedure and pass parameters

        Args:
            connectionArgs (dict): Connection arguments in key-value pairs
            procedure (str): Name of the procedure to call
            params (list): Procedures input parameters
        """
        server = connectionArgs['server']
        port = connectionArgs['port']
        database = connectionArgs['database']
        user = connectionArgs['user']
        password = connectionArgs['password']

        try:
            # Connect to the database and set error parameters
            dbconnection = psycopg2.connect(
                database=database, user=user, password=password, host=server, port=port)
            self.errorCode = 0
            self.errorMessage = "Yhdistettiin tietokantaan"
            self.detailedMessage = "Connected to database successfully"

            # Create a cursor to retrieve data from the table
            with dbconnection.cursor() as cursor:
                procedureCall = f"CALL {procedure} {params}"
                cursor.execute(procedureCall)

                # Set error values
                self.errorCode = 0
                self.errorMessage = "Suoritettiin proseduuri onnistuneesti"
                self.detailedMessage = "Procedure call was successful"
                
                dbconnection.commit()

        except (Exception, psycopg2.Error) as error:
            # Set error values
            self.errorCode = 1
            self.errorMessage = "Tietokannan käsittely ei onnistunut"
            self.detailedMessage = str(error)
        finally:
            if self.errorCode == 0:
                dbconnection.close()

# LOCAL TESTS, REMOVE WHEN FINISHED DESIGNING THE MODULE
if __name__ == "__main__":
    # Lets create a DatabaseOperation object
    testOperation = DatabaseOperation()
    # Create a dictionary for connection settings using defaults
    dictionary = testOperation.createConnectionArgumentDict(
        'metsastys', 'sovellus', 'Q2werty')
    # print(dictionary)
    # Save those settings to file
    testOperation.saveDatabaseSettingsToFile('settings.dat', dictionary)
    # Read settings back from the file
    settingsRead = testOperation.readDatabaseSettingsFromFile('settings.dat')
    
    # Get all rows from test table
    testOperation.getAllRowsFromTable(settingsRead, "public.pgmodule_test")

    print(testOperation.resultSet)

    # # Test insert operation with a sql clause
    # sqlClause = "INSERT INTO public.pgmodule_test(etunimi, sukunimi, ika) VALUES ('Jonne', 'Janttari', 17);"
    # print (sqlClause)
    # testOperation.insertRowToTable(settingsRead, sqlClause)
    # print(testOperation.errorMessage, "--------------\n", testOperation.detailedMessage)

    # Test delete operation
    # limit = 'id = 2'
    # testOperation.deleteFromTable(settingsRead, 'public.pgmodule_test', limit)

    # Test update operation
    # testOperation.updateTable(settingsRead, 'public.pgmodule.test', )

# -------------copypasted
"""
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
    
    # Execute a SQL command to get hunters (jasen)
    command = "SELECT * FROM public.jasen;"
    cursor.execute(command)
    result_set = cursor.fetchall()
    print("Jäsentiedot ovat:", result_set)

# Throw an error if connection or cursor creation fails                                     
except(Exception, psycopg2.Error) as e:
    print("Tietokantayhteydessä tapahtui virhe", e)

# If or if not successfull close the cursor and the connection   
finally:
    if (dbaseconnection):
        cursor.close()
        dbaseconnection.close()
        print("Yhteys tietokantaan katkaistiin")
"""