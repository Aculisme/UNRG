import praw, sys, progressbar, math, datetime as d
from textgenrnn import textgenrnn
from pathlib import Path

class Textgensub():
    def __init__(self,sub,u=False):
        self.r = praw.Reddit('client') 
        self.sub = str(sub)  
        self.u = bool(u)
    def gather(self,nlimit,char_limit=100):
        if self.u == True:
            f = open("inputs/u_in_"+self.sub+".txt","w")
        else:
            f = open("inputs/in_"+self.sub+".txt","w")
        
        x = 0
        bar = progressbar.ProgressBar(max_value=nlimit)
        submissions = self.r.subreddit(self.sub).hot(limit=nlimit)
        for submission in submissions:
            for top_level_comment in submission.comments:
                try:
                    if self.u == True:
                        data = top_level_comment.author.name
                    else:
                        data = top_level_comment.body
                except:
                    continue
                info = (data[:char_limit]) if (len(data) > char_limit) else data # | num_lines >= 2 
                f.write(info+"\n")
                x+=1
                bar.update(x)
                if x >= nlimit:
                    bar.finish()
                    # sys.exit("\nScraping finished.")
                    break
            if x >= nlimit:
                break

    def train(self,n_epochs):
        if n_epochs<2:
            save_incr = 1
        else:
            save_incr = 2

        if self.u == True:
            input_location = 'inputs/u_in_'+self.sub+'.txt'
            model_location = 'models/u_'+self.sub+'.hdf5'
        else:
            input_location = 'inputs/in_'+self.sub+'.txt'
            model_location = 'models/'+self.sub+'.hdf5'
        
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
        # sys.exit("\nDone. Your model has been trained and saved.")    
        print("\nDone. Your model has been trained and saved.")    

    def generate(self,nlimit,t=0.5):
        try:
            if self.u == True:
                textgen = textgenrnn('models/u_'+self.sub+'.hdf5')
            else:
                textgen = textgenrnn('models/'+self.sub+'.hdf5')
        except:
            sys.exit("\nSorry, we couldn't find "+self.sub+" in the models folder. Please try again.")

        a = d.datetime.now()
        # textgen.generate_to_file('outputs/'+sub+'.txt',n=comment_limit,max_gen_length=100) # , temperature=0.5
        if self.u == True:
            textgen.generate_to_file('outputs/u_'+self.sub+'.txt',n=nlimit,temperature=t) # , temperature=0.5
        else:
            textgen.generate_to_file('outputs/'+self.sub+'.txt',n=nlimit,temperature=t) # , temperature=0.5
        b = d.datetime.now()
        # sys.exit("\nDone. "+str(nlimit)+" comments generated in "+str(round((b-a).total_seconds(),2))+" seconds.")
        print("\nDone. "+str(nlimit)+" comments generated in "+str(round((b-a).total_seconds(),2))+" seconds.")

