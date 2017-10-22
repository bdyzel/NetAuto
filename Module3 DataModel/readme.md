# **Module 3**

### **Overview**

The function of the playbooks will be to build data models for the BGP environment used on both the WAN and CAMPUS infrastructure.
(*the public nodes do not form part of the playbooks. But there are references to the public nodes because of a possible use case to include the Public Nodes when initial deployment is done and just maybe to create reports for verification purposes*)

The lab diagram is there to give a High level visual representation of the Infrastructure Model.
![Module 3 Lab Diagram](https://github.com/bdyzel/NetAuto/blob/master/Lab%20LayoutModule3.png?raw=true "Optional Title")



## **Data Model**
### **Infrastructure Model**
The infrastructure model(*``cloth.yml``*) provides a list of the following;
* **nodes**    = 'name'=Node Name, 'mgmta'=Management IP(ansible access IP), 'mgmtb'=Router ID(loopback interface), and 'ntype'=Node Type to indicate which area the node is associated with
* **asn**      = The BGP ASN number and which nodes are associated with which ASN.
* **services** = The common services
* **intbgp**  = a list of iBGP links; each link has a east and west node, east_as and west_as, east_ip and west_ip IP addresses and east_port and west_port interfaces. iBGP is configured on these links
* **extbgp**  = a list of eBGP links; each link has a east and west node, east_as and west_as, east_ip and west_ip IP addresses and east_port and west_port interfaces. eBGP is configured on these links
* **_Future requirement_**
* **igp**   = a list of IGP links; each link has a east and west node, east_ip and west_ip IP addresses and east_port and west_port interfaces. EIGRP is configured on these links

### **Services**
#### Automatically create data model
The ``cdmod.yml`` (*Create Data Model*) playbook transforms the data (*``cloth.yml``*) into per-node, and per-area data models (*stored in ``nodes.yml``*).

**_Future requirement_**
* **Address Range Prefix list**
The ``prefixupd.yml`` playbook transforms the data () into per-node data models (stored in ``.yml``).

  * **configs**    - create the configuration files in ``dmconfigs`` directory
  * **_Future requirement_**
       * **deploy**     - deploy the configuration files from the ``dmconfigs`` directory to the nodes
  * **_Future requirement_**
       * **verify**     - Self explanatory

  * Playbooks in the bgp, eigrp and vpnv4 directories reference the relevant data models from ``nodes.yml``, this will create device configurations which can be referenced for per-node deployment.

  * **_Future requirement_** After each deployment a verification is done to confirm adjacencies and newly added prefixes.
