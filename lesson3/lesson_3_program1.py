"""
    udacity fsnd 
    lesson3 program
    open up a random music file at 2 hours interval
"""



list_music = """https://www.youtube.com/watch?v=K4DyBUG242c/
https://www.youtube.com/watch?v=zyXmsVwZqX4/
https://www.youtube.com/watch?v=3nQNiWdeH2Q/
https://www.youtube.com/watch?v=UlVcER-RQCo/
https://www.youtube.com/watch?v=-yOZEiHLuVU/
https://www.youtube.com/watch?v=2sUupgjZ58E/
https://www.youtube.com/watch?v=eyLml-zzXzw/
https://www.youtube.com/watch?v=blA7epJJaR4/
https://www.youtube.com/watch?v=1KqQQHpQc8w
""" 

import webbrowser
import random
import time 

total_break = 3

for i in range(total_break):
    
    time.sleep(2*60*60)
    url = list_music.split("\n")[random.randint(0, len(list_music.split("\n") - 1))]
    print(url)
    webbrowser.open_new_tab(url + 'doc/');
    time.sleep(250) 


