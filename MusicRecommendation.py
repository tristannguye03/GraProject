import os
from math import sqrt
from itertools import islice

import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import train_test_split

%%time
d_path = "data/kaggle_visible_evaluation_triplets.txt"
new_path = "data/song_data.csv"
with open(d_path, "r") as f1, open(new_path, "w") as f2:
    i = 0
    f2.write("user_id,song_id,listen_count\n")
    while True:
        next_n_lines = list(islice(f1, 9))
        if not next_n_lines:
            break

        # process next_n_lines: get user_id,song_id,listen_count info
        output_line = ""
        for line in next_n_lines:
            user_id, song, listen_count = line.split("\t")
            output_line += "{},{},{}\n".format(user_id, song, listen_count.strip())
        f2.write(output_line)
        
        # print status
        i += 1
        if i % 20000 == 0:
            print "%d songs converted..." % i
def load_music_data(file_name):
    """Get reviews data, from local csv."""
    if os.path.exists(file_name):
        print("-- " + file_name + " found locally")
        df = pd.read_csv(file_name)
 
    return df
 
# Load music data with sampling fraction = 0.01 for reduce processing time.
song_data = load_music_data(new_path)
song_data = song_data.sample(frac=0.01, replace=False)
 
print "-- Explore data"
display(song_data.head())
 
n_users = song_data.user_id.unique().shape[0]
n_items = song_data.song_id.unique().shape[0]
print "Number of users = " + str(n_users) + " | Number of songs = " + str(n_items)

print "-- Showing the most popular songs in the dataset"
unique, counts = np.unique(song_data["song_id"], return_counts=True)
popular_songs = dict(zip(unique, counts))
df_popular_songs = pd.DataFrame(popular_songs.items(), columns=["Song", "Count"])
df_popular_songs = df_popular_songs.sort_values(by=["Count"], ascending=False)
df_popular_songs.head()


