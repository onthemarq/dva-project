# Team 134 Group Project - The Sound of Music

## Description
This repository, or package of files, contains all of the work completed for the DVA Fall 2023 course project - "The Sound of Music". This project is an analysis of how the characteristics of music transformed over the years across genres and geographies.

The `data_cleaning.py` script performs a series of data cleaning tasks on the original dataset of Spotify songs, such as removing unicode characters and standardizing the date information. The `Wikipedia_Genre_Merge.ipynb` python notebook is used to call the Wikipedia API to obtain further geographic information for each artist in the dataset. It then merges this information to create a final dataset. 

The `Anomaly Detection.ipynb` python notebook calculates anomalies across the Spotify songs to determine which genres saw the most anomalous behaviors and which artists may have been behind this.

Finally, the two visualizations are created in the `index.html` and `comparison_maps.ipynb` files. The former leverages D3.js to building an interactive line chart of music characteristics over time for each genre. The latter develops maps which show the comparison of a genre over time and across different countries (based on the primary artist's country of origin). 

## Installation
Install the requirements.txt file using `pip install -r requirements.txt`. It's best to use a virtual environment to contain all of the necessary packages into a separate directory.

## Execution
Once the packages are installed, follow these steps:

1. Use the `data_cleaning.py` script to clean the `data.csv` file. This will create a `cleaned_spotify_data.csv`.
2. Run the `Wikipedia_Genre_Merged.ipynb` cells in order to extract geographic information per primary artist. This will create the `Spotify Dataset - Genres Cleaned.csv`.
3. Run the `Anomaly Detection.ipynb` cells to determine the anomalous points in the music history. This will create the `filtered_anomalies.csv` file.
4. Use the `index.html` and `comparison_maps.ipynb` files to interactively analyze the data, choosing different genres to compare over time and characteristics.