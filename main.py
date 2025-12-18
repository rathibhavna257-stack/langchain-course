from dotenv import load_dotenv
load_dotenv()

from architect_agent import architectural_agent
# from uml_generator import generate_uml
from uml_generator import generate_uml, generate_sequence_uml
from flow_generator import generate_flow_diagram

requirements = """
AI-driven Patient Symptom Triage System
- High scalability
- Secure patient data
- Real-time recommendations
"""

architecture = architectural_agent(requirements)

print("Architecture Style:", architecture.architecture_style)
print("Components:")
for c in architecture.components:
    print("-", c.name, ":", c.technology)

uml_code = generate_uml(architecture)
print("\nGenerated UML:\n", uml_code)

# ---- SAVE UML TO FILE ----
with open("architecture.puml", "w") as f:
    f.write(uml_code)

# print("\nSaved diagram file: architecture.puml")

sequence_uml = generate_sequence_uml(architecture)
with open("sequence.puml", "w") as f:
    f.write(sequence_uml)
print("Sequence diagram saved as sequence.puml")

# ---- OPTIONAL: AUTO-RENDER PNG ----
# import subprocess
# subprocess.run(["plantuml", "architecture.puml"], check=True)

# print("Rendered diagram: architecture.png")


flow_uml = generate_flow_diagram()
with open("flow.puml", "w") as f:
    f.write(flow_uml)

print("Flow diagram saved as flow.puml")

