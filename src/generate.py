from textgenrnn import textgenrnn
import sys, datetime as d

u = bool(input("Would you like to generate usernames? "))
subreddit = str(input("Choose a subreddit: "))
comment_limit = int(input("How many strings should it generate? "))
# temperature = int(input("At what Temperature (0.2-1)? "))

try:
    if u == True:
        textgen = textgenrnn('models/u_'+subreddit+'.hdf5')
    else:
        textgen = textgenrnn('models/'+subreddit+'.hdf5')
except:
    sys.exit("\nSorry, we couldn't find "+subreddit+" in the models folder. Please try again.")

a = d.datetime.now()
# textgen.generate_to_file('outputs/'+subreddit+'.txt',n=comment_limit,max_gen_length=100) # , temperature=0.5
if u == True:
    textgen.generate_to_file('outputs/u_'+subreddit+'.txt',n=comment_limit) # , temperature=0.5
else:
    textgen.generate_to_file('outputs/'+subreddit+'.txt',n=comment_limit) # , temperature=0.5
b = d.datetime.now()
sys.exit("\nDone. "+str(comment_limit)+" comments generated in "+str(round((b-a).total_seconds(),2))+" seconds.")
