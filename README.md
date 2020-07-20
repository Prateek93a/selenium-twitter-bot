# selenium-twitter-bot
Selenium based solution for creating a twitter bot. Selenium is a very powerful tool for web automation and scraping.

For making Twitter bot, one can use Twitter api, but its paid. With this program one can  login, like tweets of particular hashtag and even post a tweet.

Now, Twitter makes use of Dynamic classes, hence it was very difficult to choose the right attributes for the purpose, and maybe code might not work in future. But one can always inspect the Twitter page to look for suitable attributes. Also one can expand the codebase to implement even more features like following someone. An amazing feature would be to scrap a tweet where a particular user has been mentioned and based on tweet content, one can like the tweet or ignore it, this is Sentimental Analysis.
For non-ml background developers, AFINN111 is a nice alternative to perform this analysis.

Also this code is not restricted to just Twitter, one can modify it to run for Instagram, Linkedin as well. 

To setup the project->
1)Intall Python
2)Install Firefox
3)Download and unzip geckodriver and place geckodriver.exe inside Python3.7 folder so that python knows from where to run the browser
