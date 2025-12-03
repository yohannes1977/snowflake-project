import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user="YOHANNES",
    password="",
    account="",      
    warehouse="",
    database="SNOWFLAKE_LEARNING_DB",
    schema="PUBLIC"
)

sql_query = "SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER LIMIT 10;"


df = pd.read_sql(sql_query, conn)
print(df)

conn.close()

