#We can create a simple arreglo like this
arreglo = [10,20,30,40,50]
print(arreglo)

#we can access to a especific element with the index, for example
#we can use positive index and negative index

# positive index
print(arreglo[1], arreglo[2])
#output will be 20 and 30

#negative index
print(arreglo[-1], arreglo[-2])
#output will be 50 and 40

#we can know the specific length using len
lengtharreglo = len(arreglo)
print(lengtharreglo)
#we can use the value to make many things but we'll do after
#we can add new element to this array
#for this form we can add a new element but we'll need mute the original array
newArreglo = arreglo.append(100)
print('old array {}, new array {}' .format(arreglo, newArreglo))
#output will be original array and none because the method append don't return anything

#we can delete element from our array we can use del, pop and remove
#considere that our array it will see like this

#[10,20,30,40,50,100]
#we goint to delete 30, 50, and 100

#first the all the number 100 using the remove
print(arreglo)
arreglo.remove(100)
print(arreglo)

#the second we gonna delete 30 using her position
print(arreglo)
del arreglo[2]
print(arreglo)

#the last method will be pop, in this case we are gonna do the next 
#using the method pop and we need her index
print(arreglo)
arreglo.pop(-1)
print(arreglo)


#we can modify the element inside a siple array with her position or index

fruta = ['piña', 'uva', 'manzana', 'zapallo']

print(fruta[1])

fruta[1] = 'sandia'
print(fruta[1])
print(fruta)