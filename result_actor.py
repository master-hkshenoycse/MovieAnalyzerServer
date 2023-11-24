import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def get_results_display(name):
    data_netflix=pd.read_csv('data/netflix_titles.csv')
    data_netflix=data_netflix.dropna()

    #clear all the previoud plots
    plt.clf()

    #subsettting the data for actor
    data_actor=data_netflix[data_netflix['cast'].str.contains(name)]

    #getting results for movies by actor for rating distribution
    netflix_movies_df=data_actor[data_actor.type=='Movie']
    count_movies = netflix_movies_df.groupby('rating')['title'].count().reset_index()
    plt.figure(figsize=(12,7))
    plt.title('Amount of Movies by Actor vs Rating ')
    plt.xlabel("Rating")
    plt.ylabel("Amount of Movies")
    plt.bar(count_movies.rating, count_movies.title)
    plt.legend(['Movies'])
    plt.title('Movie Rating Distribution for Actor')
    plt.savefig('images/movie_actor_rating_results.jpg')
    plt.clf()

    #getting results for TV-shows by actor for rating distribution
    netflix_shows_df=data_actor[data_actor.type=='TV Show']
    count_shows = netflix_shows_df.groupby('rating')['title'].count().reset_index()
    plt.figure(figsize=(12,7))
    plt.title('Amount of TV-shows by Actor vs Rating ')
    plt.xlabel("Rating")
    plt.ylabel("Amount of TV-shows")
    plt.bar(count_shows.rating, count_shows.title)
    plt.legend(['TV Shows'])
    plt.title('TV Shows Distribution for Actor')
    plt.savefig('images/tvshows_actor_rating_results.jpg')
    plt.clf()


    result_year=data_actor['release_year'].value_counts(ascending=True)

    year_list=np.array(result_year.keys())
    cnt_list=np.array(result_year.values)



    plt.bar(year_list,cnt_list)
    plt.xlabel('Relase Year')
    plt.ylabel('No of releases')
    plt.title('Release Year Distribution for Actor')
    plt.savefig('images/actor_release_results.jpg')

    plt.clf()


    genre_list=['Comedies','Dramas','Action','Romantic','Others']
    cnt_list=[0,0,0,0,0]

    for g in data_actor['listed_in']:
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
    plt.title('Genre Distribution for Actor')
    plt.savefig('images/actor_genre_results.jpg')
    plt.clf()


    #5 latest releases by actor
    data_actor=data_actor.sort_values(by=['release_year'],ascending=False)
    data_latest=data_actor.head(5)
    data_latest=data_latest[['title','release_year','director']]

    Func = open("resources/actor_recent_movies.html","w") 
    
    # Adding input data to the HTML file 

    html_str="<html><head><title>Recent relases for actor</title></head>"
    html_str+="<body>" 
    html_str+="<table><tr><th>Title</th><th>Release Year</th><th>Director</th></tr>"


                

    for i, j in data_latest.iterrows(): 
        title=j['title']
        release_year=str(j['release_year'])
        print(release_year)
        director=j['director']
        html_str+="<tr>"
        html_str+="<td>"+title+"</td>"
        html_str+="<td>"+release_year+"</td>"
        html_str+="<td>"+director+"</td>"
        html_str+="</tr>"

    html_str+="</table></body></html>"

    Func.write(html_str)
    Func.close() 

