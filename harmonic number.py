#hn=float(input('Harmonic number is'))
#n=int(input('n is'))

#calc = hn + (1/(n+1))

#print (calc)
         
#Using loop to print harmonic numbers up to the 'n'th harmonic number
harmonicNumber = 1 #The first harmonic number starts at 1
n = 1 #'n' starts at 1 to caculate the next harmonic number (see below)

while n < 10: #How many times to do the loop (do it until you get to harmonicNumber + (1/10)
    print (harmonicNumber)
    harmonicNumber = harmonicNumber + (1/(n+1)) #Next harmonicNumber = previous harmonicNumber plus (1/the next 'n' value)
    n = n + 1 #increments n by 1 until n reaches 10 and cause the loop to close
    
