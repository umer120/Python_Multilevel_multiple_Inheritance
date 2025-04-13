class Phone:
    def call(self):
        return "Making a phone call"
    
    def message(self):
        return "Sending a text message"

class Camera:
    def take_photo(self):
        return "Taking a photo"
    
    def record_video(self):
        return "Recording a video"
    
class Smartphone(Phone, Camera):
    def browse_internet(self):
        return "Browsing the internet"


    
smartphone = Smartphone()


print(smartphone.call())
print(smartphone.message())
print(smartphone.take_photo())
print(smartphone.record_video())
print(smartphone.browse_internet())
