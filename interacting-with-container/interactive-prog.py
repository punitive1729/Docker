from random import randint

# Interact with container to provide some input
# docker run -i -t imageId -> -i means interactive mode setup for container and -t creates pseudo terminal


max_number = int(input('input max number...'))
min_number = int(input('input min number...'))

if (max_number < min_number):
    print('Invalid input..')
else:
    random_no = randint(min_number, max_number)
    print('Printing random number', random_no)
