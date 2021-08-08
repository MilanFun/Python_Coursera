import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped



@to_json
def get_data(parm):
  return {
    'data': parm
  }

# print(get_data([1, 2, 3]))
  
