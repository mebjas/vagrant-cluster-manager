# vagrant-cluster-manager
Tool to manage Virtual Machines programatically using vagrant. It starts as a daemon, and listen to a certain port, which is `12121` by default. You can send it a variety of command via socket like

```json
{
	"command": "create",
	"box": "ubuntu/trusty64",
	"files": [],
	"puppet": [],
	"shell": [],
	"network": "private",
	"hostname": "dynamic"
}
```

And this will create a box and return informaiton in format
```json
{
	"error": false,
	"boxID": "ubuntu_trusty64_12"
}
```
Now to start a VM at any instant send command
```json
REQUEST to START a VM
{
	"command": "start",
	"boxID": "ubuntu_trusty64_12"
}


RESPONSE for STARTING a VM
{
	"error": false,
	"vmID": "ubuntu_trusty64_12_1",
	"boxID": "ubuntu_trusty64_12"
}

REQUEST to STOP a VM
{
	"command": "stop",
	"vmID": "ubuntu_trusty64_12_1"
}

RESPONSE for STOPPING a VM
{
	"error": false
}
```

In a similar fashion you can query information about any no of `boxes` or `VMs` at any time. It will send all required information about a VM in JSON format. 

###TODO
 - Implement this daemon first
 - Add complete testing for this daemon
 - Create a python library, to programatically deal with this
 - Create a php library to programatically deal with this
