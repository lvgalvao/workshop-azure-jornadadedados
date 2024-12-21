import azure.functions as func
import logging
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="lab1func")
def lab1func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name == "magic":

        # Get the Key Vault URL from the environment

        try:
            key_vault_url = "https://azurekeyvaultworkshop.vault.azure.net/"
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=key_vault_url, credential=credential)
            sqlusername = client.get_secret("sqlusername")
            sqlpassword = client.get_secret("sqlpassword")

        except:
            return func.HttpResponse("Error: Unable to get secrets from Key Vault", status_code=500)
        
        server = "workshopazuredatavase.database.windows.net"
        database = "bitcoin_database"
        driver = "{ODBC Driver 17 for SQL Server}"

        try:
            cnxn = pyodbc.connect(f"DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={sqlusername.value};PWD={sqlpassword.value}")

        except pyodbc.Error as ex:
            return func.HttpResponse(f"Error: {str(ex)}", status_code=500)

        allrecords = "select * from vendas"
        car_models = []

        try:
            with cnxn.cursor() as cursor:
                cursor.execute(allrecords)
                rows = cursor.fetchall()

                for row in rows:
                    logging.info(row)
                    car_models.append(row[1])
            
            return func.HttpResponse(f"Car models: {car_models}", status_code=200)
        
        except pyodbc.Error as ex:
            logging.info("Error")
            return func.HttpResponse(f"Error: {str(ex)}", status_code=500)
        
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=200
        )