from die import Die

#Creat a D6
d = Die()

#Make some roll and store result in list.
results = []

for result in range(100):
    result = d.roll()
    results.append(result)

print(results)