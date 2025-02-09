DOMAIN = "homeNet"

def setup(hass, config):
    hass.states.set("homeNet.hello", "Successfully installed!")
    return True