# **Module 3**

### **Overview**

The function of the playbooks will be to deploy and update route-map filters on the BGP environments for both the WAN and CAMPUS infrastructure.
(*the public nodes do not form part of the playbooks. If references to the public nodes are seen it's because of a possible use case to include the Public Nodes in the playbooks for verification reports*)

The lab diagram is there to give a High level visual representation of the Infrastructure Model.
![Module 3 Lab Diagram](https://github.com/bdyzel/NetAuto/blob/master/Lab%20LayoutModule3.png?raw=true "Optional Title")



## **Data Model**
### **Infrastructure Model**
The infrastructure model(*``cloth.yml``*) provides a list of the following;
* **nodes**    = Nodes Names and what Router ID, VRF, and Management IP are associated with each node
* **asn**      = The BGP ASN number and which nodes are associated with which ASN.
* **services** = The common services
* **ibgpcon**  = a list of iBGP links; each link has a east and west node, east_ip and west_ip IP addresses and east_port and west_port interfaces. iBGP is configured on these links
* **ebgpcon**  = a list of eBGP links; each link has a east and west node, east_ip and west_ip IP addresses and east_port and west_port interfaces. eBGP is configured on these links
* **igpcon**   = a list of IGP links; each link has a east and west node, east_ip and west_ip IP addresses and east_port and west_port interfaces. EIGRP is configured on these links

### **Services**
#### Automatically create data model
The ``cdmod.yml`` (*Create Data Model*) playbook transforms the data (described in more details below) into per-node data models (*stored in ``nodes.yml``*) that are easier to work with when generating device configurations.

* **Address Range Prefix list**
The ``prefixupd.yml`` playbook transforms these data models (described in more details below) into per-node data models (stored in ``nodes.yml``) that are easier to work with when generating device configurations.

  * **configs**     - create the configuration files in ``dmconfigs`` directory
  * **deploy**     - deploy the configuration files from the ``dmconfigs`` directory to the nodes
  * **verify**     - Self explanatory

Playbooks in the bgp, eigrp and vpnv4 directories reference the relevant data models from ``nodes.yml``, this will create device configurations which is then deployed per-node.
After each deployment a verification is done to confirm adjacencies and newly added prefixes.
