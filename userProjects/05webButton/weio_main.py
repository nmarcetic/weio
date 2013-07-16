# Example of WEB button interrupt
# Turning ON LED 

LED_PIN = 1

BUTTON_WEB_ON = "turn on"
BUTTON_WEB_OFF = "turn off"


def setup() :
    
    # tells that LED is output
    pinMode(LED_PIN, OUTPUT) 
    
    # Attaches interrupt from Web client
    attach.interrupt(BUTTON_WEB_ON, onTurnOn)
    
    # Attaches interrupt from Web client
    attach.interrupt(BUTTON_WEB_OFF, onTurnOff)
    

# msg can be useful if additional data is sent
# like button is pressed, released, some message
# msg is generated by user
def onTurnOn(msg): 
    pinMode(LED_PIN, HIGH)


def onTurnOff(msg) :
    pinMode(LED_PIN, LOW)


runWeio()