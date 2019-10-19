# File Organiser

## Idea

On going project as I learn more. The idea is to organise files based on type (hopefully more in the future) to sub directories.

Pretty much just copied [this](https://dev.to/sahilrajput/create-your-own-file-organiser-in-python-507i). I've just added comments so I could figure out what was going on and make it run on a folder I choose not the folder it's in.

## Install

Basically just copy anywhere. Change the CLEANUP_PATH to whatever you want to clean up and run.

I set mine up with a cronjob:

```
* * * * * /usr/local/bin/python3 /Users/trusty/Scripts/File_Organiser_v1.py
```
This was crazy frustrating until I discovered [this](https://dccxi.com/posts/crontab-malfunction-catalina/):
`
New Catalina security permissions require you to add cron to:
System Preferences.app -> Security & Privacy -> Privacy -> Full Disk Access
`

## To Do:
- Make work on windows
  - Probably have to change a lot for this..
- "Package" it?
  - Make an application
- Make a GUI because... GUI
- Add more features
  - Select multiple folders
  - Maybe organise Photos/Video using meta data?
    Date Created, Camera, etc