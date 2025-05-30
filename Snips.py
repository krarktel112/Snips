import random
import string

def generate_unique_random_string(length, existing_strings=None):
    if existing_strings is None:
        existing_strings = set()
    
    while True:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if random_string not in existing_strings:
            existing_strings.add(random_string)
            return random_string
#firefox
from selenium import webdriver
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
driver.quit()
#chrome
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
print("Please check screenshot image")
driver.quit()
#countdown code
import time

def countdown(t):
    """
    This function counts down from a given time in seconds.
    """

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

if __name__ == '__main__':
    # Set the time in seconds (24 hours = 86400 seconds)
    t = 86400 

    countdown(t)
#email
# Importing libraries
import imaplib, email
 
user = input("User:")
password = input("Password:")
imap_url = 'imap.gmail.com'
 
# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
 
# Function to search for a key value pair 
def search(key, value, con): 
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
 
# Function to get the list of emails under this label
def get_emails(result_bytes):
    msgs = [] # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
 
    return msgs
 
# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url) 
 
# logging the user in
con.login(user, password) 
 
# calling function to check for email under this label
con.select('Inbox') 
 
 # fetching emails from this user "tu**h*****1@gmail.com"
msgs = get_emails(search('FROM', 'MY_ANOTHER_GMAIL_ADDRESS', con))
 
# Uncomment this to see what actually comes as data 
# print(msgs) 
 
 
# Finding the required content from our msgs
# User can make custom changes in this part to
# fetch the required content he / she needs
 
# printing them by the order they are displayed in your gmail 
for msg in msgs[::-1]: 
    for sent in msg:
        if type(sent) is tuple: 
 
            # encoding set as utf-8
            content = str(sent[1], 'utf-8') 
            data = str(content)
 
            # Handling errors related to unicodenecode
            try: 
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")
 
                # printing the required content which we need
                # to extract from our email i.e our body
                print(data2[0: indexend])
 
            except UnicodeEncodeError as e:
                pass
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Email:") # Enter your address
receiver_email = input("Outgoing:") or "ppteam36884@gmail.com" # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "krarktel@gmail.com"
receiver_email = "ppteam36884@gmail.com"
password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "output1.html"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    my_list = [1, 2, 2, 3, 4, 4, 5]
    my_set = set(my_list)
    print(my_set)  # Output: {1, 2, 3, 4, 5}
    
    my_string = "hello"
    string_set = set(my_string)
    print(string_set) # Output: {'h', 'e', 'l', 'o'}
    empty_set = set()
    print(empty_set)  # Output: set()
import random
import string

def generate_random_string(length=10):
  characters = string.ascii_letters + string.digits
  return ''.join(random.choice(characters) for i in range(length))

def generate_unique_random_strings(num_strings, string_length=10):
  generated_strings = set()
  while len(generated_strings) < num_strings:
    new_string = generate_random_string(string_length)
    generated_strings.add(new_string)
  return list(generated_strings)

# Example usage:
num_strings_to_generate = 5
string_length = 8
unique_strings = generate_unique_random_strings(num_strings_to_generate, string_length)

print(unique_strings)
import random
import string

def generate_unique_random_strings(num_strings, string_length):
    """
    Generates a list of unique random strings.

    Args:
        num_strings: The number of random strings to generate.
        string_length: The length of each random string.

    Returns:
        A list of unique random strings.
    """
    string_list = set()
    while len(string_list) < num_strings:
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))
        string_list.add(random_string)
    return list(string_list)

# Example usage:
num_strings = 5
string_length = 10
unique_strings = generate_unique_random_strings(num_strings, string_length)
print(unique_strings)

#js
npm install @smartthings/core-sdk
const { SmartThingsClient } = require('@smartthings/core-sdk');

async function executeScene(sceneId) {
  const client = new SmartThingsClient({
    accessToken: 'YOUR_PERSONAL_ACCESS_TOKEN',
  });

  try {
    await client.scenes.execute(sceneId);
    console.log('Scene executed successfully!');
  } catch (error) {
    console.error('Error executing scene:', error);
  }
}

// Example usage
executeScene('YOUR_SCENE_ID');
const { SmartThingsClient, BearerTokenAuthenticator } = require('@smartthings/core-sdk');

const PERSONAL_ACCESS_TOKEN = '372563b7-09f8-485b-8c95-261793424ad9';
const ROUTINE_ID = 'YOUR_ROUTINE_ID';

const client = new SmartThingsClient(new BearerTokenAuthenticator(PERSONAL_ACCESS_TOKEN));

async function executeRoutine() {
  try {
    await client.routines.execute(ROUTINE_ID);
    console.log('Routine executed successfully!');
  } catch (error) {
    console.error('Error executing routine:', error);
  }
}

executeRoutine();

import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print(ST.scenes)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes['Home']['Ashley1'])
import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print(ST.scenes)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes['Home']['Ashley2'])
import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print(ST.scenes)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes['Home']['Ashley1'])
import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print(ST.scenes)
# Reference the SmartThings API documentation for information regarding the
# format of capabilities, commands, and arguments

ST.execute_scene(ST.scenes['Home']['Ashley4'])

import SmartThings

token = '372563b7-09f8-485b-8c95-261793424ad9'
ST = SmartThings.Account(token)
print("scenes")
print(ST.scenes)
print("devices")
print(ST.devices)
print("locations")
print(ST.locations)

import json

def read_config_json(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data= json.load(file)
            return config_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
    except  Exception as e:
        print(f"An unexpected error occured: {e}")
        return None
config_file_path = r"C:\Users\User\AppData\Roaming\BetterDiscord\plugins\Aoffline.config.json"
config = read_config_json(config_file_path)
online = "online"
idle = "idle"
dnd = "dnd"
gaming = "gaming"
streaming = "streaming"
listening = "listening"
playing = "playing"
if config:
    print(config)
    if online in config:
        print("Online")
    elif idle in config:
        print("Idle")
    elif dnd in config:
        print("DND")
    elif gaming in config:
        print("Gaming")
    elif playing in config:
        print("Playing")
    elif listening in config:
        print("Listening")
    elif streaming in config:
        print("Streaming")
    else:
        print(config)
else:
    print("Failed to load configuration.")

#!/usr/bin/env python
# encoding: utf-8

import npyscreen
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()
