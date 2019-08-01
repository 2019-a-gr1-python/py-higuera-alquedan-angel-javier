import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

## LLamado al csv 
def correct_price(text):
  if text=="-" or text=="NR":
    return 0
  number = float(text)
  return number

def get_path_csv(key,extra=""):
    return f"csv/{key}_{extra}.csv"

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

def read_csv(key, extra):
  path=get_path_csv(key,extra)
  df = pd.read_csv(path, header=None)
  serie = df[1]
  serie.index = df[0]
  return serie

top_revenue = read_csv(cnames.revenue, "top")
top_revenue_low = read_csv(cnames.revenue, "low")
top_budget = read_csv(cnames.budget, "top")
top_budget_low = read_csv(cnames.budget, "low")
top_rating = read_csv(cnames.user_score, "top")
top_rating_low = read_csv(cnames.user_score, "low")
top_runtime = read_csv(cnames.runtime, "top")
top_runtime_low = read_csv(cnames.runtime, "low")
top_genres = read_csv(cnames.genres, "top")
top_genres_low = read_csv(cnames.genres, "low")
top_actors = read_csv(cnames.actors, "top")
top_actors_low = read_csv(cnames.actors, "low")
top_directors = read_csv(cnames.directors, "top")
top_directors_low = read_csv(cnames.directors, "low")
top_writers = read_csv(cnames.writing, "top")
top_writers_low = read_csv(cnames.writing, "low")
top_languages = read_csv(cnames.language, "top")
top_languages_low = read_csv(cnames.language, "low")
percentage_genres = read_csv(cnames.genres, "percentage")
average_rating = read_csv(cnames.user_score, "average")
average_genres = read_csv(cnames.genres, "average")
average_writers = read_csv(cnames.writing, "average")
average_directors = read_csv(cnames.directors, "average")
average_runtime = read_csv(cnames.runtime, "average")
average_budget = read_csv(cnames.budget, "average")
average_revenue = read_csv(cnames.revenue, "average")
average_rating = read_csv(cnames.user_score, "average")