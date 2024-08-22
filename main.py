print('[*] Prime Number Utility')

running = True

while running:
  print('\n[1] Determine if a number is prime')
  print('[2] Determine all prime numbers within a set range')
  option = input('[?] Enter your choice: ')  

  if option == '1':
    number = int(input('\n[*] Enter number: '))
    prime_status = True
    for i in range(2, number):
      print(i)
      if number % i == 0:
        prime_status = False
        break
      if prime_status:
        print(str(number) + ' is a prime number')
      else:
        print(str(number) + ' is not a prime number')