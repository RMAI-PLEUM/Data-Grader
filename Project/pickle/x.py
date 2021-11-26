import pickle

a = [1,2,3,4,5,5,6,7,10,100.4524523]
b = 'try it to save'
c = 1.5
d = ['pork', 'meet', 'egg']

pickle.dump((a,b,c,d),open('stock.plk','wb'))

