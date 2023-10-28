for i in range(1,101) :
    if i%7==0 :
        if i%3 !=0 :
          print('Fizz')
          continue
    if  i%3==0:
        if i%7!=0 :
          print('Buzz')
          continue
    if i%7==0 & i%3==0:
          print('FizzBuzz')
          continue
    else :
        print(i)
        