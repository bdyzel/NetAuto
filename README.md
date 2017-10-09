# NetAuto
* ## Description
This git repo is a mix of some testing scripts used to get familiarize with Ansible, YAML, Jinja2, etc, these items will all be placed under a Test Script Folder, with the more "Production" type scripts and playbooks located under the LAB Scripts folder.

* ## Ansible
Run from an Ubuntu Vagrant install done on Virtual box by following Ivan Pepelnjak's step by step guide.

* ## The lab environment
A loopback connection which resides directly on Windows routes traffic from the Vagrant box to the rest of the GNS3 virtual environment which contains Cisco 7200 Series IOS Routers. The idea is to swop out one of the routers at a later stage with a XRV CSR1000, see related URL to run the XRV on Virtual Box with GNS3 (https://www.youtube.com/watch?v=hkRZRAU7n7E&t=0s).
With the swap out I would like to automate the process in order to automatically deploy as much of the configuration from the IOS router to the XRV router.
 

 ##### **Future Roadmap**
* -new- Gather sufficient 'facts' from the devices to build dictionaries of each devices automatically. (For specific commands this doesn't seem possible yet, for instance; The CSR API configuration will need to be captured as a configuration set and deployed via CLI instead well known Ansible or Napalm library commands)
* -new- Ensure Idempotency checks are in place for deployments
* -new- Test the a deployment of the existing devices via playbooks
* -new- Add additional routers and automatically deploy BGP either using variable adjustments or provide an end state and deploy the configuration to match the end state.
* -new- Verify the end state of each newly deployed device
* -new- Use end state dictionaries to test routes received and advertised via BGP.
* -new- Use or build the following:
    * -new- custom templates
    * -new- custom filters
    * -new- custom libraries (TextFSM, Network2Code, etc)

 ##### **Module 1**
* This was used just to build the lab

 ##### **Module 2**
* Creating a reporting system that will;
   * Provide certain Ansible facts for all devices on the lab environment.   
   * Get BGP specific Routing Configuration.   
   * Get VRF Name of devices if VRF is being used on a Device. 
     * Additional consideration may be required for when there is more than one VRF on a device, this functionality is not yet built in or required for this lab using self built checks.
  * Get results of BGP show commands for the routing table and summary of the BGP relationships  
  * -new- Deploy minor config changes
  * -new- Get Results from CSR Router Rest API
  * -new- Gather facts from all Routers using Napalm.
  
 ##### **Module 3**
* TBC;
   * Deeper dive into Napalm functionality 

* ## Lab Diagram
![Lab Diagram](https://github.com/bdyzel/NetAuto/blob/master/Lab%20Layout.png?raw=true "Optional Title")
