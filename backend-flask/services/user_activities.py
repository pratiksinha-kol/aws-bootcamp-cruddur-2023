from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class UserActivities:
  def run(user_handle):
    try:
    # X-ray ---->
    #  segment = xray_recorder.begin_segment('user-activities')
    # above line not required anymore (refer line 32, https://docs.aws.amazon.com/xray-sdk-for-python/latest/reference/basic.html)

      model = {
      'errors': None,
      'data': None
    }

      now = datetime.now(timezone.utc).astimezone()

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results
    
    # X-ray ---->
      subsegment = xray_recorder.begin_subsegment('mock-data-subsegment')
      dict = {
      "now": now.isoformat(),
      "results-size": len(model['data'])
     }
      subsegment.put_metadata('key', dict, 'namespace')
      xray_recorder.end_subsegment()
    finally:
      xray_recorder.end_subsegment()
    return model