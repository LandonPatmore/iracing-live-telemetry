import aiohttp
import jsons

from classes.TelemetryInfo import TelemetryInfo


async def send_data(telemetry_info: TelemetryInfo):
    async with aiohttp.ClientSession() as session:
        telemetry_server_url = 'http://192.168.86.64:5000/telemetry'
        async with session.post(url=telemetry_server_url, json=jsons.dumps(telemetry_info)) as resp:
            res = await resp.json()
            print(res)
