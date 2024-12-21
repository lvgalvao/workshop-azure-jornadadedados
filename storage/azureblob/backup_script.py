import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de configuração
CONNECTION_STRING = os.getenv("AZURE_STORAGE_URL")
if not CONNECTION_STRING:
    raise ValueError("A connection string está vazia. Verifique o arquivo .env.")


CONTAINER_NAME = "backup"  # Nome do container no Azure
LOCAL_FOLDER = "./local_files"  # Caminho da pasta local para backup

def upload_files_to_blob():
    try:
        # Conectar ao Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Verificar se o container existe; se não, criar
        if not container_client.exists():
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' criado.")

        # Iterar pelos arquivos na pasta local
        for root, _, files in os.walk(LOCAL_FOLDER):
            for file_name in files:
                local_file_path = os.path.join(root, file_name)

                # Nome do arquivo no Blob
                blob_name = os.path.relpath(local_file_path, LOCAL_FOLDER)

                # Upload do arquivo para o Blob
                with open(local_file_path, "rb") as data:
                    blob_client = container_client.get_blob_client(blob_name)
                    blob_client.upload_blob(data, overwrite=True)
                    print(f"Arquivo '{file_name}' enviado como '{blob_name}'.")

    except Exception as ex:
        print(f"Erro: {ex}")

if __name__ == "__main__":
    upload_files_to_blob()
