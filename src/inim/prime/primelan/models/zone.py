from dataclasses import dataclass
from enum import IntEnum

from inim.prime.primelan.models.panel_item import PanelItemStatus


class ZoneState(IntEnum):
    TAMPER = 0
    STANDBY = 1
    ALARM = 2
    SHORT_CIRCUIT = 3


@dataclass(frozen = True)
class ZoneStatus(PanelItemStatus):
    terminal_id: int  # "tl" - zone terminal_id
    state: ZoneState  # "st" - 0=fault, 1=ready, 2=alarm, 3=short circuit
    alarm_memory: bool  # "mm" - False=not present, True=present
    bypass: bool

    def __str__(self) -> str:
        return (
            f"Zone {self.id}: {self.name} (Terminal {self.terminal_id})\n"
            f"  State: {self.state.name}\n"
            f"  Alarm memory: {'Yes' if self.alarm_memory else 'No'}\n"
            f"  Bypass: {'Yes' if self.bypass else 'No'}"
        )

    def short_str(self) -> str:
        return f"Zone {self.id}: {self.name}"


from dataclasses import dataclass


@dataclass(frozen = True)
class ZoneBypassSetRequest:
    zone_id: int
    bypass: bool = True  # True = bypass, False = included
