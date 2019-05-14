# Page Checker Script

A simple but exceedingly useful script to check a given webpage for a given keyword at a given periodicity. Useful for staying on top of listings (such as craigslist posts) without having to check regularly yourself. Instead, the script will check every n minutes and you'll get an email when a match is found.

Requires a mailgun account and API key. To set up, create a secrets.py file in the project directory and add your variables:

key = 'YOUR_KEY'

sandbox = 'YOUR_SANDBOX.mailgun.org'

recipient = 'YOUR_EMAIL@DOMAIN.com'

Requires bs4 and requests. Run in a screen for best results!