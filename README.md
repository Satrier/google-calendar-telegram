google translate from image

![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/8f198751-ce5c-4398-b67c-f8a532c805b2)

1. Install needed libraries and modules

   ``` pip install asyncio datetime os random re time python-telegram-bot google-auth google-api-python-client openai python-dotenv ```


2. Need to create a progect in https://console.cloud.google.com/apis/credentials?project=calendar-to-telegram
and add ## **Service Accounts** and download .json file
see:
https://stackoverflow.com/questions/46287267/how-can-i-get-the-file-service-account-json-for-google-translate-api
3. Create calendar in https://calendar.google.com/calendar/ and Share with user **Service Accounts** email / like telegram@calendar-to-tel-bot.iam.gserviceaccount.com
![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/49a967f9-fa44-4877-ac7f-94a1c6cecaef)
4. Add events in created calendar like ![image](https://github.com/Satrier/google-calendar-telegram/assets/10636815/4234103c-624c-4a03-8521-639c253d0976)
5. Create telegram bot - add him to channel / group or supergroup
6. Register and create Key https://platform.openai.com/api-keys
7. Add needed keys in script and run
