stockDict = {'FB': 'Facebook', 'TW' : 'Twitter'}


purchases = [( 'FB', 500, '11-oct-2016', 45),
('TW', 400, '12-dec-2016', 56)]



#Create a purchase history report that computes the full purchase price (shares times dollars)
#for each block of stock and uses the stockDict to look up the full company name. This is the
#basic relational database join algorithm between two tables.
for p in purchases:

  total = p[1] * p[3]
  print(total)


  compName = stockDict[p[0]]

  print (compName)

  output = 'You bought {0} shares of {1} at ${2} for ${3}'.format(p[1], compName, p[3], total)

  print(output)




#Create a second purchase summary that which accumulates total investment by ticker symbol.

