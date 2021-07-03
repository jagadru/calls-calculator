from typing import TypeVar

from calls_calculator.models.call import Call
from calls_calculator.models.invoice import Invoice, Movement
from calls_calculator.models.telephon_number import PhoneNumber
from calls_calculator.models.user import User

CallInformation = TypeVar('CallInformation', bound=Call)
FullNumber = TypeVar('FullNumber', bound=PhoneNumber)
MovementInformation = TypeVar('MovementInformation', bound=Movement)
InvoiceInformation = TypeVar('InvoiceInformation', bound=Invoice)
UserInformation = TypeVar('UserInformation', bound=User)
