google translate from image

![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/b73b2123-4118-4813-a012-2d6bb6e90bbb)


1. Install needed libraries and modules

   ``` pip install asyncio datetime os random re time python-telegram-bot google-auth google-api-python-client openai python-dotenv ```


2. Need to create a progect in https://console.cloud.google.com/apis/credentials?project=calendar-to-telegram
and add ## **Service Accounts** and download .json file
see:
https://stackoverflow.com/questions/46287267/how-can-i-get-the-file-service-account-json-for-google-translate-api
3. Create calendar in https://calendar.google.com/calendar/ and Share with user **Service Accounts** email / like telegram@calendar-to-tel-bot.iam.gserviceaccount.com
![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/148e67a6-3295-49bc-a408-e25ff047eb03)

4. Add events in created calendar like ![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/af6490ed-6b48-4deb-8c75-1a293046c43d)

5. Create telegram bot - add him to channel / group or supergroup
6. Register and create Key https://platform.openai.com/api-keys
7. Add needed keys in script and run
