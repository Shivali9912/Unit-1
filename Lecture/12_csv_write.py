import csv
# Python: CSV write

car = [
    ('Make', {'Toyota', 'Ford'}),
    ('Model', {'Rav4','F150'}),
    ('Max speed', {220,190}),
    ('Power', {195, 320})
]

for r in car:
    print(r)

with open("Cars.csv", 'w', newline="" ) as f:
     writer = csv.writer (f)
     writer.writerow([r[0] for r in car])
     writer.writerow([r[1] for r in car])