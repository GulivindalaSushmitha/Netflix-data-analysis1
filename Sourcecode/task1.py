#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing necessary libraries

import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

print("Libraries imported successfully!")


# In[7]:


# loading the dataset

df = pd.read_csv(r"C:\Users\SUSHMITHA\Desktop\Auspify_Netflix_Data_Analysis\Datasets\Dataset.csv")

print("Dataset loaded successfully!")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# In[8]:


# displaying the first 5 rows of the dataset

df.head(5)


# In[9]:


# displaying the last 5 rows of the dataset
df.tail(5)


# In[10]:


# Dataset information

df.info()


# In[11]:


# Dataset shape

rows, columns = df.shape

print("Rows:", rows)
print("Columns:", columns)


# In[12]:


# Dataset column names

print("Column Names:")

for column in df.columns:
    print(column)


# In[13]:


# Checking for missing values in the dataset

missing_values = df.isnull().sum()

print("Missing Values in Each Column:")
print(missing_values)


# In[14]:


# Calculating the percentage of missing values in each column

missing_percentage = (df.isnull().sum() / len(df)) * 100

missing_table = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage": missing_percentage
})

missing_table


# In[15]:


# Checking for duplicate records in the dataset

duplicate_count = df.duplicated().sum()

print("Number of duplicate records:", duplicate_count)


# In[16]:


# Removing duplicate records from the dataset ( Even though dataset currently has zero duplicates, I have include the cleaning step.)

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print("Rows before removing duplicates:", before_duplicates)
print("Rows after removing duplicates:", after_duplicates)
print("Duplicates removed:", before_duplicates - after_duplicates)


# In[17]:


# Cleaning text columns by removing extra spaces

text_columns = [
    "type",
    "title",
    "director",
    "country",
    "rating",
    "duration",
    "listed_in"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

print("Extra spaces removed from text columns.")


# In[18]:


# Cleaning the "type" column by converting to title case

df["type"] = (    df["type"].str.strip().str.title())

print(df["type"].value_counts())


# In[19]:


# Cleaning the "rating" column by converting to uppercase

df["rating"] = (df["rating"].str.strip().str.upper())

print("Unique Ratings:")
print(df["rating"].unique())


# In[20]:


# Cleaning the "date_added" column by converting to datetime format

df["date_added"] = pd.to_datetime(df["date_added"],errors="coerce")

print(df["date_added"].dtype)


# In[21]:


# Extracting year, month, and month name from the "date_added" column

df["date_added_year"] = df["date_added"].dt.year
df["date_added_month"] = df["date_added"].dt.month
df["date_added_month_name"] = df["date_added"].dt.month_name()

print(df[[
    "date_added",
    "date_added_year",
    "date_added_month",
    "date_added_month_name"
]].head())


# In[22]:


# Checking the data type of the "release_year" column and its minimum and maximum values

print("Release Year Data Type:")
print(df["release_year"].dtype)

print("\nMinimum Release Year:")
print(df["release_year"].min())

print("\nMaximum Release Year:")
print(df["release_year"].max())


# In[23]:


# Cleaning the "duration" column by extracting the numeric value and converting it to float

df["duration_value"] = (df["duration"].str.extract(r"(\d+)").astype(float))

print(df[["duration", "duration_value"]].head(10))


# In[24]:


# checking the unique values in the "type" column

print("Content Types:")
print(df["type"].unique())


# In[25]:


# checking the unique values in the "rating" column

print("Number of unique ratings:", df["rating"].nunique())

print("\nRatings:")
print(sorted(df["rating"].unique()))


# In[26]:


# final check for missing values after cleaning

final_missing = df.isnull().sum()

print("Final Missing Values:")
print(final_missing)


# In[27]:


# final check for duplicate records after cleaning

final_duplicates = df.duplicated().sum()

print("Final duplicate records:", final_duplicates)


# In[28]:


# Final dataset information after cleaning

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# In[29]:


# displaying the first 5 rows of the cleaned dataset

df.head(5)


# In[30]:


# Exporting the cleaned dataset to a new CSV file

df.to_csv(
    "Netflix_Cleaned.csv",
    index=False
)

print("Cleaned dataset exported successfully!")
print("File name: Netflix_Cleaned.csv")


# In[31]:


# Loading the cleaned dataset to verify the export

cleaned_df = pd.read_csv("Netflix_Cleaned.csv")

print("Cleaned dataset successfully loaded!")
print("Shape:", cleaned_df.shape)

cleaned_df.head()


# In[ ]:




