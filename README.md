# Team 134 Group Project - The Sound of Music

## Description
This repository, or package of files, contains all of the work completed for the DVA Fall 2023 course project - "The Sound of Music". This project is an analysis of how the characteristics of music transformed over the years across genres and geographies.

The `data_cleaning.py` script performs a series of data cleaning tasks on the original dataset of Spotify songs, such as removing unicode characters and standardizing the date information. The `Wikipedia_Genre_Merge.ipynb` Python notebook is used to call the Wikipedia API to obtain further genre information for each artist in the dataset. It then merges this information to create a final dataset. 

The `Anomaly Detection.ipynb` Python notebook calculates anomalies across the Spotify songs to determine which genres saw the most anomalous behaviors and which artists may have been behind this.

Finally, the two visualizations are stored in the `index.html` and `interactive map` files. The former leverages D3.js to build an interactive line chart of music characteristics over time for each genre. The latter includes a link to an interative world map which shows the color-coded genres over time and across different countries (based on the primary artist's country of origin).

Some supplementary comparison maps are stored in the `dropdown.zip` folder. The folder includes `map_by_genre.html` which displays two maps based on the genre selected from the dropdown menu, and a subfolder called `maps` that contains all the raw graphs. The `comparison_maps.ipynb` Python notebook generates these comparison maps.

Additionally, `spotify_data_with_coords.csv` file is the finalized dataset with genre and geographic information, and `CSE 6242 Team #134 Poster.pdf` is our final presentation poster.

## Installation
Install the requirements.txt file using `pip install -r requirements.txt`. It's best to use a virtual environment to contain all of the necessary packages into a separate directory.

## Execution
Once the packages are installed, follow these steps:

1. Use the `data_cleaning.py` script to clean the original data downloaded from here: https://github.com/jesperhemmingsson/Spotify-EDA/tree/master/data. This will create a `cleaned_spotify_data.csv`.
2. Run the `Wikipedia_Genre_Merged.ipynb` cells in order to extract genres per song. This will create the `Spotify Dataset - Genres Cleaned.csv`.
3. Run the `Anomaly Detection.ipynb` cells to determine the anomalous points in the music history. This will create the `filtered_anomalies.csv` file.
4. Use the `index.html` and `interactive map` files to interactively analyze the data, choosing different genres to compare over time and attributes.
5. Download the `dropdown.zip` folder and use the `map_by_genre.html` file to see the direct comparison maps (before vs after 1975) of top 10 genres. If you wish to recreate these graphs, run the `comparison_maps.ipynb` cells to see the demo.
