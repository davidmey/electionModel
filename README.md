This is a very basic election model used to examine how overall media bias may impact the 2020 election results. 

Polls were selected from fivethirtyeight.com favoring polls with higher ratings by the website and more recent results.  
According to fivethirtyeight.com, poll bias was about 3.1 percent in favor of Donald Trump, although there is no gaurantee there will be a similar bias this time. In the past polls have also been baised towards the Democratic Candidate. For more information check out https://fivethirtyeight.com/features/the-polls-are-all-right/

The model uses binomial distributions to predict the results for each state in each simulation based on the selected poll results. 

The model always prints out the total number of victories, ties. When calculating win percentages for the plot, ties are considered a Biden victory as in the event of a tied electoral college, the House of Representatives would vote to break the tie (which would presumably go Biden's way). 

Use `python model.py` to run the model. 
Acceptable arguments are:
  -v: verbose results.
  -i: this should be followed by an integer. The model will run i simulations (Default 100).
  -p: plots the aggregate data. 
  -b: this should be followed by a float. The simulation will skew all polls by b percent in favor of Trump. For example, a value of 3.1 would skew poll results by 3.1% in favor of Trump while -5.2 would skew poll results by 5.2 in favor of Biden (Default 0). 
