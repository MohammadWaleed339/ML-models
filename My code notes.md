   **Pandas : Renaming and Combining**
To rename a column from points to score use :
     reviews.rename(columns={'points': 'score'})
To rename an index value (index 0 becomes firstEntry) :
     reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
You can give names to your rows and columns like this :
     reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
In order to study different data sometimes we smush them together this done via join() or concat() method like :
     canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
     british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

     pd.concat([canadian_youtube, british_youtube])
Join() is a bit complex, it lets you join to data set which have an index common e.g.,
     left = canadian_youtube.set_index(['title', 'trending_date'])  
     right = british_youtube.set_index(['title', 'trending_date'])
 
     left.join(right, lsuffix='_CAN', rsuffix='_UK') 
here it joins the song trending on same data at UK and Canada.