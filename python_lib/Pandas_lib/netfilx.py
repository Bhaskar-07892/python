import pandas as pd 

netflix_df = pd.read_csv(
    r"C:\Users\op_Bh\code_base\data_science\mymoviedb.csv",
    engine='python',           # Python parser इस्तेमाल करें
    on_bad_lines='skip'        # जो लाइनें खराब हैं, उन्हें स्किप कर दें
)


# remove column ()
exit_column = netflix_df.drop( [ 'Poster_Url' , 'Overview' ] , axis = 1 , inplace = True )

# head ()
head = netflix_df.head()
print ( " Head Function : \n " , head )

# tail ()
tail = netflix_df.tail ()
print ( " Tail Function : \n" , tail )

Datatype = netflix_df.dtypes 
print ( " Data type : \n" , Datatype )

# describe ()
statics = netflix_df.describe ()
print ( " All Stats : describe Function : \n" , statics )

# iloc ()
iloc_func = netflix_df.iloc [24:39]
print ( " iloc : \n" , iloc_func )

#similer iloc ()
s_iloc = netflix_df [20 : 35]
print ( " Similer of iloc : \n" , s_iloc )

# Title with above 8 Vote_Average
# title_with_ratings  = netflix_df [ [ 'Title' , 'Vote_Average' ] ]
title_with_ratings = netflix_df [ netflix_df [ 'Vote_Average'] >= 8.0 ] [ ['Title' , 'Vote_Average'] ] 
print ( " Movies With their rating \n" , title_with_ratings  )

# Add column in a last 
netflix_df ['last_col'] = 'none'
print ( 'Add column in last for temprary \n' , netflix_df )

# Add column in a specific index for movie ratings and given category
def ratings (Vote_Average) : 
pass

df_with_new_column = netflix_df.insert ( )