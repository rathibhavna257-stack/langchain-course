def generate_uml(architecture):
    uml = "@startuml\n"
    uml += "skinparam componentStyle rectangle\n"
    uml += "skinparam shadowing false\n\n"

    uml += "actor User\n\n"
    uml += 'rectangle "Cloud Infrastructure" {\n'

    aliases = {}
    notes = []

    for idx, comp in enumerate(architecture.components, start=1):
        alias = f"C{idx}"
        aliases[comp.name] = alias

        label = f"{comp.name}\\n({comp.technology})"
        uml += f'  component "{label}" as {alias}\n'

        tech = comp.technology.lower()

        # 🔐 Auto security notes
        if "api" in tech:
            notes.append((alias, "OAuth2\nRate limiting"))
        if "postgres" in tech or "rds" in tech:
            notes.append((alias, "Encrypted at rest\nHIPAA compliant"))
        if "sns" in tech or "firebase" in tech:
            notes.append((alias, "Asynchronous\nEvent-driven"))

    uml += "}\n\n"

    # 🔁 Auto flow (basic heuristic)
    if "API Gateway" in aliases:
        uml += f'User --> {aliases["API Gateway"]} : Submit symptoms\n'

    flow_order = list(aliases.values())
    for i in range(len(flow_order) - 1):
        uml += f'{flow_order[i]} --> {flow_order[i+1]}\n'

    uml += "\n"

    # 📝 Attach notes
    for alias, note in notes:
        uml += f'note right of {alias}\n{note}\nend note\n\n'

    uml += "@enduml"
    return uml
def generate_sequence_uml(architecture):
    uml = "@startuml\n"
    uml += "actor User\n"

    participants = []
    for comp in architecture.components:
        alias = comp.name.replace(" ", "")
        participants.append(alias)
        uml += f'participant "{comp.name}" as {alias}\n'

    uml += "\nUser -> APIGateway: Submit symptoms\n"
    uml += "APIGateway -> SymptomAnalysisService: Analyze symptoms\n"
    uml += "SymptomAnalysisService -> PatientDataService: Fetch patient history\n"
    uml += "PatientDataService --> SymptomAnalysisService: Patient data\n"
    uml += "SymptomAnalysisService -> NotificationService: Send alert\n"
    uml += "NotificationService --> User: Notification sent\n"

    uml += "@enduml"
    return uml

