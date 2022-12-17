# SDN Network Topology

---

<aside>
👉 Project:   Interactive topology display for SDN networks. This project provides a mechanism to quickly create a Mininet topology up a GUI to interact with the network. Furthermore this software exploit RYU Northbound RestAPI to gain topology informations.

</aside>

### **Table of contents**

---

# Quick Start

---

### Prerequisites

- Ubuntu (16.04 LTS or later).
- We assume that you have already installed mininet on your PC.

### Install RYU

From your **comnetsemu** command line: 

```jsx
~$ pip install ryu
```

If you prefer to install from native **source code**:  

```jsx
~$ git clone git://github.com/osrg/ryu.git
~$ cd ryu; pip install .
```

# Usage

---

### Start up Comnetsemu VM

Open your VM ad execute **~$ ifconfig** to, check your **host Inet IP**  (something like **192.168.56.102**) then link your host terminal to comnetsemu as follow: 

```jsx
mypc@mypc:~$ ssh comnetsemu@192.168.56.102
```

Using the same procedure you are able to create any number of terminals to manage the network.

### Start RYU controller

First of all run the code below so you’ll lunch the RYU controller that is able to easy create and manage the network.  

```jsx
comnetsemu@comnetsemu:~$ ryu-manager --observe-links gui_start.py simple_switch.py
```

![ryu-manager](https://user-images.githubusercontent.com/86969245/207618082-c3d13ed5-4bc0-4b83-b69c-b019e31f18ad.png)

### Setting up the mininet topology

First step, in the terminal flush any previous topology configuration to avoid any starting problem typing:

```jsx
~$ mn -c
```

![clean_mn](https://user-images.githubusercontent.com/86969245/206305011-f9c602c5-53a8-478c-a08f-d4d470acfcea.png)


Now you can create a generic network: 

```jsx
~$ sudo mn --controller remote --topo tree,depth=3
```

Or run your custom topology:  

```jsx
~$ sudo -E python3 network.py
```


![start-topo](https://user-images.githubusercontent.com/86969245/207618145-0a2fcdf0-4b9f-4036-9339-e97e9815949e.png)


**Tips:** when you have finished remeber to exit mininet  so you will avoid any future mininet start up mistakes.

![exit_mn](https://user-images.githubusercontent.com/86969245/207617798-60bf39d8-9f45-4c9e-a6b2-20dc0e0da4bb.png)

### RYU Northbound Visualizer

Now that all is set up to check the network browse your  locahost like **192.168.56.102:8080.**

![topo_1](https://user-images.githubusercontent.com/86969245/207623889-fdd7545c-298a-49be-a28c-c8ee1e96413c.png)



 ****

It will open a Ryu visualizer page that wil show you all the switches linked between them and all the hosts linked to their own switches.  Clicking on to the different nodes you will retrieve informations related to the node that you selected.

### No topology has been istantiated



![empty-topo](https://user-images.githubusercontent.com/86969245/207617778-e6d9cd99-2be8-43b1-b022-3a2129b27b81.png)




### Generic topology

### Custom topology

![no pingall](https://user-images.githubusercontent.com/86969245/207617898-e1c6d86f-39f1-448f-a002-d24b4b894f4c.png)


### Retrieve information manually (mininet)

You can also check some infromations about the different nodes of the topology directly in mininet.

**Display nodes:**

```jsx
mininet> nodes
```
![nodes_mn](https://user-images.githubusercontent.com/86969245/207617929-aab728ff-34aa-418b-8bae-cd07b568a263.png)


**Display network links:** 

```jsx
mininet> links 
```


**Display all and list the links present in the network:** 

```jsx
mininet> net
```
![net_mn](https://user-images.githubusercontent.com/86969245/207617872-118cd8a7-4894-4b8f-9d6b-88ced847f7c5.png)

**Ping a host to a target host (ping reachability):** 

```jsx
mininet> h1 ping h2
```

**Test connection among hosts (we generate traffic among nodes):** 

```jsx
mininet> pingall
```
![pingall](https://user-images.githubusercontent.com/86969245/207617994-1e6a9f0f-849b-45c6-b1a1-185cdc8f6561.png)

![pingall_2](https://user-images.githubusercontent.com/86969245/207620574-d1ac6f80-37ca-4733-9cae-fec8e90918dc.png)


**FlowTable (dumped informations about flows):**

```jsx
mininet> dpctl dump-flows #all-flowTable-of-the-switch
mininet> dpctl dump-flows NUMBER #all-flowTable-of-the-specified-switch
```


Output before pingall command:

![dump_flow](https://user-images.githubusercontent.com/86969245/207617697-0f29c40b-be91-4169-a44b-7c23cd174a48.png)

Output after pingall command: 

![dump_flow_after_pingall](https://user-images.githubusercontent.com/86969245/207617723-9a0032f4-cdd3-41a4-84aa-ae15190b7a88.png)


### RYU RestAPI

[ryu.app.ofctl_rest](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html) provides **REST APIs** for retrieving infromation about the **switch stats** and  **update the switch stats**.  If  you want to try  open your browser and type: 

### Get Switches stats 

- Get the list of the switches connected to the controller → **localhost:8080/stats/switches**

![stat_switches](https://user-images.githubusercontent.com/86969245/207618175-d52574c4-b414-4cb6-a12d-c67958725891.png)

- Get the list of the  hosts → **localhost:8080/v1.0/topology/hosts**

![topo_host ](https://user-images.githubusercontent.com/86969245/207618202-9e7f80f0-7981-4c20-b8dd-be62b22f08bf.png)

- Get the links of the topology → **localhost:8080/v1.0/topology/links**

![topo_links](https://user-images.githubusercontent.com/86969245/207618247-e782b385-ac4b-4f04-9271-15217e205b7c.png)



### Update the switch stats

- Delete all matching flow entry of the switch → localhost:8080/stats/flowentry/delete



![delete_cmd](https://user-images.githubusercontent.com/86969245/206302361-13a7edbd-dd9d-4465-b6fa-c2d0e9d82e78.png)


![net_stats_after_del](https://user-images.githubusercontent.com/86969245/206302445-4696582f-0fc8-43c3-a768-f7ec12267917.png)

![pingall_no_del](https://user-images.githubusercontent.com/86969245/206302489-d8ea6ebe-23ae-4c11-a273-fb3398c799ee.png)


- Delete all flow entries  → localhost:8080/stats/flowentry/clear/<dpid>

# Documentation

---

For more informations about **Mininet and RYU** follow those links:

 

- **Mininet** → [http://mininet.org/walkthrough/](http://mininet.org/walkthrough/)
- **RYU documentation** → [https://ryu.readthedocs.io/en/latest/](https://ryu.readthedocs.io/en/latest/)
- **RYU RestAPI** → [https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html)

# Credits

---

Hlaj Alessandro 

Dauti Andriano 

Bonvecchio Francesco 
