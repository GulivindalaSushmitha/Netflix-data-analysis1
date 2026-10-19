#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Seaborn and Matplotlib are handled outside the script


# In[2]:


# importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("Libraries imported successfully!")


# In[3]:


# loading the cleaned Netflix dataset

df = pd.read_csv("Netflix_Cleaned.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

df.head(5)


# In[4]:


# checking dataset information

print("=" * 60)
print("              DATASET INFORMATION")
print("=" * 60)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# In[5]:


# checking missing values

missing_values = df.isnull().sum()

print("Missing Values:")
print(missing_values)


# In[6]:


# displaying only columns with missing values

missing_summary = (
    df.isnull()
    .sum()
    .reset_index()
)

missing_summary.columns = [
    "Column",
    "Missing_Values"
]

missing_summary = missing_summary[
    missing_summary["Missing_Values"] > 0
]

missing_summary


# In[7]:


# calculating content type distribution

content_counts = df["type"].value_counts()

print("Content Type Distribution:")
print(content_counts)


# In[8]:


# visualizing content type distribution

plt.figure(figsize=(8, 5))

sns.barplot(
    x=content_counts.index,
    y=content_counts.values
)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.show()


# In[9]:


# calculating content type percentages

content_percentage = (
    df["type"]
    .value_counts(normalize=True) * 100
)

print("Content Type Percentage:")
print(content_percentage.round(2))


# In[10]:


# preparing country information

country_df = df.copy()

country_df["country"] = (
    country_df["country"]
    .fillna("Unknown")
    .astype(str)
    .str.split(",")
)

country_df = country_df.explode("country")

country_df["country"] = (
    country_df["country"]
    .str.strip()
)

country_counts = country_df["country"].value_counts()

print("Top 10 Countries:")
print(country_counts.head(10))


# In[11]:


# visualizing top content-producing countries

top_countries = country_counts.head(10)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.show()


# In[12]:


# calculating yearly content releases

year_counts = (
    df["release_year"]
    .value_counts()
    .sort_index()
)

year_analysis = year_counts.reset_index()

year_analysis.columns = [
    "Release_Year",
    "Content_Count"
]

year_analysis.head()


# In[13]:


# visualizing Netflix content release trend

plt.figure(figsize=(14, 6))

plt.plot(
    year_analysis["Release_Year"],
    year_analysis["Content_Count"],
    marker="o"
)

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()


# In[14]:


# analyzing recent content production

recent_years = year_analysis[
    year_analysis["Release_Year"] >= 2000
]

plt.figure(figsize=(14, 6))

sns.lineplot(
    data=recent_years,
    x="Release_Year",
    y="Content_Count",
    marker="o"
)

plt.title("Netflix Content Production Since 2000")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()


# In[15]:


# calculating rating distribution

rating_counts = df["rating"].value_counts()

print("Rating Distribution:")
print(rating_counts)


# In[16]:


# visualizing rating distribution

plt.figure(figsize=(12, 6))

sns.barplot(
    x=rating_counts.values,
    y=rating_counts.index
)

plt.title("Netflix Content Rating Distribution")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")

plt.show()


# In[17]:


# preparing genre information

genre_df = df.copy()

genre_df["listed_in"] = (
    genre_df["listed_in"]
    .fillna("Unknown")
    .astype(str)
    .str.split(",")
)

genre_df = genre_df.explode("listed_in")

genre_df["listed_in"] = (
    genre_df["listed_in"]
    .str.strip()
)

genre_counts = genre_df["listed_in"].value_counts()

print("Top 15 Genres:")
print(genre_counts.head(15))


# In[18]:


# visualizing top 10 genres

top_genres = genre_counts.head(10)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.show()


# In[19]:


# calculating yearly content by type

year_type = (
    df.groupby(["release_year", "type"])
    .size()
    .reset_index(name="Number_of_Titles")
)

recent_year_type = year_type[
    year_type["release_year"] >= 2000
]

recent_year_type.head()


# In[20]:


# visualizing Movies vs TV Shows over time

plt.figure(figsize=(14, 7))

sns.lineplot(
    data=recent_year_type,
    x="release_year",
    y="Number_of_Titles",
    hue="type",
    marker="o"
)

plt.title("Movies vs TV Shows Release Trend Since 2000")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.legend(title="Content Type")

plt.show()


# In[21]:


# calculating key business metrics

total_titles = len(df)

total_movies = (
    df["type"] == "Movie"
).sum()

total_tv_shows = (
    df["type"] == "TV Show"
).sum()

total_countries = country_counts[
    country_counts.index != "Unknown"
].shape[0]

total_genres = genre_counts[
    genre_counts.index != "Unknown"
].shape[0]

most_common_rating = rating_counts.idxmax()
most_common_rating_count = rating_counts.max()

most_common_genre = genre_counts.idxmax()
most_common_genre_count = genre_counts.max()

peak_year = year_counts.idxmax()
peak_year_count = year_counts.max()

top_country = country_counts.index[0]
top_country_count = country_counts.iloc[0]


# In[22]:


# displaying key business metrics

print("=" * 65)
print("                 NETFLIX KPI REPORT")
print("=" * 65)

print(f"\nTotal Titles              : {total_titles}")
print(f"Total Movies              : {total_movies}")
print(f"Total TV Shows            : {total_tv_shows}")
print(f"Countries Represented     : {total_countries}")
print(f"Genres Represented        : {total_genres}")

print(f"\nMost Common Rating        : {most_common_rating}")
print(f"Titles with This Rating  : {most_common_rating_count}")

print(f"\nMost Common Genre         : {most_common_genre}")
print(f"Titles in This Genre     : {most_common_genre_count}")

print(f"\nPeak Release Year         : {peak_year}")
print(f"Titles Released That Year: {peak_year_count}")

print(f"\nTop Content Country       : {top_country}")
print(f"Content Count             : {top_country_count}")


# In[23]:


# creating content type distribution chart

plt.figure(figsize=(7, 7))

plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Type Distribution")

plt.show()


# In[24]:


# comparing ratings across Movies and TV Shows

plt.figure(figsize=(14, 7))

sns.countplot(
    data=df,
    y="rating",
    hue="type",
    order=rating_counts.index
)

plt.title("Netflix Ratings: Movies vs TV Shows")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")

plt.legend(title="Content Type")

plt.show()


# In[25]:


# creating rating percentage heatmap

rating_type_percentage = (
    pd.crosstab(
        df["rating"],
        df["type"],
        normalize="columns"
    ) * 100
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    rating_type_percentage,
    annot=True,
    fmt=".1f"
)

plt.title("Rating Distribution by Content Type (%)")
plt.xlabel("Content Type")
plt.ylabel("Rating")

plt.show()


# In[26]:


# generating final business insights

print("=" * 70)
print("              NETFLIX BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"\n1. CONTENT MIX:"
    f"\n   Netflix has {total_movies} Movies and "
    f"{total_tv_shows} TV Shows."
)

if total_movies > total_tv_shows:
    print(
        "   Movies represent the larger share of the "
        "Netflix catalog."
    )
else:
    print(
        "   TV Shows represent the larger share of the "
        "Netflix catalog."
    )


print(
    f"\n2. TOP CONTENT COUNTRY:"
    f"\n   {top_country} is the leading country in terms "
    f"of listed Netflix content."
)


print(
    f"\n3. CONTENT PRODUCTION TREND:"
    f"\n   The peak release year in this dataset is "
    f"{peak_year}, with {peak_year_count} titles."
)


print(
    f"\n4. MOST COMMON RATING:"
    f"\n   {most_common_rating} is the most frequently "
    f"represented rating."
)


print(
    f"\n5. MOST COMMON GENRE:"
    f"\n   {most_common_genre} is the most frequently "
    f"represented genre."
)


print(
    "\n6. CONTENT STRATEGY:"
    "\n   The analysis can help identify major content "
    "categories and geographic markets."
)


print(
    "\n7. AUDIENCE TARGETING:"
    "\n   Rating and genre distributions provide insight "
    "into the audiences targeted by Netflix."
)


print(
    "\n8. BUSINESS DECISION MAKING:"
    "\n   These trends can support decisions about "
    "content investment, regional expansion and "
    "audience-focused programming."
)


# In[27]:


# creating final summary report

final_summary = pd.DataFrame({
    "Metric": [
        "Total Titles",
        "Total Movies",
        "Total TV Shows",
        "Countries",
        "Genres",
        "Most Common Rating",
        "Most Common Genre",
        "Peak Release Year",
        "Top Content Country"
    ],

    "Value": [
        total_titles,
        total_movies,
        total_tv_shows,
        total_countries,
        total_genres,
        most_common_rating,
        most_common_genre,
        peak_year,
        top_country
    ]
})

final_summary


# In[28]:


# exporting final business report

final_summary.to_csv(
    "Netflix_Business_Insights_Report.csv",
    index=False
)

print("Final business insights report saved successfully!")
print("File: Netflix_Business_Insights_Report.csv")


# In[29]:


# creating a Netflix business dashboard

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# ------------------------------------------
# Chart 1 - Content Type
# ------------------------------------------

sns.barplot(
    x=content_counts.index,
    y=content_counts.values,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Movies vs TV Shows")
axes[0, 0].set_xlabel("Content Type")
axes[0, 0].set_ylabel("Number of Titles")


# ------------------------------------------
# Chart 2 - Top Countries
# ------------------------------------------

sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Top 10 Countries")
axes[0, 1].set_xlabel("Number of Titles")
axes[0, 1].set_ylabel("Country")


# ------------------------------------------
# Chart 3 - Release Trend
# ------------------------------------------

axes[1, 0].plot(
    recent_years["Release_Year"],
    recent_years["Content_Count"],
    marker="o"
)

axes[1, 0].set_title("Content Production Trend")
axes[1, 0].set_xlabel("Release Year")
axes[1, 0].set_ylabel("Number of Titles")


# ------------------------------------------
# Chart 4 - Top Genres
# ------------------------------------------

sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    ax=axes[1, 1]
)

axes[1, 1].set_title("Top 10 Genres")
axes[1, 1].set_xlabel("Number of Titles")
axes[1, 1].set_ylabel("Genre")


plt.suptitle(
    "NETFLIX BUSINESS INSIGHTS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




