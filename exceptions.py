def main():
  import math

  trig = input('Struggling? I can help! \n\n Calculate: \n (1) sine \n (2) cosine \n (3) tangent \n\n **Please enter a designated numeric choice**\n :')

  if trig == '1':
    s = eval(input('What is the degree of the angle? \n'))
  result = math.sin(math.radians(s))
  print('The answer is' +str(round(result,3)))
  main()

  if trig == '2':
	  c = eval(input('What is the degree of the angle? \n'))
  result = math.cos(math.radians(c))
  print('The answer is' +str(round(result,3)))
  main()

  if trig == '3':
  	t = eval(input('What is the degree of the angle? \n'))
  result = math.tan(math.radians(t))
  print('The answer is \n\n' +str(round(result,3)))
  main()

  else: 
    print ('error')

main()

