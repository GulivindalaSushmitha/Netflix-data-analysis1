#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Seaborn was installed from the terminal


# In[2]:


# importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("Libraries imported successfully!")


# In[4]:


# loading the cleaned dataset

df = pd.read_csv(r"C:\Users\SUSHMITHA\Desktop\Auspify_Netflix_Data_Analysis\Datasets\Netflix Cleaned dataset.csv")
print("Dataset loaded successfully!")
print("Shape:", df.shape)

df.head(5)


# In[5]:


# checking the unique values in the "type" column

print("Content Types:")
print(df["type"].unique())


# In[6]:


# counting the number of movies and TV shows in the dataset

content_counts = df["type"].value_counts()

print("Number of Movies and TV Shows:")
print(content_counts)


# In[7]:


# calculating the percentage of each content type

content_percentage = df["type"].value_counts(normalize=True) * 100

print("Percentage of Each Content Type:")
print(content_percentage.round(2))


# In[8]:


# creating a summary DataFrame for content type analysis

content_summary = pd.DataFrame({
    "Content Type": content_counts.index,
    "Number of Titles": content_counts.values,
    "Percentage": content_percentage.round(2).values
})

content_summary


# In[9]:


# visualizing the distribution of content types using a count plot

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.show()


# In[10]:


# visualizing the distribution of content types using a pie chart

plt.figure(figsize=(7, 7))

plt.pie(
    content_counts.values,
    labels=content_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Netflix Content Type Distribution")

plt.show()


# In[11]:


# visualizing the distribution of content types using a bar plot

plt.figure(figsize=(8, 5))

ax = sns.barplot(
    x=content_counts.index,
    y=content_counts.values
)

plt.title("Number of Movies and TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

for i, value in enumerate(content_counts.values):
    ax.text(
        i,
        value + 50,
        str(value),
        ha="center",
        fontweight="bold"
    )

plt.show()


# In[12]:


# finding the most common content type and its count

most_common_type = content_counts.idxmax()
most_common_count = content_counts.max()

print("Most Common Content Type:", most_common_type)
print("Number of Titles:", most_common_count)


# In[13]:


# calculating the difference in the number of movies and TV shows

movie_count = content_counts.get("Movie", 0)
tv_show_count = content_counts.get("TV Show", 0)

difference = abs(movie_count - tv_show_count)

print("Movies:", movie_count)
print("TV Shows:", tv_show_count)
print("Difference:", difference)


# In[14]:


# providing insights based on the counts of movies and TV shows

if movie_count > tv_show_count:
    print(
        f"Insight: Movies are more common than TV Shows "
        f"by {difference} titles."
    )
elif tv_show_count > movie_count:
    print(
        f"Insight: TV Shows are more common than Movies "
        f"by {difference} titles."
    )
else:
    print("Insight: Movies and TV Shows have the same number of titles.")


# In[ ]:




