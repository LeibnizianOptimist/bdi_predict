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

