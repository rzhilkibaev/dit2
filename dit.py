#!/usr/bin/env python3

import docker
import time
# cat /proc/self/cgroup | grep "docker" | head --lines 1 | rev | cut -d'/' -f1

print("Manager started")

# get this container id
with open("/proc/self/cgroup") as f:
   container_id = f.readline().rstrip().split("docker")[1][1:]
print("This container id: " + container_id)

client = docker.Client(base_url='unix://var/run/docker.sock')

# get project instance id
project_instance_id = client.containers(all=True, filters={"id": container_id})[0].get("Labels").get("com.docker.compose.project")
print("Project instance id: " + project_instance_id)

test_container_id_2_status = {}
#status=(created|restarting|running|paused|exited)
activity_present = True
while activity_present:
    print("Waiting for activity")
    time.sleep(3)


# get all containers in the project instance
compose_project_containers = client.containers(all=True, filters={"label": "com.docker.compose.project=" + project_instance_id})

for contanier in compose_project_containers:
    # skip 'main' container
    main_container_name = "/" + project_instance_id + "_main_1"
    
    if container.get("Names")[0] == main_container_name
    #print(str(cont.get("Names")) + str(cont.get("Labels")))
    print(str(cont.get("Names")))
    print("----------------------------------------------------")
