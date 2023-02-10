from enum import Enum


class PreemptionCapability(Enum):
    not_preempt = "NOT_PREEMPT"
    may_preempt = "MAY_PREEMPT"
