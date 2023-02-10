from pydantic import BaseModel

from .ArpPriorityLevel import ArpPriorityLevel
from .PreemptionCapability import PreemptionCapability
from .PreemptionVulnerability import PreemptionVulnerability


class Arp(BaseModel):
    priorityLevel: ArpPriorityLevel
    preemptCap: PreemptionCapability
    preemptVuln: PreemptionVulnerability
