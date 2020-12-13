python3 -m pip install numpy
pip3 install pandas

#convert raw data
song_df.to_excel("millionsong.xlsx")

#importing all the required libraries
import numpy as np
import pandas as pd

#importing both the datasets
songmetadata = pd.read_csv(r'Destop\song_data.csv')
#one of the file is a text file hence we import it with pd.read_fwf

#fwf stands for fixed width file
othersongdata = pd.read_fwf(r'Destop\10000.txt')
#naming the columns for the othersongdata
othersongdata.columns = ['user_id','song_id','listen_count’]
                         
#merging both the datasets and removing duplicates
song_df = pd.merge(othersongdata, songmetadata.drop_duplicates(['song_id']), on="song_id", how="left")

#writing the file in .csv to visualize in Tableau
song_df.to_csv(r'Destop\Tableau.csv', index = False)

                         
import numpy as np
import pandas as pd
songmetadata = pd.read_csv(r'Destop\song_data.csv')
othersongdata = pd.read_fwf(r'Destop\10000.txt')
othersongdata.columns = ['user_id','song_id','listen_count’]
song_df = pd.merge(othersongdata, songmetadata.drop_duplicates(['song_id']), on="song_id", how="left")
song_grouped = pd.DataFrame(song_df.groupby('song_id')['listen_count'].count())
song_grouped = pd.DataFrame(song_df.groupby('song_id')['listen_count'].count())
song_df.astype({'listen_count': 'int32'},{'song_id':'str'}).dtypes
song_df[song_df['song_id'] == 'SOFVZRE12A8C139783']
songs_crosstab = pd.pivot_table(song_df, values = 'listen_count', index = 'user_id', columns = 'song_id’)
songs_crosstab.head()
predictor_song_ratings = songs_crosstab['SOFVZRE12A8C139783']
predictor_song_ratings[predictor_song_ratings>= 1]
similar_songs = songs_crosstab.corrwith(predictor_song_ratings)
corr_listened_song = pd.DataFrame(similar_songs, columns = ['pearsonR'])
corr_listened_song.dropna(inplace = True)
predictor_corr_summary =corr_listened_song.join(song_grouped['listen_count'])
predictor_corr_summary = predictor_corr_summary.sort_values('pearsonR', ascending = False)
final_recommended_songs = predictor_corr_summary[predictor_corr_summary.pearsonR < 0.9999]
final_recommended_songs.sort_values('pearsonR', ascending = False)
final_recommended_songs = final_recommended_songs.reset_index()
song_df_one = song_df.drop(['listen_count'], axis=1)
similar_songs = pd.merge(final_recommended_songs, song_df_one.drop_duplicates(["song_id"]), on="song_id", how="left")
similar_songs = similar_songs.sort_values('pearsonR', ascending = False)
similar_songs.head(50)                        
