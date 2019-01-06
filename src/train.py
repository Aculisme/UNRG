import math, sys
from textgenrnn import textgenrnn
from pathlib import Path

subreddit = str(input("Choose a subreddit: "))
n_epochs = int(input("How many epochs would you like the model to train for? "))

if n_epochs<2:
    save_incr = 1
else:
    save_incr = 2

input_location = 'inputs/in_'+subreddit+'.txt'
model_location = 'models/'+subreddit+'.hdf5'

my_file = Path("models/"+subreddit+'.hdf5')
if my_file.is_file():
    textgen = textgenrnn(model_location)
else:
    textgen = textgenrnn()

print("\nTraining for: ",n_epochs," epochs, and saving every ",save_incr," epochs.")

textgen.train_from_file(input_location,num_epochs=n_epochs, save_epochs=save_incr)

textgen.save(model_location)

sys.exit("\nDone. Your model has been trained and saved.")