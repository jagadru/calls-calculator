<<<<<<< HEAD
COUNTRY_CODE_REGEX = r"^\+(?P<country_code>\d.*?)9"
||||||| parent of e340180 (Fixing pre-commit issues)
import os

COUNTRY_CODE_REGEX = r"^\+(?P<country_code>\d.*?)9"
=======
import os

COUNTRY_CODE_REGEX = r'^\+(?P<country_code>\d.*?)9'
>>>>>>> e340180 (Fixing pre-commit issues)
BASE_FEE_NATIONAL_CALL = 2.5
BASE_FEE_INTERNATIONAL_CALL = 20.0
MINUTES_FOR_FRIENDS_CALLS = 150
FRIENDS = 'FRIENDS'
NATIONAL = 'NATIONAL'
INTERNATIONAL = 'NATIONAL'
BASE_USER_SERVICE_URL = 'https://interview-brubank-api.herokuapp.com/'
USER_INFORMATION_RESOURCE = 'users/'
BILLING_PERIOD_DATETIME_FORMAT = '%Y-%m-%d'
CALL_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
