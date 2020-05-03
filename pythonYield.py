def fun():
   yield 1
   yield 2
   yield 3


def caller():
   print ('First value printing')
   print (fun())
   print ('Second value printing')
   print (fun())
   print ('Third value printing')
   print (fun())

caller()
