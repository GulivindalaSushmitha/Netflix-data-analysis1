#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Seaborn and Matplotlib are handled outside the script


# In[2]:


# importing necessary libraries

import pandas as pd
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


# checking rating categories

print("Rating Categories:")
print(df["rating"].unique())


# In[5]:


# counting each rating category

rating_counts = df["rating"].value_counts()

print("Netflix Rating Distribution:")
print(rating_counts)


# In[6]:


# visualizing rating distribution

plt.figure(figsize=(12, 6))

sns.countplot(
    data=df,
    y="rating",
    order=rating_counts.index
)

plt.title("Netflix Content Rating Distribution")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")

plt.show()


# In[7]:


# creating rating summary table

rating_summary = rating_counts.reset_index()

rating_summary.columns = [
    "Rating",
    "Number_of_Titles"
]

rating_summary


# In[8]:


# checking genre information

print("Genre information:")
print(df["listed_in"].head(10))


# In[9]:


# creating a copy of the dataset

genre_df = df.copy()

# splitting multiple genres

genre_df["listed_in"] = genre_df["listed_in"].str.split(",")

# creating separate row for each genre

genre_df = genre_df.explode("listed_in")

# removing extra spaces

genre_df["listed_in"] = genre_df["listed_in"].str.strip()

print("Genre data cleaned successfully!")

genre_df[["title", "listed_in"]].head(10)


# In[10]:


# counting the number of titles in each genre

genre_counts = genre_df["listed_in"].value_counts()

print("Top 20 Netflix Genres:")
print(genre_counts.head(20))


# In[11]:


# selecting top 10 genres

top_10_genres = genre_counts.head(10)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_10_genres.values,
    y=top_10_genres.index
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.show()


# In[12]:


# creating genre summary table

genre_summary = genre_counts.reset_index()

genre_summary.columns = [
    "Genre",
    "Number_of_Titles"
]

genre_summary.head(20)


# In[13]:


# creating rating and content type table

rating_type = (
    df.groupby(["rating", "type"])
    .size()
    .reset_index(name="Number_of_Titles")
)

rating_type.head(20)


# In[14]:


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


# In[15]:


# calculating rating percentages by content type

rating_type_percentage = (
    pd.crosstab(
        df["rating"],
        df["type"],
        normalize="columns"
    ) * 100
)

rating_type_percentage.round(2)


# In[16]:


# creating a heatmap for rating distribution

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


# In[17]:


# finding the most common rating

most_common_rating = rating_counts.idxmax()
most_common_rating_count = rating_counts.max()

print("Most Common Rating:", most_common_rating)
print("Number of Titles:", most_common_rating_count)


# In[18]:


# finding the most common genre

most_common_genre = genre_counts.idxmax()
most_common_genre_count = genre_counts.max()

print("Most Common Genre:", most_common_genre)
print("Number of Titles:", most_common_genre_count)


# In[19]:


# finding the most common movie rating

movie_ratings = (
    df[df["type"] == "Movie"]["rating"]
    .value_counts()
)

print("Most Common Movie Rating:")
print(movie_ratings.head(10))


# In[20]:


print(df["type"].unique())
print(df["type"].value_counts())


# In[21]:


# cleaning the type column

df["type"] = df["type"].astype(str).str.strip()

print(df["type"].unique())
print(df["type"].value_counts())


# In[22]:


# finding the most common TV Show rating

tv_ratings = (
    df[df["type"].str.lower() == "tv show"]["rating"]
    .value_counts()
)

print("Most Common TV Show Rating:")
print(tv_ratings.head(10))


# In[23]:


# identifying most common ratings

top_movie_rating = movie_ratings.idxmax()
top_movie_rating_count = movie_ratings.max()

top_tv_rating = tv_ratings.idxmax()
top_tv_rating_count = tv_ratings.max()

print("Most Common Movie Rating:")
print(top_movie_rating, "-", top_movie_rating_count)

print("\nMost Common TV Show Rating:")
print(top_tv_rating, "-", top_tv_rating_count)


# In[24]:


# generating audience insights

print("=" * 60)
print("           TASK 5 - AUDIENCE INSIGHTS")
print("=" * 60)

print(
    f"\n1. The most common Netflix rating is "
    f"{most_common_rating}."
)

print(
    f"   Number of titles: {most_common_rating_count}"
)

print(
    f"\n2. The most common Netflix genre is "
    f"{most_common_genre}."
)

print(
    f"   Number of titles: {most_common_genre_count}"
)

print(
    f"\n3. The most common Movie rating is "
    f"{top_movie_rating}."
)

print(
    f"4. The most common TV Show rating is "
    f"{top_tv_rating}."
)

print(
    "\n5. Rating analysis helps identify the primary "
    "audience segments targeted by Netflix."
)

print(
    "6. Genre analysis helps identify the types of "
    "content that are most widely represented."
)

print(
    "7. Comparing Movies and TV Shows reveals differences "
    "in their audience targeting."
)


# In[25]:


# exporting rating analysis

rating_summary.to_csv(
    "Netflix_Rating_Analysis.csv",
    index=False
)

# exporting genre analysis

genre_summary.to_csv(
    "Netflix_Genre_Analysis.csv",
    index=False
)

# exporting rating vs content type analysis

rating_type.to_csv(
    "Netflix_Rating_Type_Analysis.csv",
    index=False
)

print("Task 5 analysis files exported successfully!")

print("\nFiles created:")
print("1. Netflix_Rating_Analysis.csv")
print("2. Netflix_Genre_Analysis.csv")
print("3. Netflix_Rating_Type_Analysis.csv")


# In[ ]:





# In[ ]:




