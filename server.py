from bottle import route, run
import json


'''@route('/ahmed3lanamedaddo')
def hello():
    return json.dumps({"data": [
        {"action": "JasperSitting", "actor": "Jasper", "obj": "chair"},
        {"action": "JasperWalking", "actor": "Jasper", "obj": ""},
        {"action": "PearlWalking", "actor": "Pearl", "obj": ""},
        {"action": "JasperJump", "actor": "Jasper", "obj": ""},
        # {"action": "PearlWalking", "actor": "Pearl", "obj": ""},
        # {"action": "PearlWalking", "actor": "Pearl", "obj": ""},
        # {"action": "PearlWalking", "actor": "Pearl", "obj": ""},
        # {"action": "PearlIdle", "actor": "Pearl", "obj": ""},
        # {"action": "PearlStandToSit", "actor": "Pearl", "obj": ""},
        # {"action": "JasperJump", "actor": "Jasper", "obj": ""},
        # {"action": "Jasper1StandToSit", "actor": "Jasper1", "obj": ""},
        # {"action": "PearlIdle", "actor": "Pearl", "obj": ""},
        # {"action": "JasperIdle", "actor": "Jasper", "obj": ""},
        # {"action": "Jasper1Idle", "actor": "Jasper1", "obj": ""},
       
    ]})


@route('/init')
def hello():
    # return json.dumps({"objects": ["Jasper"], "scene": ["street"]})
    return json.dumps({"characters": ["Jasper",  "Pearl"], "objects": ["chair"], "scene": ["street"]})
'''

run( port=8080, debug=True)
