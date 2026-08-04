from dataclasses import dataclass
from enum import IntEnum

from inim.prime.primelan.models.panel_item import PanelItemStatus


class ArmingStatus(IntEnum):
    ARM_AWAY = 1
    ARM_STAY = 2
    ARM_INSTANT = 3
    DISARMED = 4


class PartitionState(IntEnum):
    ALARM = 0
    OK = 1
    TAMPER = 2


@dataclass(frozen = True)
class PartitionStatus(PanelItemStatus):
    arming_status: ArmingStatus
    state: PartitionState
    alarm_memory: bool

    def __str__(self) -> str:
        return (
            f"Partition {self.id}: {self.name}\n"
            f"  Arming status: {self.arming_status.name}\n"
            f"  State: {self.state.name}\n"
            f"  Alarm memory: {'Yes' if self.alarm_memory else 'No'}"
        )


@dataclass(frozen = True)
class SetPartitionArmingStatusRequest:
    partition_id: int
    arming_status: ArmingStatus


@dataclass(frozen = True)
class ClearPartitionAlarmMemoryRequest:
    partition_id: int
