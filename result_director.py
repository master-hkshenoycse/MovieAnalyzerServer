import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def get_director_results_display(name):
    data_netflix=pd.read_csv('data/netflix_titles.csv')
    data_netflix=data_netflix.dropna()

    #clear all the previous plots
    plt.clf()

    #subsettting the data for Director
    data_Director=data_netflix[data_netflix['director'].str.contains(name)]

    #getting results for movies by Director for rating distribution
    netflix_movies_df=data_Director[data_Director.type=='Movie']
    count_movies = netflix_movies_df.groupby('rating')['title'].count().reset_index()
    plt.figure(figsize=(12,7))
    plt.title('Amount of Movies by Director vs Rating ')
    plt.xlabel("Rating")
    plt.ylabel("Amount of Movies")
    plt.bar(count_movies.rating, count_movies.title)
    plt.legend(['Movies'])
    plt.title('Movie Rating Distribution for Director')
    plt.savefig('images/movie_director_rating_results.jpg')
    plt.clf()

    #getting results for TV-shows by Director for rating distribution
    netflix_shows_df=data_Director[data_Director.type=='TV Show']
    count_shows = netflix_shows_df.groupby('rating')['title'].count().reset_index()
    plt.figure(figsize=(12,7))
    plt.title('Amount of TV-shows by Director vs Rating ')
    plt.xlabel("Rating")
    plt.ylabel("Amount of TV-shows")
    plt.bar(count_shows.rating, count_shows.title)
    plt.legend(['TV Shows'])
    plt.title('TV Shows Distribution for Director')
    plt.savefig('images/tvshows_Director_rating_results.jpg')
    plt.clf()


    result_year=data_Director['release_year'].value_counts(ascending=True)

    year_list=np.array(result_year.keys())
    cnt_list=np.array(result_year.values)



    plt.bar(year_list,cnt_list)
    plt.xlabel('Relase Year')
    plt.ylabel('No of releases')
    plt.title('Release Year Distribution for Director')
    plt.savefig('images/Director_release_results.jpg')

    plt.clf()


    genre_list=['Comedies','Dramas','Action','Romantic','Others']
    cnt_list=[0,0,0,0,0]

    for g in data_Director['listed_in']:
        if 'Comedies' in g:
            cnt_list[0]=cnt_list[0]+1
        elif 'Dramas' in g:
            cnt_list[1]=cnt_list[1]+1
        elif 'Action' in g:
            cnt_list[2]=cnt_list[2]+1
        elif 'Romantic' in g:
            cnt_list[3]=cnt_list[3]+1
        else:
            cnt_list[4]=cnt_list[4]+1

    plt.bar(genre_list,cnt_list)
    plt.xlabel('Genre')
    plt.ylabel('No of Releases')
    plt.title('Genre Distribution for Director')
    plt.savefig('images/Director_genre_results.jpg')
    plt.clf()


    #5 latest releases by Director
    """data_Director=data_Director.sort_values(by=['release_year'],ascending=False)
    data_latest=data_Director.head(5)
    data_latest=data_latest[['title','release_year','director']]



    data=[]
    columns = ['title','release_year','director']

    for i, j in data_latest.iterrows(): 
        curr=[]
        curr.append(j['title'])
        curr.append(str(j['release_year']))
        curr.append(j['director'])
        data.append(curr)

    plt.figure(figsize=(12,7))
    fig, axs = plt.subplots(1, 1)

    columns = ("title", "release_year", "director")
    axs.axis('tight')
    axs.axis('off')
    the_table = axs.table(cellText=data, colLabels=columns, loc='center')
    plt.savefig('/images/latest_titles_by_Director.jpg')"""
