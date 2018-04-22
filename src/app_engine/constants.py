# Copyright 2015 Google Inc. All Rights Reserved.

"""AppRTC Constants.

This module contains the constants used in AppRTC Python modules.
"""
import os

# Deprecated domains which we should to redirect to REDIRECT_URL.
REDIRECT_DOMAINS =  [
  'mylivetour.com'
]
# URL which we should redirect to if matching in REDIRECT_DOMAINS.
REDIRECT_URL = 'https://www.mylivetour.com'

ROOM_MEMCACHE_EXPIRATION_SEC = 60 * 60 * 24
MEMCACHE_RETRY_LIMIT = 100

LOOPBACK_CLIENT_ID = 'LOOPBACK_CLIENT_ID'

# Turn/Stun server override. This allows AppRTC to connect to turn servers
# directly rather than retrieving them from an ICE server provider.
#ICE_SERVER_OVERRIDE = None
# Enable by uncomment below and comment out above, then specify turn and stun
ICE_SERVER_OVERRIDE  = [
   {
     "urls": [
       "turn:turn-server.mylivetour.com:5349?transport=udp",
       "turn:turn-server.mylivetour.com:5349?transport=tcp"
     ],
     "username": "livetour",
     "credential": "livetour"
   },
   {
     "urls": [
       "stun:turn-server.mylivetour.com:5349"
     ]
   }
]

ICE_SERVER_BASE_URL = 'https://networktraversal.googleapis.com'
ICE_SERVER_URL_TEMPLATE = '%s/v1alpha/iceconfig?key=%s'
ICE_SERVER_API_KEY = os.environ.get('ICE_SERVER_API_KEY')

# Dictionary keys in the collider instance info constant.
WSS_INSTANCE_HOST_KEY = 'signalling-server.mylivetour.com:443'
WSS_INSTANCE_NAME_KEY = 'signalling'
WSS_INSTANCE_ZONE_KEY = 'europe-west2-a'
WSS_INSTANCES = [{
    WSS_INSTANCE_HOST_KEY: 'signalling-server.mylivetour.com:443',
    WSS_INSTANCE_NAME_KEY: 'signalling',
    WSS_INSTANCE_ZONE_KEY: 'europe-west2-a'
}]

WSS_HOST_PORT_PAIRS = [ins[WSS_INSTANCE_HOST_KEY] for ins in WSS_INSTANCES]

# memcache key for the active collider host.
WSS_HOST_ACTIVE_HOST_KEY = 'wss_host_active_host'

# Dictionary keys in the collider probing result.
WSS_HOST_IS_UP_KEY = 'is_up'
WSS_HOST_STATUS_CODE_KEY = 'status_code'
WSS_HOST_ERROR_MESSAGE_KEY = 'error_message'

RESPONSE_ERROR = 'ERROR'
RESPONSE_ROOM_FULL = 'FULL'
RESPONSE_UNKNOWN_ROOM = 'UNKNOWN_ROOM'
RESPONSE_UNKNOWN_CLIENT = 'UNKNOWN_CLIENT'
RESPONSE_DUPLICATE_CLIENT = 'DUPLICATE_CLIENT'
RESPONSE_SUCCESS = 'SUCCESS'
RESPONSE_INVALID_REQUEST = 'INVALID_REQUEST'

IS_DEV_SERVER = os.environ.get('APPLICATION_ID', '').startswith('dev')

BIGQUERY_URL = 'https://www.googleapis.com/auth/bigquery'

# Dataset used in production.
BIGQUERY_DATASET_PROD = 'prod'

# Dataset used when running locally.
BIGQUERY_DATASET_LOCAL = 'dev'

# BigQuery table within the dataset.
BIGQUERY_TABLE = 'analytics'
