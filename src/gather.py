import praw, sys, progressbar
subreddit = str(input("Choose a subreddit: "))
comment_limit = int(input("How many comments should it scrape? "))
# char_limit = int(input("What should the character limit for comments be? "))

r = praw.Reddit('client') 
submissions = r.subreddit(subreddit).hot(limit=comment_limit)

f = open("inputs/in_"+subreddit+".txt","w")

x = 0

bar = progressbar.ProgressBar(max_value=comment_limit)

for submission in submissions:
	for top_level_comment in submission.comments:
		try:
			data = top_level_comment.body
		except:
			continue
		info = (data[:100]) if (len(data) > 100) else data # | num_lines >= 2 
		f.write(info+"\n")
		x+=1
		bar.update(x)
		if x>=comment_limit:
			bar.finish()
			sys.exit("\nScraping finished.")
		
