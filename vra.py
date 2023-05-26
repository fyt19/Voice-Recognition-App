#start

import speech_recognition as sr

# Create a recognizer object

r = sr.Recognizer()

# Use microphone as source

with sr.Microphone() as source:
  
    # Reduce background noise
    
    r.adjust_for_ambient_noise(source)
    
    # Ask the user for voice input
    
    print("Please speak...")
    
    # Get the voice from the microphone
    
    audio = r.listen(source)
    
    # Try to convert the voice to text
    
    try:
        # Use Google Speech Recognition service
        
        text = r.recognize_google(audio, language="en-US")
        
        # Print the text on the screen
        
        print("You said: {}".format(text))
        
        # Detect certain words and run functions
        
        if "thief" in text.lower():
          
            print("Thief alarm triggered!")
            
            # Here you can call a function that triggers the thief alarm.
            
        elif "fire" in text.lower():
          
            print("Fire alarm triggered!")
            
            # Here you can call a function that triggers the fire alarm.
            
        elif "help" in text.lower():
          
            print("Help call made!")
            
            # Here you can call a function that makes a help call.
            
        else:
          
            print("An unrecognized word was said.")
            
            # Here you can call a function that does something when an unrecognized word is said.
            
    # Give an error if the voice is not recognized
    
    except sr.UnknownValueError:
      
        print("Voice could not be understood.")
        
    # Give an error if the connection to the service cannot be established
    
    except sr.RequestError as e:
      
        print("Could not connect to the service; {0}".format(e))
        
#end
    
