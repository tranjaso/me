TODO: Reflect on what you learned this week and what is still unclear.
wth, for the loop_ranger stop was literally stop!!! 
7:07 PM 18/6: Continued on exercise1 and finished, saved and pushed to Github. We use a while loop for the boolean "True" so that the program will continuously ask for a number (since the boolean is set to False if not between low and high) until between the ranges.

For exercise 3, I can only improve on these 1 of these failure modes (cant think of anything else).

1. When the lowerbound is equal to the upperbound, we obviously know that the number will be either the lowerbound and the upperbound. Hence, a error saying "Wow, how'd you guess that" or something should occur and the program should exit instead of letting the user continue with the guess.

![Exercise 4 Diagram:](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R5VlLc9s2EP4tOWimPajDt6yjZTtxp69MfWh7ysAkRKICAQYE9civ74IAJL6kUWoznCQHDYnF4vXtfrtLaObf5ft3AhXZbzzBdOY5yX7m3888zw1DBx5KctCSG2epBakgiVE6CZ7IJ2yEZlxakQSXLUXJOZWkaAtjzhiOZUuGhOC7ttqa0%2FaqBUpxT%2FAUI9qX%2FkUSmZlTeIuT%2FBGTNLMru5E5X46ssjlJmaGE7xoi%2F2Hm3wnOpX7L93eYKvAsLnrc2zO9x40JzOQ1A27%2F%2BDnY%2FL7afPpFfGCFePw43zzOfXOOUh7siXECAJgmFzLjKWeIPpykK8ErlmA1rQOtk86vnBcgdEH4L5byYKyJKslBlMmcml69plro7FmMqOSViPGFA1ifQCLF8pKee4QcfBXzHEtxgIECUyTJtr0RZJwmPeqdcIUXA%2B3nwHzzvcDsTAlz8E148wvQM0PfcwIre46JwgvHhCATg72l055Cm9WM6tjguI3%2Fbxaz4S2ilTnCE6wo6%2BiOy1KFZcFzFTNJkoBNrOpRTiFues4cfhmE2p6NTxZU5thlROKnAtVA7yArDVlri4XE%2B8v26tvBDli08XRtstqdMoRnE1%2FWzA6%2Bc952L%2FN8t4fKF%2FB8wEsc%2Fjbj68Y%2FqvHTIrTt%2B32z9%2F5gWq9JGefK0BRMGprsNhsk%2BBPnfHv0dkUDiteKFSWUPPDga02JmQdLOlVZy6B8MUK1R0MN1Y%2BYksUCI1nPheDH8O6obSh1ljrOuNQxVPHDAaoEQ1TxRqOKNylV3Ampcm0Wn5gq%2FXwx8yIKG16VBWIt00UfK1U%2Fr1pvqXr22SVq7xqXXnqbcGy9U72V6Vi37yT8SyyMvigL3aBnZBTLCtEPrMqfsZiplSOUKzAMphrpDpQAimzjVUrBN%2FiOUy5AwjhT%2FF0TSjsiREnKoBkDiLCev1IQE%2FjyuzUdphoZNlDbhK9go7BjIq9vItcZMNFoJYUfDdDw666uwyvj37Qfi3abnxP%2FYu3bt2qT6fMPjg5a9vGj5s%2BaMzlfo5zQg1Z9xHSLlc83%2BsvaEKrX9Yp9s0MvqnoYFzmijb4tEgTBE5iDZCXUhc1FvRgV51R2xrdVZ%2BBockFhJIGjczh%2BTFjaH8lFkSFmpvS0TEWGuSG5Eh95bvsIOCYzKzn2qHWPFDDZGua3K9UBQ5OxvlFqLLPjImlv7DgXnOV5Q2A6NacOS3ND55beM4o3aU2UeceOXnCjTegFS%2FMSWmvWsyY45gJ8krO5zEi8Yep7qh5OGJHE4tPVbdjyol5jOy29NeVIdsFJSFlQdLDqlDCVUt%2BQvADaIzacps8G%2FbQZ9K9LqyYXjJ9P%2FWuC9VBVO16wXvZihv22flM3nQ7Q32oa7ZY63kCpM1TpjPdlHn7lWfPFHwPDl1JeFLYMtXA7Fhj5Uirof5ATBvV9jutdSkF0nV%2FX%2FYXQe%2BfVwK1VQmI5eYnv3rT9PvQHQtJiwPG7d4Gv5%2Fj9%2BvEdN9lOAcxrwHChKo3J4fM6V6SLoYjuD8AXjQbfTQ%2B%2B9y0vtB7a8kLjr6XkRVn7LU8FgjLm7eQIR34nMC8HEB6KzKM5aNi%2FZ7DMVq3vKWtGQcc4A%2B7%2FSlkTmqf%2FPHUwP%2F1z7D%2F8Bw%3D%3D)

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

