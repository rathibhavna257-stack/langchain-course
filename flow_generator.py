def generate_flow_diagram():
    return """
@startuml
start

:User submits symptoms;

:API Gateway validates request;

if (Request valid?) then (yes)
    :Forward to Symptom Analysis Service;
else (no)
    :Reject request;
    stop
endif

:Analyze symptoms using ML;

if (Critical case?) then (yes)
    :Store patient data;
    :Trigger notification;
    :Alert doctor / patient;
else (no)
    :Store patient data;
    :Schedule follow-up;
endif

stop
@enduml
"""
