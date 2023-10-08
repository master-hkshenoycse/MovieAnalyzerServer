import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



def get_results_display(name):
    data_netflix=pd.read_csv('data/netflix_titles.csv')
    data_amazon=pd.read_csv('data/amazon_prime_titles.csv')
    data_disney=pd.read_csv('data/disney_plus_titles.csv')


    data_netflix=data_netflix.dropna()

    plt.clf()

    data_actor=data_netflix[data_netflix['cast'].str.contains(name)]

    x_label=[1,2,3,4,5,6,7,8,9,10]
    y_cnt=[0,0,0,0,0,0,0,0,0,0]

    for r in data_actor['rating']:
        y_cnt[r-1]=y_cnt[r-1]+1



    plt.bar(x_label, y_cnt, color ='maroon',width = 0.4)
    plt.xlabel('Rating Range')
    plt.ylabel('No of Shows')
    plt.title('Rating Distribution for Actor')
    plt.savefig('images/actor_rating_results.jpg')
    plt.clf()

    result_year=data_actor['release_year'].value_counts(ascending=True)

    year_list=np.array(result_year.keys())
    cnt_list=np.array(result_year.values)



    plt.bar(year_list,cnt_list)
    plt.xlabel('Relase Year')
    plt.ylabel('No of Shows')
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
    plt.ylabel('No of Shows')
    plt.title('Genre Distribution for Actor')
    plt.savefig('images/actor_genre_results.jpg')

