import json
from datetime import datetime
from infra.postgresql_connector import get_postgres_connection
from infra.redis_connector import get_redis_connection
from infra.mongodb_connector import get_mongo_connection



# Normalize function to set default values for missing fields
def normalize_item(item):
    fields_defaults = {
        'slug': None,
        'language': None,
        'languages': [],
        'req_id': None,
        'title': None,
        'description': None,
        'street_address': None,
        'city': None,
        'state': None,
        'country_code': None,
        'postal_code': None,
        'location_type': None,
        'latitude': 0.0,
        'longitude': 0.0,
        'categories': [],
        'tags': [],
        'tags5': [],
        'tags6': [],
        'brand': None,
        'promotion_value': 0.0,
        'salary_currency': None,
        'salary_value': 0.0,
        'salary_min_value': 0.0,
        'salary_max_value': 0.0,
        'benefits': [],
        'employment_type': None,
        'hiring_organization': None,
        'source': None,
        'apply_url': None,
        'internal': False,
        'searchable': False,
        'applyable': False,
        'li_easy_applyable': False,
        'ats_code': None,
        'meta_data': {},
        'update_date': None,
        'create_date': None,
        'category': [],
        'full_location': None,
        'short_location': None,
        'location_name': None,
        'country': None,
        'tags1': [],
        'tags2': [],
        'tags8': [],
        'department': None,
        'recruiter_id': None,
        'posted_date': None,
        'posting_expiry_date': None,
        'work_hours': None,
        'salary_frequency': None
    }
    
    for field, default_value in fields_defaults.items():
        if field not in item or item[field] is None:
            item[field] = default_value
    return item

