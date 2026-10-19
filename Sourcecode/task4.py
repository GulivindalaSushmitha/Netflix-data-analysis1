#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Seaborn and Matplotlib are handled outside the script


# In[3]:


# importing necessary libraries

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


# checking release year information

print("Data type of release_year:")
print(df["release_year"].dtype)

print("\nMinimum Release Year:")
print(df["release_year"].min())

print("\nMaximum Release Year:")
print(df["release_year"].max())


# In[6]:


# calculating number of Netflix titles released each year

year_counts = (
    df["release_year"]
    .value_counts()
    .sort_index()
)

print("Yearly Content Releases:")
print(year_counts)


# In[7]:


# creating a yearly content analysis table

year_analysis = year_counts.reset_index()

year_analysis.columns = [
    "Release_Year",
    "Content_Count"
]

year_analysis.head(20)


# In[8]:


# displaying content releases from 2000 onwards

recent_years = year_analysis[
    year_analysis["Release_Year"] >= 2000
]

recent_years.head()


# In[9]:


# visualizing Netflix content releases by year

plt.figure(figsize=(14, 6))

plt.plot(
    year_analysis["Release_Year"],
    year_analysis["Content_Count"],
    marker="o"
)

plt.title("Netflix Content Releases by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()


# In[10]:


# visualizing the trend from 2000 onwards

plt.figure(figsize=(14, 6))

plt.plot(
    recent_years["Release_Year"],
    recent_years["Content_Count"],
    marker="o"
)

plt.title("Netflix Content Release Trend Since 2000")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()


# In[11]:


# creating a seaborn trend chart

plt.figure(figsize=(14, 6))

sns.lineplot(
    data=recent_years,
    x="Release_Year",
    y="Content_Count",
    marker="o"
)

plt.title("Netflix Content Production Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()


# In[12]:


# finding the year with the highest number of releases

peak_year = year_counts.idxmax()
peak_count = year_counts.max()

print("Peak Release Year:", peak_year)
print("Number of Titles Released:", peak_count)


# In[13]:


# finding the year with the lowest number of releases

lowest_year = year_counts.idxmin()
lowest_count = year_counts.min()

print("Lowest Release Year:", lowest_year)
print("Number of Titles:", lowest_count)


# In[14]:


# calculating yearly releases by content type

year_type = (
    df.groupby(["release_year", "type"])
    .size()
    .reset_index(name="Content_Count")
)

print(year_type.head(5))
print("=" * 44)
print(year_type.tail(5))


# In[15]:


# filtering data from 2000 onwards

recent_year_type = year_type[
    year_type["release_year"] >= 2000
]

plt.figure(figsize=(14, 7))

sns.lineplot(
    data=recent_year_type,
    x="release_year",
    y="Content_Count",
    hue="type",
    marker="o"
)

plt.title("Movies vs TV Shows Release Trend Since 2000")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.legend(title="Content Type")

plt.show()


# In[16]:


# finding the years with the highest number of releases

top_release_years = (
    df["release_year"]
    .value_counts()
    .head(10)
)

print("Top 10 Release Years:")
print(top_release_years)


# In[17]:


# visualizing top 10 release years

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_release_years.values,
    y=top_release_years.index.astype(str)
)

plt.title("Top 10 Years by Netflix Content Releases")
plt.xlabel("Number of Titles")
plt.ylabel("Release Year")

plt.show()


# In[18]:


# calculating year-to-year change

year_analysis["Yearly_Change"] = (
    year_analysis["Content_Count"].diff()
)

year_analysis["Growth_Percentage"] = (
    year_analysis["Content_Count"]
    .pct_change() * 100
)

year_analysis.tail(20)


# In[19]:


# displaying growth analysis from 2000 onwards

recent_growth = year_analysis[
    year_analysis["Release_Year"] >= 2000
].copy()

recent_growth[
    [
        "Release_Year",
        "Content_Count",
        "Yearly_Change",
        "Growth_Percentage"
    ]
].tail(20)


# In[20]:


# visualizing yearly growth percentage

plt.figure(figsize=(14, 6))

plt.plot(
    recent_growth["Release_Year"],
    recent_growth["Growth_Percentage"],
    marker="o"
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.title("Yearly Netflix Content Growth Percentage")
plt.xlabel("Release Year")
plt.ylabel("Growth (%)")

plt.show()


# In[21]:


# generating business insights

print("=" * 60)
print("           TASK 4 - BUSINESS INSIGHTS")
print("=" * 60)

print(
    f"\n1. Peak release year: {peak_year}"
)

print(
    f"2. Number of titles released during the peak year: "
    f"{peak_count}"
)

print(
    f"3. Lowest release year in the dataset: {lowest_year}"
)

print(
    f"4. Number of titles in that year: {lowest_count}"
)

print(
    "\n5. The release-year analysis helps identify "
    "periods of increasing and decreasing content production."
)

print(
    "6. Comparing Movies and TV Shows shows how the "
    "content mix has changed over time."
)


# In[22]:


# exporting yearly analysis

year_analysis.to_csv(
    "Netflix_Year_Analysis.csv",
    index=False
)

print("Yearly analysis exported successfully!")
print("File: Netflix_Year_Analysis.csv")

