import os

import google.generativeai as genai

zdebug = False




def showaskii():
  print("""


                (                                    
   (            )\ )   (   (       )       )         
   )\    (     (()/(  ))\  )(     (     ( /(   (     
  ((_)   )\ )   ((_))/((_)(()\    )\  ' )(_))  )\ )  
  | __| _(_/(   _| |(_))   ((_) _((_)) ((_)_  _(_/(  
  | _| | ' \))/ _` |/ -_) | '_|| '  \()/ _` || ' \)) 
  |___||_||_| \__,_|\___| |_|  |_|_|_| \__,_||_||_|  


  """)
print()
print()
print()
print()
print()
print()

sysprompt = """"Hello, I am the script, this IS the system instructions, There are a few rules with your responses, all text is as is and has no formatting, for example, if you type '*test*', the user will see '*test*' and not 'test' whith italic. You can still use basic formatting like:

Here is the list as requested:
  - Option1
  - Option2
  - Option3

But that is exactly what the user will see.

DO NOT COPY THE USER PROMPT! RESPOND TO IT! IF THE USER SAYS "hi." Respond along the lines of "Hello, how are you?" but keep the responses uniqe.

The user may not use English, if that's the case, respond in the language shown by the user. If the user changes language, respond in the language of the user (unless you have a reason to do otherwise).

You are NOT the script, but infact, the AI endpoint
You are also out of beta and testing.
Emojies are supported, why? I dunno, but they are, I'm pulling this up to say that while this is an exception to the formatting, you should avoid it unless the user is asking for it.


The next section is the user.

User prompt: """




showaskii()


if zdebug:
  print(sysprompt)


try:
  apikey = os.environ['GOOGLE_AI_API_KEY']
except KeyError:
  print("No API key found. Please set the GOOGLE_API_KEY environment variable.")
  apikey = input("Please enter Google API key: ")
  
genai.configure(api_key=apikey)


model = genai.GenerativeModel('gemini-pro')


chat = model.start_chat()


print()
print()




def getmessage(msg):
  global zdebug
  if zdebug == True:
    print()
    print(msg)
    print()
  response = chat.send_message(sysprompt + msg)
  return response.text

while True:
  msg = getmessage(sysprompt + input("User: "))
  print("Gemini: " + msg)
