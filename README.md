# There are too many uni students (and usel

## Instructions:
1. To use OpenAI API Key first source ~/.bashrc (because I'll likely forget where it was)
2. Activate the venv (because I'll likely forget this too)
3. Run tweet.py


Twitter acc that incorrectly pronounces words and gives the wrong definition
* Scrape word of the day from different websites (maybe top 10 most searched words? and keep a dictionary so there won't be repeats for a month?)
* Fine tune ai to do stupid shit
* Use twitter api to post on regular intervals (gaussian distribution of 0-7 hours)(a script that does that for a day and basically runs the script when the time is right)

Scrape -> AI to process word and definition -> shows me for verification (maybe on discord if I'm trying to be fancy, start with something stupidly simple) -> posts on twitter

Desired AI output:
1. Borderline gets me banned
2. Wrong pronunciations
3. Definition makes sense when you see the word but doesn't really work without that context - doesn't really do it right now? better prompt engineering needed? 

make it work first then change from gpt4 to mixtral because i'll run out of money

* scrape.py - Gets the WOTD
* rnd.py - wRites and Defines the words returned
* tweet.py - tweets on a scheduled basis (once a day at 1230 until i find a better solution)

