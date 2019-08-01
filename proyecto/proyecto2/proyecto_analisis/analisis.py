import numpy as np
import pandas as pd
import os
import re

## LLamado al csv 
path = './tmp/database_peliculas.csv'
toprevenue = 's'
data = pd.read_csv(path)

def correct_price(text):
  if text=="-" or text=="NR":
    return 0
  number = float(text)
  return number

def parse_duration_to_minutes(text):
  text=f"{text}".replace(" ","")
  if text=="-" or text=="NR":
    return 0
  parts = text.split("h")
  parts[0] = re.sub(r"[hm]", "", parts[0])
  parts[1] = re.sub(r"[hm]", "", parts[1])
  total_duration=(float(parts[0])*60)+float(parts[1])
  return total_duration

def split_values(text):
  array=f"{text}"
  array = array.split("/")
  return np.array(array)

def comparator_arrays(array, value):
  print(value)
  if value in array:
    return 1
  else:
    return None

def get_path_csv(key,extra=""):
    return f"../csv/{key}_{extra}.csv"

class cnames:
    actors = "actors"
    budget = "budget"
    directors = "directors"
    genres = "genres"
    language = "language"
    name = "name"
    overview = "overview"
    releases_dates = "releases_dates"
    releases_formats = "releases_formats"
    revenue = "revenue"
    runtime = "runtime"
    url = "url"
    user_score = "user_score"
    writing = "writing"

## Correccion de datos
data[cnames.revenue] = data[cnames.revenue].map(correct_price)
data[cnames.budget] = data[cnames.budget].map(correct_price)
data[cnames.user_score] = data[cnames.user_score].map(correct_price)
data[cnames.budget] = data[cnames.budget].map(correct_price)
data[cnames.actors] = data[cnames.actors].map(split_values)
data[cnames.genres] = data[cnames.genres].map(split_values)
data[cnames.writing] = data[cnames.writing].map(split_values)
data[cnames.directors] = data[cnames.directors].map(split_values)
data[cnames.language] = data[cnames.language].map(split_values)
data[cnames.runtime] = data[cnames.runtime].map(parse_duration_to_minutes)

## collectores
def collect_data(values):
  all_values = np.array([])
  for value in values:
    all_values = np.append(all_values, value)
  all_values = np.unique(all_values)
  all_values = all_values[all_values!="nan"]
  return all_values

all_genres = collect_data(data[cnames.genres].values)
all_actors = collect_data(data[cnames.actors].values)
all_directors = collect_data(data[cnames.directors].values)
all_writing = collect_data(data[cnames.writing].values)
all_languages = collect_data(data[cnames.language].values)

## ==================================== Top Order Only ====================================

def get_top(field_name, ascending=False, number_10=True):
  top_by_value = data[field_name]
  top_by_value.index=data[cnames.name]
  top_by_value = top_by_value[top_by_value> 0]
  if number_10:
    return pd.Series.sort_values(top_by_value, ascending=ascending).head(10)
  else:
    return pd.Series.sort_values(top_by_value, ascending=ascending)

## top reveue
top_revenue = get_top(cnames.revenue, False)
top_revenue.to_csv(get_path_csv(cnames.revenue, "top"))
top_revenue_low = get_top(cnames.revenue, True)
top_revenue_low.to_csv(get_path_csv(cnames.revenue, "low"))
print('top_revenue: ', top_revenue)
print('top_revenue_low: ', top_revenue_low)
## top budget
top_budget = get_top(cnames.budget, False)
top_budget.to_csv(get_path_csv(cnames.budget, "top"))
top_budget_low = get_top(cnames.budget, True)
top_budget_low.to_csv(get_path_csv(cnames.budget, "low"))
print('top_budget: ', top_budget)
print('top_budget_low: ', top_budget_low)
## top rating
top_rating = get_top(cnames.user_score, False)
top_rating.to_csv(get_path_csv(cnames.user_score, "top"))
top_rating_low = get_top(cnames.user_score, True)
top_rating_low.to_csv(get_path_csv(cnames.user_score, "low"))
print('top_rating: ', top_rating)
print('top_rating_low: ', top_rating_low)
## top runtime
top_runtime = get_top(cnames.runtime, False)
top_runtime.to_csv(get_path_csv(cnames.runtime, "top"))
top_runtime_low = get_top(cnames.runtime, True)
top_runtime_low.to_csv(get_path_csv(cnames.runtime, "low"))
print('top_runtime: ', top_runtime)
print('top_runtime_low: ', top_runtime_low)

## ==================================== Top based on list ====================================

