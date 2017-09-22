# NetAuto
* ## Description
This git repo is a mix of some testing scripts used to get familiarize with Ansible, YAML, Jinja2, etc, these items will all be placed under a Test Script Folder, with the more "Production" type scripts and playbooks located under the LAB Scripts folder.

* ## Ansible
Run from an Ubuntu Vagrant install done on Virtual box by following Ivan Pepelnjak's step by step guide.

* ## The lab environment
A loopback connection which resides directly on Windows routes traffic from the Vagrant box to the rest of the GNS3 virtual environment which contains Cisco 7200 Series IOS Routers. The idea is to swop out one of the routers at a later stage with a XRV CSR1000, see related URL to run the XRV on Virtual Box (http://blog.alexolivan.com/cisco-csr1000-on-oracle-virtualbox-5-1/).
With the swap out I would like to automate the process in order to automatically deploy as much of the configuration from the IOS router to the XRV router.

 ##### **Easy Win**
The easier part(I hope), will be the initial deployment of the routers by using ansible playbooks which will serve as a familiarization process.

 ##### **Future Roadmap**
* Vagrant 'NetOpsWorkshop' Git repository
* Until I can figure out how to run a FortiVM image on Virtual box the idea to also run the Fortigate in the GNS3 environment is still a cloud dream, pardon the pun.
A substitute Firewall may still present itself in order to test a REST API deployment or change automation.

* ## Lab Diagram
![Lab Diagram](https://github.com/bdyzel/NetAuto/blob/master/Lab%20Layout.png?raw=true "Optional Title")
