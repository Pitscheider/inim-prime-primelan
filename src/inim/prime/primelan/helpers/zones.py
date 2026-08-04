from inim.prime.primelan.client import InimPrimeClient
from inim.prime.primelan.models.zone import ZoneStatus, ZoneBypassSetRequest


def get_bypassed_zones(
        zones: dict[int, ZoneStatus],
) -> dict[int, ZoneStatus]:
    return {
        zone_id: zone
        for zone_id, zone in zones.items()
        if zone.bypass
    }


async def disable_all_zone_bypasses(
        zones: dict[int, ZoneStatus],
        client: InimPrimeClient,
        timeout: int | None = None,
        retries: int | None = None,
        retry_delay: float | None = None,
) -> dict[int, ZoneStatus]:
    bypassed_zones = get_bypassed_zones(zones)

    for zone in bypassed_zones.values():
        request = ZoneBypassSetRequest(
            zone_id = zone.id,
            bypass = False,
        )
        await client.set_zone_bypass(
            request = request,
            timeout = timeout,
            retries = retries,
            retry_delay = retry_delay,
        )

    return bypassed_zones
