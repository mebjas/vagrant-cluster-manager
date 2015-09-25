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
	"boxID": "ubuntu_trusty64_12",
	"box": "ubuntu/trusty64",
	"IP": "192.168.33.12",
	"hostname": "ubuntu_trusty64_12_1.example.com",
	"message": "started VM ubuntu_trusty64_12_1 successfully"
}

REQUEST to STOP a VM
{
	"command": "stop",
	"vmID": "ubuntu_trusty64_12_1"
}

RESPONSE for STOPPING a VM
{
	"error": false,
	"vmID": "ubuntu_trusty64_12_1",
	"boxID": "ubuntu_trusty64_12",
	"message": "shutdown VM ubuntu_trusty64_12_1 successfully"
}
```

In a similar fashion you can query information about any no of `boxes` or `VMs` at any time. It will send all required information about a VM in JSON format. 

```json
Request info on all active VMS
{
	"command": "info",
	"subcommand": "VM all"
}

Response
{
	"error": "false",
	"message": "listed information on 3 active VMs",
	"VMS": [
		{
			"vmID": "ubuntu_trusty64_12_1",
			"boxID": "ubuntu_trusty64_12",
			"box": "ubuntu/trusty64",
			"IP": "192.168.33.12",
			"hostname": "ubuntu_trusty64_12_1.example.com"
		},
		{
			"vmID": "ubuntu_trusty64_12_2",
			"boxID": "ubuntu_trusty64_12",
			"box": "ubuntu/trusty64",
			"IP": "192.168.33.33",
			"hostname": "ubuntu_trusty64_12_2.example.com"
		},
		{
			"vmID": "ubuntu_presise64_3_1",
			"boxID": "ubuntu_presise64_3",
			"box": "ubuntu/presise64",
			"IP": "192.168.33.15",
			"hostname": "ubuntu_presise64_3_1.example.com"
		}
	]
}


You can also `destroy` or `halt` or `shutdown` all active VMs at once. Just send `destroy all` command or similar ones.
```

###TODO
 - Implement this daemon first
 - Add complete testing for this daemon
 - Create a python library, to programatically deal with this
 - Create a php library to programatically deal with this
