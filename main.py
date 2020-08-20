groupName = input('whats the name of your group?: ')

NOofPupils = int(input('How many pupils are in your group?,must be between 4 to 10: '))

while NOofPupils < 4 or NOofPupils > 10:
  NOofPuils = int(input('Must be between 4 and 10: '))

pupilNames = []
TicketPrices = []
picture = []
for x in range (NOofPupils):
    pupilNames.append(input('whats the names of the pupils in your group?: ' + str(x + 1) + '?: '))
    picture = input('Do you want a picute Y/N?: ')

while picture.lower() != 'y' and picture.lower() != 'n':
  print('Please use Y for Yes or N for No')
  picture = input('Do you want a picture Y/N?: ')

if picture.lower() == 'y':
  TicketPrices.append('£4.99')
else : 
  TicketPrices.append('£3.00')
  
print('your group is called', groupName) 
print('There is', NOofPupils, 'in your group') 
print('and the cost for your prices are')
for x in range (NOofPupils):
  print(pupilNames[x], '\t', TicketPrices[x])



