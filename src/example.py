from main import Textgensub

a = Textgensub('all',u=True)
a.gather(150,char_limit=20)
a.train(1)
# a.generate(100)