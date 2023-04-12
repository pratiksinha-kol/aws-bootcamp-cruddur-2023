#from aws_xray_sdk.core import xray_recorder

class UserActivities:
  def run(user_handle):
    try:
      model = {
        'errors': None,
        'data': None
      }
    
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        sql = db.template('users','show')
        results = db.query_array_json(sql)            
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