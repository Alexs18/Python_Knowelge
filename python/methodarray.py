# we can concat 1 array with a new values or her same value
from re import sub


movies = ['Avenger', 'the end', 'spiderman', '2012']
print(movies)

newmovies = ['the old man', 'summer', 'holidate']
print(newmovies)
newmovies = newmovies+ movies
print(newmovies)

#we can duplicate the value from an array with the instruction *

restaurantlist = ['fist', 'meet', 'pig']
restaurantlist = restaurantlist * 5

print(restaurantlist)

subjects = ['matematicas', 'fisica', 'quimica', 'anatomia', 'filosofia']

print(subjects[1:4])
print(subjects[1:3])
print(subjects[2:4])
print(subjects[:-1])
print(subjects[-2:])


#we can use a matrix inside the python element

matrix = [[1,2], [4,45]]
print(matrix[1][0])
