import json
import os
import sys
import requests

VARNAME_HOSTNAME = 'C9_HOSTNAME'
DEFAULT_APP_ROUTE = 'sms'

if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) != 2:
        print "Usage: python run.py <config_file>"
        exit(-1)
    config_filepath = sys.argv[1]

    # Parse configuration file
    try:
        config_file = open(config_filepath, 'r')
        config = json.load(config_file)
    except IOError:
        print "Configuration file not found - run `make install`"
        exit(-1)

    for required_key in ['account_sid', 'auth_token', 'phone_number_sid']:
        if required_key not in config:
            print "*** ERROR ***"
            print "config.json missing an entry: " + required_key
            print "edit config.json and add your twilio secret data and try again"
            exit(-2)
        if len(config[required_key]) < 30:
            print "*** ERROR ***"
            print "Invalid value for " + required_key
            exit(-2)

    print "Account SID: " + config['account_sid']
    print "Auth Token: " + config['auth_token']
    print "Phone Number SID: " + config['phone_number_sid']

    # Scrape app url from env and update PN SMS URL
    app_url = 'http://' + os.environ[VARNAME_HOSTNAME] + '/' + DEFAULT_APP_ROUTE
    print "App URL: " + app_url
    print "Updating SMS URL for phone number..."
    try:
        response = requests.post(
            'https://api.twilio.com/2010-04-01/Accounts/{}/IncomingPhoneNumbers/{}.json'.format(config['account_sid'], config['phone_number_sid']),
            auth=(config['account_sid'], config['auth_token']),
            data={
                'SmsUrl': app_url
            }
        )
    except:
        print "Could not update your Twilio phone number SMS URL"
        print "First, check your internet connection"
        print "Also, try reconfiguring by running `make configure`"
        exit(-1)
