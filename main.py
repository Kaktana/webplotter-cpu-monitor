import requests
import time
import os
import psutil

MONITORING_CHART_URL = os.environ.get("MONITORING_CHART_URL")
MONITORING_PERIOD = int(os.environ.get("MONITORING_PERIOD"))
NODE_PREFIX = os.environ.get("NODE_PREFIX")

print("HOST PREFIX", NODE_PREFIX)
print("MONITORING PERIOD", MONITORING_PERIOD)
print("MONITORING CHART URL", MONITORING_CHART_URL)

while True:
    request = []
    time.sleep(MONITORING_PERIOD)
    cpus = psutil.cpu_percent(percpu=True)
    for i, cpu_perc in enumerate(cpus):
        request.append({
            "key": "{}-cpu_{}".format(NODE_PREFIX, str(i)),
            "value": cpu_perc
        })
    request.append({
        "key": "{}-memory_u_s_e_d".format(NODE_PREFIX),
        "value": psutil.virtual_memory().percent
    })
    print("trying on", MONITORING_CHART_URL + "/addPoints")
    requests.post(MONITORING_CHART_URL + "/addPoints", json=request)
