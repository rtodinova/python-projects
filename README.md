This repository contains 10 Python projects: web applications, desktop applications, data analyse and other.

Here is a description of the projects included:

1. Interactive Dictionary - smart English dictionary, which uses json in order to display definitions of requested words. The dictionary uses difflib if there is a misspell in the user input and suggests similar word.
2. Webmaps with Python and Folium - web map implemented with Folium, that contains markers for all volcanoes in the world and their evaluation (using a csv file from www.arcgis.com) and different colors depending on the population of the country.

![Screenshot of the map](https://i.imgur.com/u5NxskS.png)

3. Website Blocker - blocking given websites for a specific time of the day (for example - blocking facebook for the working hours). The application contains of two python files - one for Windows users with .pyw extension and one for Mac and Linux users.
How to schedule the Website Blocker?

For Windows users:
  1. Open Task Scheduler and click Create a Basic Task, give it a name (for example Website Blocker)
  2. Configure it for your Windows version in the bottom of the window - Configure for and the dropdown menu and tick "Run with highest privileges"
  3. In the menu Triggers choose "New..." and for "Begin the task" choose "At startup". Click OK.
  4. In the menu Actions choose "New..." and browse for the daily_blocker.pyw file
  4. In the Conditions menu untick "Start the task only if the computer is on AC power"
  
You're done!

For Linux and Mac users:
  1. In the terminal write sudo crontab -e and choose an editor (nano for example)
  2. In the end of the file write:
    @reboot python3 /full/path/to/python/file/daily_blocker.py
  3. Ctrl+X, press Y and Enter to save the file

You're done!
