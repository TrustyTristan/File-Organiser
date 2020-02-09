# File Organiser

## Idea

On going project as I learn more. The idea is to organise files based on type (hopefully more in the future) to sub directories.

Pretty much just copied [this](https://dev.to/sahilrajput/create-your-own-file-organiser-in-python-507i). I've just added comments so I could figure out what was going on and make it run on a folder I choose not the folder it's in.

## Install

Basically just copy anywhere. Change the CLEANUP_PATH to whatever you want to clean up and run.

I set mine up with a cronjob:

```
* * * * * /usr/local/bin/python3 ~/Documents/Scripts/./File_Organiser.py -p ~/Downloads/
```
Or if you want to run it more frequently (Like every 20 seconds):
```
* * * * * /usr/local/bin/python3 ~/Documents/Scripts/File_Organiser.py -p ~/Downloads/; sleep 20; /usr/local/bin/python3 ~/Documents/Scripts/File_Organiser.py -p ~/Downloads/; sleep 20; /usr/local/bin/python3 ~/Documents/Scripts/File_Organiser.py -p ~/Downloads/
```
This was crazy frustrating until I discovered [this](https://dccxi.com/posts/crontab-not-working-catalina/):
`
New Catalina security permissions require you to add cron to:
System Preferences.app -> Security & Privacy -> Privacy -> Full Disk Access
`

## To Do:
- Make it work on windows
  - I think this should work.. haven't tested it though.
- Add more features
  - Maybe organise Photos/Video using meta data?
    Date Created, Camera, etc