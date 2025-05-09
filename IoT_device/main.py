class Device:
    def turn_on(self):
        raise NotImplementedError

class Fan(Device):
    def turn_on(self):
        print("Fan is spinning...")

class Light(Device):
    def turn_on(self):
        print("Light is glowing...")

class AC(Device):
    def turn_on(self):
        print("AC is cooling...")

def activate_device(device: Device):
    device.turn_on()

devices = [Fan(), Light(), AC()]

for dev in devices:
    activate_device(dev)
