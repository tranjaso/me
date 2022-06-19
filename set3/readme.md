TODO: Reflect on what you learned this week and what is still unclear.
wth, for the loop_ranger stop was literally stop!!! 
7:07 PM 18/6: Continued on exercise1 and finished, saved and pushed to Github. We use a while loop for the boolean "True" so that the program will continuously ask for a number (since the boolean is set to False if not between low and high) until between the ranges.

For exercise 3, I can only improve on these 1 of these failure modes (cant think of anything else).

1. When the lowerbound is equal to the upperbound, we obviously know that the number will be either the lowerbound and the upperbound. Hence, a error saying "Wow, how'd you guess that" or something should occur and the program should exit instead of letting the user continue with the guess.

Dataset homework:
https://openpowerlifting.gitlab.io/opl-csv/bulk-csv.html <-- Powerlifting
Question: The purpose of people testing their limit and why they find the challenge enjoyable and satisfying.

Data Audit -
By having a look at the dataset I can see that there are reducntant types of Data, e.g; a minority of powerlifters were able to do a 4th set of bench/deadlift, some attributes of data were empty.

There are 41 rows and 1,048,576 columns in total (big woop). 
This dataset gives us data on each individual professional powerlifter, it provides detail on the maximum, average and where each powerlifter comes from.
As it is a competition, it is collected in order in order to show the integrity of the results not only for powerlifters, but fans and judges alike.
The data is open-source and is collectively updated by a community of powerlifter fanatics!
How did I get it?: I did a neat little trick by going on this website https://www.openpowerlifting.org/, right click -> inspect element and CTRL + F '.csv'. I was then redirected to the dataset itself which I was able to download!
Does it have a geographical component?: Yes! It has the country, Federation, State, MeetState, MeetCountry and MeetTown
Column in dataset: Too many but I'll try explain if needed :'(

We know that [name, sex, event, equipment, state, ag... etc] is categorial and [age, ageclass, place, bodyweight, squat, bench, deadlift] are continuous data. 
