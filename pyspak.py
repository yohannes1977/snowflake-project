

#read data from snowflake database in customer table
import snowflake.connector
import pandas as pd


conn = snowflake.connector.connect(
    user="YOHANNES",
    password="Yoteke19771985@",
    account="XVARSSD-VKC56305",      
    warehouse="COMPUTE_WH",
    database="SNOWFLAKE_LEARNING_DB",
    schema="PUBLIC"
)

df = pd.read_sql("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER LIMIT 10;", conn)



print(df)
conn.close()