class DatabasePipeline:
    def open_spider(self, spider):
        try:
            self.conn = get_postgres_connection()
            self.cur = self.conn.cursor()
            # Create the table if it doesn't exist
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS raw_table (
                    slug VARCHAR,
                    language VARCHAR,
                    languages JSON,
                    req_id VARCHAR PRIMARY KEY,
                    title VARCHAR,
                    description TEXT,
                    street_address VARCHAR,
                    city VARCHAR,
                    state VARCHAR,
                    country_code VARCHAR,
                    postal_code VARCHAR,
                    location_type VARCHAR,
                    latitude FLOAT,
                    longitude FLOAT,
                    categories JSON,
                    tags JSON,
                    tags5 JSON,
                    tags6 JSON,
                    brand VARCHAR,
                    promotion_value FLOAT,
                    salary_currency VARCHAR,
                    salary_value FLOAT,
                    salary_min_value FLOAT,
                    salary_max_value FLOAT,
                    benefits JSON,
                    employment_type VARCHAR,
                    hiring_organization VARCHAR,
                    source VARCHAR,
                    apply_url VARCHAR,
                    internal BOOLEAN,
                    searchable BOOLEAN,
                    applyable BOOLEAN,
                    li_easy_applyable BOOLEAN,
                    ats_code VARCHAR,
                    meta_data JSON,
                    update_date TIMESTAMP,
                    create_date TIMESTAMP,
                    category JSON,
                    full_location VARCHAR,
                    short_location VARCHAR,
                    location_name VARCHAR,
                    country VARCHAR,
                    tags1 JSON,
                    tags2 JSON,
                    tags8 JSON,
                    department VARCHAR,
                    recruiter_id VARCHAR,
                    posted_date VARCHAR,
                    posting_expiry_date TIMESTAMP,
                    work_hours VARCHAR,
                    salary_frequency VARCHAR
                );
            """)
            self.conn.commit()  
        except Exception as e:
            spider.logger.error(f"Failed to create table in PostgreSQL: {e}")

    def close_spider(self, spider):
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except Exception as e:
            spider.logger.error(f"Failed to close PostgreSQL connection: {e}")


    def process_item(self, item, spider):
        item = normalize_item(item)
        
        # Convert dates to timestamps
        for date_field in ['update_date', 'create_date', 'posting_expiry_date']:
            if item[date_field]:
                try:
                    item[date_field] = datetime.strptime(item[date_field], '%Y-%m-%dT%H:%M:%S%z')
                except ValueError:
                    spider.logger.warning(f"Invalid date format in field {date_field}: {item[date_field]}")
                    item[date_field] = None

        try:
            # Insert into PostgreSQL, converting JSON-compatible fields where needed
            self.cur.execute("""
                INSERT INTO raw_table (
                    slug, language, languages, req_id, title, description, street_address, city, state, country_code,
                    postal_code, location_type, latitude, longitude, categories, tags, tags5, tags6, brand,
                    promotion_value, salary_currency, salary_value, salary_min_value, salary_max_value, benefits,
                    employment_type, hiring_organization, source, apply_url, internal, searchable, applyable,
                    li_easy_applyable, ats_code, meta_data, update_date, create_date,
                    category, full_location, short_location, location_name, country, tags1, tags2, tags8, department,
                    recruiter_id, posted_date, posting_expiry_date, work_hours, salary_frequency
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                ) ON CONFLICT (req_id) DO NOTHING
            """, (
                item['slug'], item['language'], json.dumps(item['languages']), item['req_id'], item['title'], 
                item['description'], item['street_address'], item['city'], item['state'], item['country_code'], 
                item['postal_code'], item['location_type'], item['latitude'], item['longitude'], 
                json.dumps(item['categories']), json.dumps(item['tags']), json.dumps(item['tags5']), 
                json.dumps(item['tags6']), item['brand'], item['promotion_value'], item['salary_currency'], 
                item['salary_value'], item['salary_min_value'], item['salary_max_value'], json.dumps(item['benefits']), 
                item['employment_type'], item['hiring_organization'], item['source'], item['apply_url'], 
                item['internal'], item['searchable'], item['applyable'], item['li_easy_applyable'], item['ats_code'], 
                json.dumps(item['meta_data']), item['update_date'], item['create_date'], json.dumps(item['category']), 
                item['full_location'], item['short_location'], item['location_name'], item['country'], 
                json.dumps(item['tags1']), json.dumps(item['tags2']), json.dumps(item['tags8']), item['department'], 
                item['recruiter_id'], item['posted_date'], item['posting_expiry_date'], item['work_hours'], 
                item['salary_frequency']
            ))
        except Exception as e:
            spider.logger.error(f"Failed to insert item into PostgreSQL: {e}")
            self.conn.rollback()
        
        return item





class CachePipeline:
    def open_spider(self, spider):
        try:
            self.redis_conn = get_redis_connection()
        except Exception as e:
            spider.logger.error(f"Failed to connect to Redis: {e}")

    def close_spider(self, spider):
        try:
            self.redis_conn.close()
        except Exception as e:
            spider.logger.error(f"Failed to close Redis connection: {e}")

    def process_item(self, item, spider):
        item_id = item.get('req_id')
        if not item_id:
            spider.logger.warning("Item is missing a unique identifier.")
            return item

        try:
            if self.redis_conn.exists(item_id):
                spider.logger.info(f"Duplicate item found: {item_id}")
                return None
            self.redis_conn.set(item_id, 1)
        except Exception as e:
            spider.logger.error(f"Redis operation failed for item {item_id}: {e}")
        
        return item



class MongoPipeline:
    def open_spider(self, spider):
        try:
            self.client = get_mongo_connection()
            self.db = self.client['jobs_db']
            self.collection = self.db['raw_collection']
            self.collection.create_index("req_id", unique=True)
        except Exception as e:
            spider.logger.error(f"Failed to connect to MongoDB: {e}")

    def close_spider(self, spider):
        try:
            self.client.close()
        except Exception as e:
            spider.logger.error(f"Failed to close MongoDB connection: {e}")

    def process_item(self, item, spider):
        item = normalize_item(item)
        try:
            # Check if the item with the same req_id already exists
            if not self.collection.find_one({'req_id': item['req_id']}):
                # Insert only if there's no existing item with the same req_id
                self.collection.insert_one(dict(item))
            else:
                spider.logger.info(f"Duplicate item found with req_id: {item['req_id']}. Skipping insertion.")
        except Exception as e:
            spider.logger.error(f"Failed to insert item in MongoDB: {e}")
        
        return item
