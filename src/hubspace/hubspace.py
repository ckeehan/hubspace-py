from .util import getExpansions
from .hubspace_user import HubspaceUser 
from .hubspace_device import HubspaceDevice 

class Hubspace:

    devices = {}

    def __init__(self, username, password):
        self._user = HubspaceUser(username, password)

    def getAccountID(self):
        return self._user.getAccountID()

    def get(self, path, data=None, host=None):
        return self._user.get(path, data, host)

    def post(self, path, data=None, host=None):
        return self._user.post(path, data, host)

    def put(self, path, data=None, host=None):
        return self._user.put(path, data, host)

    def getDevices(self, expansions=[]):
        return self.get("accounts/" + self._user.getAccountID() + "/devices" + getExpansions(expansions))

    def getDeviceStates(self):
        return [ device["deviceState"] for device in self.getDevices(["state"]) ]

    def getDeviceTags(self):
        return [ device["deviceTags"] for device in self.getDevices(["tags"]) ]

    def getDeviceAttributes(self):
        return [ device["attributes"] for device in self.getDevices(["attributes"]) ]

    def getMetadata(self):
        return self.get("accounts/" + self._user.getAccountID() + "/metadevices", host="semantics2.afero.net")

    def getConclaveAccess(self):
        return self.post("accounts/" + self._user.getAccountID() + "/conclaveAccess", data="{}", host="api2.afero.net")

    def getDevice(self, deviceID):
        if self.devices.get(deviceID) == None:
            self.devices[deviceID] = HubspaceDevice(self, deviceID)
        return self.devices[deviceID]