def top_by_array(all_values, column, ascending=False, number_10=True):
  top_values = pd.Series(np.zeros(len(all_values)), index=all_values)
  top_data = data[column]
  top_data.index = data[cnames.name]
  for genre in top_values.index:
    filtered_data = top_data.map(lambda x: comparator_arrays(x, genre)).dropna()
    top_values[genre]=len(filtered_data)
  return_data = pd.Series.sort_values(top_values, ascending=ascending)
  if number_10:
    return return_data.head(10)
  else:
    return return_data

## top genres
top_genres = top_by_array(all_genres, cnames.genres, False, True)
top_genres.to_csv(get_path_csv(cnames.genres, "top"))
top_genres_low = top_by_array(all_genres, cnames.genres, True, True)
top_genres_low.to_csv(get_path_csv(cnames.genres, "low"))
print('top_genres: ', top_genres)
print('top_genres_low: ', top_genres_low)
## top actors
all_top_actors = top_by_array(all_actors, cnames.actors, False, False)
top_actors = pd.Series.sort_values(all_top_actors, ascending=False).head(10)
top_actors.to_csv(get_path_csv(cnames.actors, "top"))
top_actors_low = pd.Series.sort_values(all_top_actors, ascending=True).head(10)
top_actors_low.to_csv(get_path_csv(cnames.actors, "low"))
print('top_actors: ', top_actors)
print('top_actors_low: ', top_actors_low)
## top directors
all_top_directors = top_by_array(all_directors, cnames.directors, False, False)
top_directors = pd.Series.sort_values(all_top_directors, ascending=False).head(10)
top_directors.to_csv(get_path_csv(cnames.directors, "top"))
top_directors_low = pd.Series.sort_values(all_top_directors, ascending=True).head(10)
top_directors_low.to_csv(get_path_csv(cnames.directors, "low"))
print('top_directors: ', top_directors)
print('top_directors_low: ', top_directors_low)
## top writers
all_top_writing = top_by_array(all_writing, cnames.writing, False, False)
top_writers = pd.Series.sort_values(all_top_writing, ascending=False).head(10)
top_writers.to_csv(get_path_csv(cnames.writing, "top"))
top_writers_low = pd.Series.sort_values(all_top_writing, ascending=True).head(10)
top_writers_low.to_csv(get_path_csv(cnames.writing, "low"))
print('top_writers: ', top_writers)
print('top_writers_low: ', top_writers_low)
# percentage genres
percentage_genres = top_by_array(all_genres, cnames.genres, True, False)
percentage_genres.to_csv(get_path_csv(cnames.genres, "percentage"))
print('percentage_genres: ', percentage_genres)
## top writers
top_languages = top_by_array(all_languages, cnames.language, False, True)
top_languages_low = top_by_array(all_languages, cnames.language, True, True)
top_languages.to_csv(get_path_csv(cnames.language, "top"))
top_languages_low.to_csv(get_path_csv(cnames.language, "low"))
print('top_languages: ', top_languages)
print('top_languages_low: ', top_languages_low)

## ==================================== Averages arrays ====================================

def get_max_min_avg(serie):
  value_serie = pd.Series({
      "MAX": serie.max(),
      "AVG": serie.mean(),
      "MIN": serie.min()
  })
  return value_serie

average_rating = get_max_min_avg(top_by_array(all_languages, cnames.language, True, False))
average_rating.to_csv(get_path_csv(cnames.user_score, "average"))
print('average_rating: ', average_rating)
average_genres = get_max_min_avg(top_by_array(all_genres, cnames.genres, True, False))
average_genres.to_csv(get_path_csv(cnames.genres, "average"))
print('average_genres: ', average_genres)
average_runtime = get_max_min_avg(get_top(cnames.runtime, True, False))
average_runtime.to_csv(get_path_csv(cnames.runtime, "average"))
print('average_runtime: ', average_runtime)
average_budget = get_max_min_avg(get_top(cnames.budget, True, False))
average_budget.to_csv(get_path_csv(cnames.budget, "average"))
print('average_budget: ', average_budget)
average_revenue = get_max_min_avg(get_top(cnames.revenue, True, False))
average_revenue.to_csv(get_path_csv(cnames.revenue, "average"))
print('average_revenue: ', average_revenue)
average_rating = get_max_min_avg(get_top(cnames.user_score, True, False))
average_rating.to_csv(get_path_csv(cnames.user_score, "average"))
print('average_rating: ', average_rating)
average_writers = get_max_min_avg(top_by_array(all_writing, cnames.writing, True, False))
average_writers.to_csv(get_path_csv(cnames.writing, "average"))
print('average_writers: ', average_writers)
average_directors = get_max_min_avg(top_by_array(all_directors, cnames.directors, True, False))
average_directors.to_csv(get_path_csv(cnames.directors, "average"))
print('average_directors: ', average_directors)
average_actors = get_max_min_avg(all_top_actors)
average_actors.to_csv(get_path_csv(cnames.actors, "average"))
print('average_directors: ', average_directors)