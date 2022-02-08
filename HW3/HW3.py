import pandas as pd
import numpy as np
#Создаем датафреймы из наших файлов
df_books = pd.read_csv('books.csv')
df_users = pd.read_json('users.json')
#Создаем на основе датафрейма с книгами наш датафрейм с нужными столбцами
df_new_books = df_books[['Title','Author','Pages','Genre']]
#Переводим оглавление в нижний регистр
df_new_books.columns = df_new_books.columns.str.lower()
#Создаем на основе датафрейма с читателями наш датафрейм с нужными столбцами
df_new_users = df_users[['name','gender','address','age']]
#Делаем словарь из нашего датафрейма с книгами
books = df_new_books.to_dict('records')
#Разбиваем книги
books_split = np.array_split(books,len(df_new_users))
#Создаем новую коллонку в датафрейме с перечнем книг
df_new_users['books'] = books_split
#Выводим результат в файл с нужным форматированием
with open('result_hw3.json', 'w') as f:
    f.write(df_new_users.to_json(orient='records', lines=True, indent=3))