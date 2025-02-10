DOMAIN = "homeNet"

def setup(hass, config):
    hass.data.setdefault(DOMAIN, {})
    return True