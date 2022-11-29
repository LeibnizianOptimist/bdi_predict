# DEMO DAY SCRIPT


## What we wanted to do:

- Our central aim is was to create, within two weeks, a half-decent model to predict the Baltic Dry Index that woudl then be deployed on google cloud run instance  where the model would be intractable using FastAPI. 

## Explaining what the BDI is & what we were trying to solve: 

- The Baltic Dry index (henceforth the BDI) is an index whose value represents the aggregate of 3 prices of three freight future timecharter contracts each contract being reserved for s specific standard class of dry bulk freighter. 

- The BDI's value flucations are devoid of speculative content because dry bulk freighters are only booked by individuals who possess cargo to move, such as iron ore or coal mining corporations. Hence the majority of the movement in its value can be attributed to the supply and demand of important raw resources and base materials used in manufacturing.

## Why predict the BDI?

1. BDI is used by economists as a leading economic indicator - its value markedly increases prior to recessions (e.g. mid-2007 to late 2008, mid-2021 to now...) Helpful auxiliary tool for economist to aid their assessment of macroeconomic conditions.
2. Aid shipbrokers and businesses dealing in dry bulk cargo to try and purchase freight futures at optimal price points to minimize loss on bad freight contracts. Hence our developement of an interactable API hosted on google cloud. 
3. Attempting to predict the value of the BDI would be an entertaining and challenging intellectual exercise where we could apply what we've learnt over the past few months and to further expand and cement our understanding of these concepts. 


## What we did:

- We wanted to predict the value of the index one week in advance because given our research, certain papers (Bae et al 2021, p.21) cited that a period exceeding at least one week must be forecasted in consideration of freight rate liquidity in the shipping market and further be useful for any stakeholder within the shipping industry.


- First we attempted creating a univariete model LSTM Recurrent Neural Network that attempted to predict abosute values, but with no success, as it was not able to enough to beat the baseline score of 140 (MAE).  

- Next, we shifted our target from being an absolute value to attempting to predict the log-difference between BDI values over the absolute value or the growth rate of the BDI per week. This was because compared to growth rates there was symmetry in the increse of decrease of the difference.

- Feature selection was difficult: much of the freautre data cited was dispered across the internet, given by multiple sources, and much that was useful was proprietary and would be expensive given the current scope of the project. 

-  

## !DEMO OF THE API! 

## What we would’ve done differently/What we will continue to do in the future:

- Convert regression task into a classification task identifying inherent behavioural states of the index - defined by our own domain knowledge of the index and how it would operate.

- Obtain obscure proprietary data used as features within academic papers - getting better model performance seems to require this!  


DEMO DAY SCRIPT
What we wanted to do:

Our central aim was to create, within two weeks, a decent model that predicted values of the Baltic Dry Index.

As an intractable product, our team thought in the timeframe we could develop a service that ran on a Google Cloud Run instance with FastAPI, with a frontend built using Streamlit.
What is the BDI?
The Baltic Dry index (henceforth the BDI) is an index whose value represents the aggregate of the prices of three freight future time-charter contracts where each contract relates to a specific defined class of dry bulk freighter.

For context, the BDI's value fluctuations are devoid of speculative content because dry bulk freighters are only booked by individuals who possess cargo to move, such as iron ore or coal mining corporations. Thus the majority of the movement in its value can be attributed to the supply and demand of important raw resources and base materials used in manufacturing.
Why predict the BDI?

BDI is used by economists as a leading economic indicator - its value markedly increases prior to recessions (e.g. mid-2007 to late 2008, mid-2021 to now...) It is a helpful auxiliary tool for economists to aid their assessment of macroeconomic conditions.

A prediction model would also help stakeholders in the shipping industry to try and predict when the best time would be for them to minimise avoidable losses. 

Attempting to predict the value of the BDI would be an entertaining, challenging and novel intellectual exercise that requires us to further expand and cement our understanding of some of the most difficult concepts we learnt during the bootcamp.
What we did:
THE STRUGGLE:
The first model we attempted creating was a univariate LSTM Recurrent Neural Network that attempted to predict absolute values.
We began with this model framework to emulate the approach certain academic papers had taken to predicting the BDI. 
However, this model yielded no success, and was not even able to beat our baseline score. Even when we then attempted a multivariate LSTM RNN predicting absolute values, we still could not get good model performance.
This was likely due to a host of reasons: the difficulty in predicting absolute values, the model was underfitting due to inadequate data, and the data we had obtained was not sufficient. 
Feature selection and data sourcing was also difficult. Much of the feature data that was referenced in academic papers was dispersed across the internet, given by multiple sources, and much that was useful was proprietary and would be expensive to obtain given the scope of our project. 
We knew this challenge even before starting and thus resolved to find proxies for some of the data we could not obtain. Given the scope of the project we were not ready to shill out lots of money. 
THE TRIUMPH:

However, fortunately, we began to achieve great results once we made the decision to shift the model’s target from being the absolute value of the BDI to being the log-difference between daily BDI values.

We predicted log difference per day instead of growth rate per day due to the lack of symmetry in the decrease and increase of growth rates. 

We also engaged in diligent data sourcing to obtain veritable feature data, based on our domain knowledge.

Our process was:
(1) find indexes and data related to global economic performance, indexes and price data of Dry bulk products transported by ships in the BDI, and proxies for global trade situations. 
(2) apply statistical analyses to ascertain which of these could be useful before using it as a feature in our model. 
(3) attempt it without our model. 

After feature ablation and greater hyperparameter tuning, we were able to create a very good model that confidently beat the baseline score.

Given this we created a basic API and frontend that would represent a minimum viable product that could be served in-house to other coworkers in accompany where this data would be useful, or for a client Here is the demo of our model and front in action: 

DEMO OF THE API & FRONTEND
What we would’ve done differently & What we will continue to do in the future with this project:

Given the development of the project so far, we have several clear ideas of what we should do next, and what we should've done previously if we were to start again.

(1) Convert a regression task into a classification task identifying inherent behavioural states of the index - defined by our own domain knowledge of the index and how it would operate.

(2) Obtain obscure proprietary data used as features within academic papers - getting better model performance seems to require this.

(3) Predict a week in advance instead! More useful for the clients involved! Certain papers (Bae et al 2021, p.21) cited that a period exceeding at least one week must be forecasted in consideration of freight rate liquidity in the shipping. 

Develop frontend much more - do not just display the prediction value, but also display what the model predicted previously (what Nazir recommended we do this morning). 



