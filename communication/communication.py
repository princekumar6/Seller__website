
# Create your views here.
from .config import config
from .email_communication import send as send_email
from .mobile_communication import send as send_mobile
from .notification_communication import send as send_notification


#  all parameter expact as array
#channels={
#   'email':{from_:'mobile',to_:[]}
#   'mobile':[]
#   'notification':[]
# }
def send(channels=None):
    if channels is None:
        return
    for key in channels:
        if key in config['channels'] :
            globals()['send_'+key](channels[key])
        

