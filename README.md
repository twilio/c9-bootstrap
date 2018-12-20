# twilio-c9-bootstrap
###### Jumpstart your first Twilio app using Python and Cloud9!

twilio-c9-bootstrap is designed to make setting up your first Twilio app a breeze. Here's a walkthrough of how to get one up in no time.

1. [Set up a Twilio account](https://www.twilio.com/try-twilio).
2. [Buy a phone number](https://www.twilio.com/user/account/phone-numbers/search).
3. [Set up a Cloud9 account](http://twilio-invite.herokuapp.com/)
  - Input your twilio account into page.
  - You should receive a Cloud9 invite link. Use the link to set up your account.
  - On the "Join team" page, instead of joining team, just "Go to dashboard".
4. [Create a new workspace](https://c9.io/new).
  - Under `Clone from Git or Mercurial URL` enter `https://github.com/twilio/c9-bootstrap`
  - Under `Hosted workspace` select `Public`
  - Under `Choose a template` select `Python`
4. Set up your application.
  - In your newly created workspace, click on the terminal window (bottom pane).
  - Type `make install` and return.
  - Enter your credentials and phone number sid from steps 1 and 2 when prompted.
  - Type `python run.py` and enter to run your server.

Now, send a text to your Twilio number. You should get a response from your app! You're all set to start developing your first Twilio app.

##### Next steps
- Tinker around with `run.py` to add more functionality to your app.
- Explore [Twilio's API Documentation & Libraries](https://www.twilio.com/api)

##### Additional `make` options
- `make` - Installs, configures and starts your server
- `make install` - Installs and configures your server
- `make configure` - Sets up configuration files
- `make bootstrap` - Reconfigures your server
- `make serve` - Starts your server
- `make clean` - Uninstalls your server
