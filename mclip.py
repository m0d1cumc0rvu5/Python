#!/usr/bin/env python3

#mclip.py - a multi-clipboard program.


#choose proper text for each clipboard slot

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  #first command line arg is the keyphrase