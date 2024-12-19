from lib.core.compat import xrange
from lib.core.enums import PRIORITY
 
__priority__ = PRIORITY.LOW
 
def dependencies():
    pass
 
def tamper(payload, **kwargs):
    payload= payload.replace('select' , 'selselectect')
    retVal=payload
    return retVal
 
 