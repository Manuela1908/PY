import googleapiclient.discovery
import google.oauth2.service_account
import pymysql


credenciais_json = r'C:\Users\RDSINFO\Documents\script\python\credenciais.json'


escopos = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.send'] #adicione quantos escopos forem necessários


credentials = google.oauth2.service_account.Credentials.from_service_account_file(credenciais_json, scopes=escopos)

delegated_credentials = credentials.with_subject('nome@dominio.com') #conta Google


calendar_service = googleapiclient.discovery.build('calendar', 'v3', credentials = delegated_credentials)

events = calendar_service.events().list(calendarId='primary', maxResults=10).execute()

access_token = delegated_credentials.token

print(f"\n{access_token}")


config = {
    'host': '', 
    'user': '',        
    'password': '', 
    'db': '',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


conn = pymysql.connect(**config)
cursor = conn.cursor()
token = access_token

insert_query = "UPDATE Tabela_Tokens SET token = %s WHERE nome = 'nome token'"
value = token

try:
    
    cursor.execute(insert_query, (value))
    conn.commit()
    print("\nAtualização bem-sucedida!")

except pymysql.Error as err:

    conn.rollback()
    print(f"\nErro ao inserir dados: {err}")

finally:

    cursor.close()
    conn.close()

