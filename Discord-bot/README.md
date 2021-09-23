1.Setup
 *Start an application on discord developer portal, Add a bot and connect to the sever. Then u can generate the token. create a .env file paste the token into the file. DISCORD_TOKEN={your-bot-token}
 *put .env into gitignore to avoid git cache it, or discord will regenerate a new token automaticlly. .env should be in the same folder with .py file in order to work.
 *Need to install python3 python3-pip discord.py python3-dotenv

2.Usage
 *I changed the code from client to bot. define the bot instead of client.Then do bot even to print the connecting conformation. Then do bot.commands to respond to the specific word that user type in discord.(Since its a command need to add !to the front).In the end bot.run(TOKEN)
 *I can type !funny in order to get the funny quotes
 *response:funny quote:
        'I’m sick of following my dreams, man. I’m just going to ask where they’re going and hook up with ’em later.',
        'A pessimist is a person who has had to listen to too many optimists.',
        'Better to remain silent and be thought a fool than to speak out and remove all doubt.',
        'Don’t worry about the world coming to an end today. It is already tomorrow in Australia.',

3.Research
 *First is to download some host softwares to manage the bot keeps running 24/7
 *Or maybe we install SCREEN and start a new screen to run the process then close the terminal. As long as the computer is running the bot should be actived.

