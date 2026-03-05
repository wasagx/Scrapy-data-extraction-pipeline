import pandas as pd
from infra.postgresql_connector import get_postgres_connection
from infra.mongodb_connector import get_mongo_connection

class DatabaseQuery:
    def __init__(self):
        # Initialize PostgreSQL and MongoDB connections
        self.pg_conn = get_postgres_connection()
        self.mongo_client = get_mongo_connection()
        self.mongo_db = self.mongo_client['jobs_db']  
        self.mongo_collection = self.mongo_db['raw_collection']

    def fetch_postgres_data(self):
        # Fetch data from PostgreSQL
        query = "SELECT * FROM raw_table"  
        pg_data = pd.read_sql(query, self.pg_conn)
        return pg_data

    def fetch_mongo_data(self):
        # Fetch data from MongoDB
        mongo_data = list(self.mongo_collection.find())
        mongo_df = pd.DataFrame(mongo_data)
        return mongo_df

    def export_postgres_to_csv(self, pg_data, output_file="postgres_data.csv"):
        # Export PostgreSQL data to CSV
        pg_data.to_csv(output_file, index=False)
        print(f"PostgreSQL data successfully exported to {output_file}")

    def export_mongo_to_csv(self, mongo_data, output_file="mongo_data.csv"):
        # Export MongoDB data to CSV
        mongo_data.to_csv(output_file, index=False)
        print(f"MongoDB data successfully exported to {output_file}")

    def close_connections(self):
        # Close database connections
        self.pg_conn.close()
        self.mongo_client.close()

if __name__ == "__main__":
    db_query = DatabaseQuery()
    
    pg_data = db_query.fetch_postgres_data()
    mongo_data = db_query.fetch_mongo_data()
    
    db_query.export_postgres_to_csv(pg_data, output_file="postgres_data.csv")
    db_query.export_mongo_to_csv(mongo_data, output_file="mongo_data.csv")
    
    db_query.close_connections()
