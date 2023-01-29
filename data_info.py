#Analisis del dataset y generacion de preguntas.
import numpy as np
import pandas as pd


#Create a Pandas dataframe from dataset
def population_to_Pandas():
    #Dataset: World Population (wp) / Game: How much you known about the global population?
    wp_world_population = pd.read_csv('datasets/world_population.csv')
    #Create dataframe
    df_wp = pd.DataFrame(wp_world_population)
    
    return df_wp


#The function that choice info for play
def options(dataframe):
    chosen = []
    #Using sample method (Pandas) for select options
    #random_sample = 0
    #random_sample = dataframe.sample(n = 4, replace = False)

    #Using random.choice method (Numpy) for select options
    chosen = np.random.choice(len(dataframe),replace = False, size = 4)
    random_sample = dataframe.iloc[chosen]
    
    return random_sample

#Create dict to show options to play
def select_data():
    data_full_wp = population_to_Pandas()
    opt_filter = options(data_full_wp).set_index('Country').to_dict()['2022 Population']
    
    return opt_filter

#Evaluate to answer questions
def evaluate(dictionary):
    max_popu = max(dictionary, key=dictionary.get)

    return max_popu
