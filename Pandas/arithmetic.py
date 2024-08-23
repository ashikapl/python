# Arithmetic Operation 
import pandas as pd

var = pd.DataFrame({'A':[11,12,13,14,15],'B':[10,20,30,40,50]})

print(var)
print('\n')

# addition , subtraction, division, multiplication
var['Add'] = var['A'] + var['B']
print(var)
print('\n')
var['Sub'] = var['A'] - var['B']
var['Multi'] = var['A'] / var['B']
var['Div']= var['A'] * var['B']
print(var)
print('\n')


var1 = pd.DataFrame({'A':[13,12,5,33,65],'B':[13,5,6,7,4]})
print(var1)
print('\n')

var1['logic'] = var1['A'] <= 13
print(var1)
print('\n')

var1['logic_1'] = var1['B'] >= 4
print(var1)

