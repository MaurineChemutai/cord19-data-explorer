# ...existing code...
#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional imports (handle missing packages gracefully)
try:
    from wordcloud import WordCloud
except Exception:
    WordCloud = None

try:
    import streamlit as st
except Exception:
    st = None

# Path to CSV (adjust if needed)
CSV_PATH = r"C:\Users\hp\metadata.csv"

# Load data
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV file not found at: {CSV_PATH}")

df = pd.read_csv(CSV_PATH)

# Convert publish_time to datetime first, then drop rows missing title or publish_time
df["publish_time"] = pd.to_datetime(df.get("publish_time"), errors="coerce")
df = df.dropna(subset=["title", "publish_time"])

# Derived columns
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df.get("abstract", "").fillna("").astype(str).apply(lambda x: len(x.split()))

# Basic info (console)
def print_basic_info(dataframe):
    print("Shape:", dataframe.shape)
    print(dataframe.info())
    print("Missing values:\n", dataframe.isnull().sum())
    print("Describe:\n", dataframe.describe(include="all"))

# Plot helpers
def plot_publications_by_year(dataframe, use_streamlit=False):
    if "year" not in dataframe.columns or dataframe["year"].dropna().empty:
        print("No year data to plot.")
        return
    year_counts = dataframe["year"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(year_counts.index.astype(int), year_counts.values)
    ax.set_title("Publications by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Count")
    plt.tight_layout()
    if use_streamlit and st:
        st.pyplot(fig)
    else:
        plt.show()
    plt.close(fig)

def plot_top_journals(dataframe, top_n=10, use_streamlit=False):
    if "journal" not in dataframe.columns:
        print("No journal column found.")
        return
    top_journals = dataframe["journal"].fillna("Unknown").value_counts().head(top_n)
    if top_journals.empty:
        print("No journal data to plot.")
        return
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
    ax.set_title("Top Journals Publishing COVID-19 Research")
    ax.set_xlabel("Count")
    plt.tight_layout()
    if use_streamlit and st:
        st.pyplot(fig)
    else:
        plt.show()
    plt.close(fig)

def plot_title_wordcloud(dataframe, use_streamlit=False):
    import gc
    if WordCloud is None:
        msg = "wordcloud package not installed; skipping word cloud."
        if use_streamlit and st:
            st.warning(msg)
        else:
            print(msg)
        return

    # Run garbage collection before large operations
    gc.collect()

    # Drop missing titles
    titles = dataframe["title"].dropna().astype(str)
    if titles.empty:
        print("No titles for word cloud.")
        return

    # Sample to avoid memory issues (limit to 1000 titles)
    if len(titles) > 1000:
        titles = titles.sample(n=1000, random_state=42)

    # Join into single text
    text = " ".join(titles)

    # Configure smaller and memory-efficient word cloud
    wc = WordCloud(
        width=600, 
        height=300, 
        background_color="white", 
        max_words=300, 
        max_font_size=60
    ).generate(text)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("Word Cloud of Paper Titles")
    plt.tight_layout()

    if use_streamlit and st:
        st.pyplot(fig)
    else:
        plt.show()

    plt.close(fig)
    gc.collect()

# Script entry (non-Streamlit)
if __name__ == "__main__" and st is None:
    print_basic_info(df)
    plot_publications_by_year(df, use_streamlit=False)
    plot_top_journals(df, use_streamlit=False)
    plot_title_wordcloud(df, use_streamlit=False)

# Streamlit app (if streamlit is available)
if st:
    st.title("CORD-19 Data Explorer")
    st.write("Simple exploration of COVID-19 research papers")

    # slider bounds derived from data
    if df["year"].dropna().empty:
        min_year, max_year = 2019, 2023
    else:
        min_year = int(df["year"].min())
        max_year = int(df["year"].max())
    default_range = (max(min_year, 2019), max_year)

    year_range = st.slider("Select Year Range", min_year, max_year, default_range)
    filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

    if filtered.empty:
        st.write("No records for selected year range.")
    else:
        year_counts = filtered["year"].value_counts().sort_index()
        st.bar_chart(year_counts)
        st.dataframe(filtered.head())
        plot_top_journals(filtered, use_streamlit=True)
        plot_title_wordcloud(filtered, use_streamlit=True)
# ...existing code...

