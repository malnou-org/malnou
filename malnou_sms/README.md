# malnou_sms

malnou_sms is a 2-way SMS based communication framework that uses the SMS gateway 'TextLocal' which supports 2-way communication in India.

malnou_sms was built in order to help give a voice to the thousands of parents who have their kids enrolled in numerous anganwadis all over India.

After visiting a few anganwadis and speaking with the parents who withdrew their kids from these anganwadis we were able to get insights as to why they wished to do so.

One of the main reason was that the parents felt like they did not have a sense of power to stand up to the corrupt/ irresponsible staff.

The kids in a few anganwadis were beaten up and served bad quality food. The parents who feel helpless find it easier to just remove the child from the anganwadis rather than stand up to these workers.

Hence it is important to give them a platform to raise their problems and complaints.

It is also important to keep them update about the current happenings, Weekly food plan, and supplements that are being provided. By doing so the parents can now feel like they are part of the process instead of feeling isolated.

## Quickstart

Before you can start using malnou_sms you need to create a 'TextLocal' account and a 'Firebase Database' project.

1. Create a 'TextLocal' account, obtain an 'API key' and a 'Keyword'. The keyword is used to redirect the messages to your inbox. If you wish to create a 'dedicated number' in TextLocal you don't need to use the Keyword as all the messages sent to this number would be directly sent to your inbox.

Take these values and input them in the config file

2. Create a firebase project and obtain the JSON file containing the private key.
for more information refer to this firebase [documentation](https://firebase.google.com/docs/admin/setup) 

3. Install dependencies

First, install python 3.6
```bash
sudo apt-get update
sudo apt-get install python3.6
```

Now install pip and virtualenv
```bash
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 
```

Install all the dependencies by typing
```bash
sudo pip install -r requirements.txt
```
(If you wish to run the application in a virtalenv. Create and activate your virtalenv before running the above bash command)

4. Now you can finally run the application by typing 

```bash
python app.py
```

This should start a flask server with rest apis running on your localhost

## Usage
When you start the server, a listener process runs in the background and listens to any new messages (Complaints). 
If a new complaint is received, The complaint is translated from its regional language and this translated message is used to obtain valuable insights regarding the type of complaint, keyphrases in the complaint and the overall sentiment of the complaint using IBM Watson's Natural Language Understanding API. 

You can communicate with the server by doing these API calls

**getMessages**
----
  Returns JSON data about the default messages that are saved on the server.

* **URL**

    /api/v1.0/get_messages

* **Method:**

    `GET`

* **Success Response:**

  * **Code:** 200
  * **Content:** `{"messages": [{"name": "GreetingMessage", "message": "Hello"}]}`

* **Sample Call:**

  ```bash
  curl -i http://localhost:5000/api/v1.0/get_messages
  ```

**setMessages**
----
  Used to set the default messages that can be sent from the system.

* **URL**

    /api/v1.0/set_messages

* **Method:**

    `POST`

* **Success Response:**

  * **Code:** 200
  * **Content:** `{"messages": [{"name": "GreetingMessage", "message": "Ok"}]}`

* **Sample Call:**

  ```bash
  curl -i -H "Content-Type: application/json" -X POST -d '{"messages":[{"name": "GreetingMessage", "message": "Ok"}]}' http://localhost:5000/api/v1.0/set_messages
  ```

**sendDefaultMessages**
----
  Used to send the default messages to the contacts of your choice.

* **URL**

    /api/v1.0/send_default_messages

* **Method:**

    `POST`

* **Success Response:**

  * **Code:** 200

* **Sample Call:**

  ```bash
  curl -i -H "Content-Type: application/json" -X POST -d '{"numbers":[91xxxxxxxx, 91xxxxxxxxxx], "message_type": "GreetingMessage"} http://localhost:5000/api/v1.0/send_default_messages
  ```
  For more information related to the different message types as used in the above sample check out the 'messages.json' file.

**sendMessages**
----
  Used to send messages to the contacts of your choice.

* **URL**

    /api/v1.0/send_messages

* **Method:**

    `POST`

* **Success Response:**

  * **Code:** 200

* **Sample Call:**

  ```bash
  curl -i -H "Content-Type: application/json" -X POST -d '{"numbers":[91xxxxxxxx, 91xxxxxxxxxx], "message": "Hello"} http://localhost:5000/api/v1.0/send_messages
  ```


