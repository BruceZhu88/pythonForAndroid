#-*-coding:utf8;-*-
#qpy:console
#qpy:2
import androidhelper
import time,sys
 
# Prepare the python for android API
droid = androidhelper.Android()

# Instruct Py4A which HTML file to use for the webview (we¡¯ll explore this later)
#droid.webViewShow('file:///sdcard/sl4a/scripts/daveTest/index.html')
droid.webViewShow('file:///index.html')
 
# SL4A uses the concept of events, like javascript does. 
# To use them, you need to ¡°register¡± to events, and take action whenever you detect an event. 
# Events are passed with various attributes to your script.
# So for example the ¡°name¡± attribute allows you to distinguish between different events, while the ¡°data¡± attribute contains the # data passed by the event
# You create your own event names and data via the webview as we¡¯ll soon see

while True: 
    # Wait for an event
    event = droid.eventWait().result
    
    #If / else statement to determine what action to take depending on the event name
    if event['name'] == 'kill':
        #exit if webview sends and event named ¡°kill¡±
        sys.exit()
    elif event['name'] == 'bluetooth':
        #switch bluetooth on
      	droid.toggleBluetoothState(True)
      	# this is a bluetooth client, so we just need to ask the user
      	# which bluetooth server to connect to, and connect
      	droid.bluetoothConnect()
      	
  # wait for a bluetooth message
	while True:
	  # We got a bluetooth message, so emit an event to the webview (using eventPost)
	  # named ¡°bluetoothOut¡± and pass the message along with the #event.
	  message = droid.bluetoothReadLine().result
	  droid.eventPost('bluetoothOut', message)
	  
	  #If the message is ¡°quit¡±, display a native android alert (not a web one) and #exit
	  if message =='quit':
	    title = 'dvas0004'
	    text = 'Server told me to turn bluetooth off'
            droid.dialogCreateAlert(title, text)
	    droid.dialogSetNeutralButtonText('Ok')
            droid.dialogShow()
            droid.dialogGetResponse().result
            droid.dialogDismiss()
	    break

    elif event['name'] == 'sayHi':

        # If the event the script receives is called ¡°sayHi¡± vibrate, create a notification 
        # in the notification bar, and an alert to boot¡­

        droid.notify('dvas0004',event['data'])
      	droid.vibrate()	
      	title = 'dvas0004'
      	text = 'Look at your notifications bar!'
      	droid.dialogCreateAlert(title, text)
      	droid.dialogSetNeutralButtonText('Ok')
        droid.dialogShow()
        droid.dialogGetResponse().result
        droid.dialogDismiss()