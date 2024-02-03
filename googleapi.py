import googleapiclient.discovery
import google.oauth2.service_account
import pymysql
import os
import dotenv

dotenv.load_dotenv()

credenciais_json = os.getenv("JSON")


escopos = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/gmail.send'] #Adiciones escopos conforme necessário


credentials = google.oauth2.service_account.Credentials.from_service_account_file(credenciais_json, scopes=escopos)

delegated_credentials = credentials.with_subject(os.getenv("GMAIL_USER"))


calendar_service = googleapiclient.discovery.build('calendar', 'v3', credentials = delegated_credentials)

events = calendar_service.events().list(calendarId='primary', maxResults=10).execute()

access_token = delegated_credentials.token

print(f"\n{access_token}")


config = {
    'host': os.getenv("DB_HOST"), 
    'user': os.getenv("DB_USER"),        
    'password': os.getenv("DB_PASSWORD"), 
    'db': os.getenv("DATABASE"),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


conn = pymysql.connect(**config)
cursor = conn.cursor()
token = access_token

insert_query = "UPDATE Tokens SET token = %s WHERE nome = 'API Google Calendar'"
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

