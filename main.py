print('[*] Prime Number Utility')

running = True

while running:
  print('\n[1] Determine if number is prime')
  print('[2] Determine all prime number within a set range')
  option = input('[?]Enter your choice: ')  
  print(option)

  if option == '1':
    number = int(input('\n[*] Enter number: '))
    prime_status = True
    for i in range(0, number):
      if number % i == 0:
        prime_status = False