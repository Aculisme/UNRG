import math, sys
from textgenrnn import textgenrnn
from pathlib import Path

################## TODO: change inputs to flags
u = bool(input("Would you like to train usernames? "))
subreddit = str(input("Choose a subreddit: "))
n_epochs = int(input("How many epochs would you like the model to train for? "))

if n_epochs<2:
    save_incr = 1
else:
    save_incr = 2

if u == True:
    input_location = 'u_inputs/u_in_'+subreddit+'.txt' # (uin_)                      fine
    model_location = 'models/u_'+subreddit+'.hdf5' # change                         fine (it'll go to uall now) 
    # search_model_location = Path("models/u"+subreddit+'.hdf5') # change          

else:
    input_location = 'inputs/in_'+subreddit+'.txt' # (in_)
    model_location = 'models/'+subreddit+'.hdf5' # change
    # search_model_location = Path("models/"+subreddit+'.hdf5') # change

search_model_location = Path(model_location)

if search_model_location.is_file():
    print("Training from existing model")
    textgen = textgenrnn(model_location)
else:
    print("Training new model")
    textgen = textgenrnn()

print("\nTraining for: ",n_epochs," epochs, and saving every ",save_incr," epochs.")

textgen.train_from_file(input_location,num_epochs=n_epochs, save_epochs=save_incr)

textgen.save(model_location)

sys.exit("\nDone. Your model has been trained and saved.")