# Lab 3: The Social Media Data Detective

## Project Overview
This project processes a dataset of Twitter posts (`twitter_dataset.csv`) to clean missing values, identify top-performing posts, search by keywords, and extract user activity analytics using Python and Bash.

## Features & Implementation

### 1. Python Data Detective (`data-detective.py`)
- **Quest 1 (Data Cleaning)**: Filters out tweets missing text content and sets empty or invalid `Likes`/`Retweets` fields to `0`.
- **Quest 2 (Viral Tweet)**: Iterates through the dataset manually to find the tweet with the highest number of likes without using Python's built-in `max()`.
- **Quest 3 (Custom Sorting)**: Implements **Bubble Sort** to sort tweets by likes in descending order without using `.sort()` or `sorted()`.
- **Quest 4 (Content Filter)**: Extracts and counts tweets containing a user-specified keyword.

### 2. Bash Feed Analyzer (`feed-analyzer.sh`)
Uses a single terminal pipeline chaining `tr`, `cut`, `grep`, `sort`, `uniq`, and `head` to extract the Top 5 Most Active Users directly from the command line.

## How to Run

1. Execute the Python Data Detective script:
   ```bash
   python3 data-detective.py