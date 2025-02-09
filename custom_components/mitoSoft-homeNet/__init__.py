DOMAIN = "mitoSoft-homeNet"

def setup(hass, config):
    hass.states.set("mitoSoft-homeNet.hello", "Successfully installed!")
    return True