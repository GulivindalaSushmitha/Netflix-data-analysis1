#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Seaborn and Matplotlib are handled outside the script


# In[3]:


 #importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("Libraries imported successfully!")


# In[4]:


# loading the cleaned dataset

df = pd.read_csv("Netflix_Cleaned.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

df.head(5)


# In[5]:


# checking country information

print("Country column:")
print(df["country"].head(10))


# In[6]:


# checking missing values in country column

print("Missing country values:")
print(df["country"].isnull().sum())


# In[7]:


# removing extra spaces from country names

df["country"] = df["country"].astype(str).str.strip()

# splitting multiple countries

country_df = df.copy()

country_df["country"] = country_df["country"].str.split(",")

# creating separate row for each country

country_df = country_df.explode("country")

# removing extra spaces

country_df["country"] = country_df["country"].str.strip()

print("Country data cleaned successfully!")

country_df[["title", "country"]].head(10)


# In[8]:


# calculating number of Netflix titles by country

country_counts = country_df["country"].value_counts()

print("Top 20 countries by number of Netflix titles:")
print(country_counts.head(20))


# In[9]:


# creating country ranking table

country_ranking = country_counts.reset_index()

country_ranking.columns = [
    "Country",
    "Content_Count"
]

country_ranking["Rank"] = (
    country_ranking["Content_Count"]
    .rank(method="dense", ascending=False)
    .astype(int)
)

country_ranking = country_ranking[
    ["Rank", "Country", "Content_Count"]
]

country_ranking.head(20)


# In[10]:


# selecting top 10 content-producing countries

top_10_countries = country_counts.head(10)

print("Top 10 Content-Producing Countries:")
print(top_10_countries)


# In[11]:


# visualizing top 10 countries

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_10_countries.values,
    y=top_10_countries.index
)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.show()


# In[12]:


# creating bar chart with values

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    x=top_10_countries.values,
    y=top_10_countries.index
)

plt.title("Top 10 Netflix Content-Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

for i, value in enumerate(top_10_countries.values):
    ax.text(
        value + 20,
        i,
        str(value),
        va="center",
        fontweight="bold"
    )

plt.show()


# In[13]:


# analyzing movies and TV shows by country

country_type = (
    country_df
    .groupby(["country", "type"])
    .size()
    .unstack(fill_value=0)
)

country_type.head(10)


# In[14]:


# selecting top 10 countries

top_country_names = country_counts.head(10).index

top_country_type = country_type.loc[
    country_type.index.intersection(top_country_names)
]

top_country_type


# In[15]:


# visualizing content type by country

top_country_type.plot(
    kind="bar",
    figsize=(14, 7)
)

plt.title("Movies vs TV Shows in Top Netflix Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.legend(title="Content Type")

plt.tight_layout()

plt.show()


# In[16]:


# identifying the country with the highest content count

top_country = country_counts.index[0]
top_country_count = country_counts.iloc[0]

print("Top Content-Producing Country:", top_country)
print("Number of Titles:", top_country_count)


# In[17]:


# displaying top 5 countries

for i, (country, count) in enumerate(
    country_counts.head(5).items(),
    start=1
):
    print(f"{i}. {country} - {count} titles")


# In[19]:


# generating business insights

print("=" * 55)
print("          BUSINESS INSIGHTS")
print("=" * 55)

print(
    f"\n1. The country with the highest number of "
    f"Netflix titles is {top_country}."
)

print(
    f"2. It has approximately {top_country_count} "
    f"titles in the dataset."
)

print("\n3. Top 5 content-producing countries:")

for i, (country, count) in enumerate(
    country_counts.head(5).items(),
    start=1
):
    print(f"   {i}. {country}: {count} titles")

print(
    "\n4. Country-wise analysis helps identify "
    "major Netflix content-producing markets."
)

print(
    "5. This information can help businesses understand "
    "geographic content distribution and market focus."
)


# In[20]:


# displaying top 20 country ranking

country_ranking.head(20)


# In[21]:


# exporting country analysis

country_ranking.to_csv(
    "Netflix_Country_Analysis.csv",
    index=False
)

print("Country analysis exported successfully!")
print("File: Netflix_Country_Analysis.csv")


# In[ ]:





# In[ ]:




