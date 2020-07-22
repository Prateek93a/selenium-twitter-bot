# selenium-twitter-bot
Selenium based solution for creating a twitter bot. Selenium is a very powerful tool for web automation and scraping. For making Twitter bot, one can use Twitter api, but its paid. This solution on the other hand is not but does require much more work to get things right. 

## Features:
 - Logging into your Twitter account
- Liking tweets of your homepage
- Searching for some keyword or hashtag
- Liking tweets of the search results
- Posting tweets
- Logging out of your account

## Note:
Twitter makes use of dynamic classes, hence it's difficult to choose the right attributes for the purpose, and maybe code might not work for all the features in the future( although the attributes I have used will most likely work ). But one can always inspect the Twitter page to look for suitable attributes. 

## Running project locally:

 1. Have `python` environment setup
 2. Clone the repo and go to the cloned directory
 3. Run `pip3 install selenium`
 4. Now you may run any of the given example scripts or write and execute your own scripts 

## Examples:

All the following tasks are completely automated without any manual user input. The script launches Firefox instance and carrys out the tasks provided.
#### Posting Tweets
![tweet2gif](https://user-images.githubusercontent.com/44807945/87979619-f7b43b80-caef-11ea-8f63-266c8ed9c481.gif)

#### Adding likes to tweets on homepage
![tweet1gif](https://user-images.githubusercontent.com/44807945/87979792-3a761380-caf0-11ea-8a8f-433fe46f8526.gif)

#### Adding likes to tweets on search results of some query
![tweet3gif](https://user-images.githubusercontent.com/44807945/87979877-5aa5d280-caf0-11ea-8738-f2c29a37edca.gif)



## Attribution:
This project is inspired from DevEd([@developedbyed](https://twitter.com/developedbyed?lang=en)) tutorial on Twitter automation using Selenium where he explains how to search for a hashtag and like the related posts. I built on top of it and added new features such as posting tweets, adding likes to tweets on homepage, search for any keyword and like related posts and logging out.

## What's next:
I will be working on adding feature of finding and following new users. Apart from that I will also add features to perform other tasks on tweets such retweeting them.
