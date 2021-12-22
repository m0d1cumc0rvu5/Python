#usr/bin/env python3

'''
tip calculator
'''

#declare program purpose
print('This is your friendly tip calculator to help you when you are feeling blue in the face!')
#generate user input for query then convert to float for best results
overall_price = input('What was final bill tally?\n')
overall_price = float(overall_price)
#generate user input for the amount of heads that are contributing to the bill
#then convert to float for best results...(remember to convert back to int)
total_people = input('How many people are splitting the bill?\n')
total_people = float(total_people)
#generate user input for the % of which you wish to contribute for the bill
#keep everything as float until end for ease of use
percent_to_tip = input('What % of a tip shall we leave?(exlude %)\n')
percent_to_tip = float(percent_to_tip) / 100
#now resolve how much each individual person will be spending for/by % of tip
results = overall_price * percent_to_tip / total_people
results = int(results)
#print results with any other print statement if desired
print('If you each give your waiter/waitress', results, 'they will be pleased I am sure!')




