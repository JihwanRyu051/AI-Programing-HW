coefficient = float(input('Enter coefficient of restitution: '))
height = float(input('Enter initial height in meters: '))
sum = 0.0
bounce = 0

while True:
    sum += height
    bounce += 1
    height *= coefficient
    if height <= 0.1:
        break
    sum += height

print('Number of bounces: {0:1}'.format(bounce))
print('Meters traveled: {0:3,.2f}'.format(sum))
