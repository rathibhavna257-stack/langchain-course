from pydantic import BaseModel
from typing import List

class Component(BaseModel):
    name: str
    responsibility: str
    technology: str

class ArchitectureDesign(BaseModel):
    architecture_style: str
    components: List[Component]
    data_flow: str
    scalability_notes: str