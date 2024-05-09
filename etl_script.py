import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Connect to PostgreSQL database
engine = create_engine(f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

# Load data from Heart Disease Dataset.csv into a pandas DataFrame
data = pd.read_csv("Heart_Disease_Dataset.csv")

# Transform data if needed
# For example, select relevant columns and rename them
transformed_data = data[['age', 'sex', 'cp', 'chol',]]

# Load transformed data into PostgreSQL database
transformed_data.to_sql('heart_disease_data_copy', engine, if_exists='replace', index=False)
