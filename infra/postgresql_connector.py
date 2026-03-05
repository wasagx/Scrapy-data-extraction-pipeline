import psycopg2

def get_postgres_connection():
    return psycopg2.connect(
        dbname="jobs_db",
        user="postgres",
        password="password",
        host="postgres"
    )
