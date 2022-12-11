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

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled.png)

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

![custom_topo_run](https://user-images.githubusercontent.com/86969245/206305155-ed3e9046-0fa4-4fca-a22f-c147d86ed475.png)


**Tips:** when you have finished remeber to exit mininet  so you will avoid any future mininet start up mistakes.

![mn_exit](https://user-images.githubusercontent.com/86969245/206303945-87d92c8e-10ba-4eb2-b7f3-f3668bc2a157.png)

### RYU Northbound Visualizer

Now that all is set up to check the network browse your  locahost like **192.168.56.102:8080.**

![tp_1_viewer](https://user-images.githubusercontent.com/86969245/206303712-d6f9a4dd-2cf9-4d02-8bcc-e0214c1ee4a4.png)


 ****

It will open a Ryu visualizer page that wil show you all the switches linked between them and all the hosts linked to their own switches.  Clicking on to the different nodes you will retrieve informations related to the node that you selected.

### No topology has been istantiated


![tp_vuota](https://user-images.githubusercontent.com/86969245/206303624-b1373de2-b722-49a9-8332-1e0c4dee7a00.png)




### Generic topology

### Custom topology

![topology](https://user-images.githubusercontent.com/86969245/206303535-740e8b18-514f-4fd6-998b-da85b57eab93.png)


### Retrieve information manually (mininet)

You can also check some infromations about the different nodes of the topology directly in mininet.

**Display nodes:**

```jsx
mininet> nodes
```
![mn_nodes](https://user-images.githubusercontent.com/86969245/206305285-863eea24-05bc-4cb5-85ea-517b6e3dcfa1.png)


**Display network links:** 

```jsx
mininet> links 
```


**Display all and list the links present in the network:** 

```jsx
mininet> net
```
![net_mn](https://user-images.githubusercontent.com/86969245/206305383-3a46238a-c6f6-472e-a4b9-9b9ab96b6fd0.png)


**Ping a host to a target host (ping reachability):** 

```jsx
mininet> h1 ping h2
```

**Test connection among hosts (we generate traffic among nodes):** 

```jsx
mininet> pingall
```

![pingall_out1](https://user-images.githubusercontent.com/86969245/206302672-418462f1-049b-4454-b98b-d7eac532b862.png)

![pingall_out2](https://user-images.githubusercontent.com/86969245/206302708-680bc367-b387-42c6-8ae2-87effe15aa5d.png)



**FlowTable (dumped informations about flows):**

```jsx
mininet> dpctl dump-flows #all-flowTable-of-the-switch
mininet> dpctl dump-flows NUMBER #all-flowTable-of-the-specified-switch
```
![dump_flow](https://user-images.githubusercontent.com/86969245/206302864-75c853fd-c315-43a2-af27-5276d0860d33.png)



### RYU RestAPI

[ryu.app.ofctl_rest](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html) provides **REST APIs** for retrieving infromation about the **switch stats** and  **update the switch stats**.  If  you want to try  open your browser and type: 

### Get Switches stats (aggiungere immagini esempio)

- Get the list of the switches connected to the controller → **localhost:8080/stats/switches**

![switches](https://user-images.githubusercontent.com/86969245/206301900-4e2bcc70-36a6-4f52-a338-df6ddc600500.png)

- Get the list of the  hosts → **localhost:8080/v1.0/topology/hosts**

![hosts](https://user-images.githubusercontent.com/86969245/206301606-3c382930-59e2-41e3-99e3-a49985763fee.png)

- Get the links of the topology → **loaclhost:8080/v1.0/topology/links**

![links ](https://user-images.githubusercontent.com/86969245/206302046-a7450e48-f5f8-48f2-882b-c39e3d152e86.png)


- Get all flows stats of the switch which specified with Datapath ID → **localhost:8080/stats/flow/<dpid>**
- Get all switch table stats specified with Datapath ID → **localhost:8080/stats/table/<dpid>**
- Get ports stats of the switch which specified with Datapath ID → **localhost:8080/stats/port/<dpid>**

### Update the switch stats

- Add a flow entry to the switch → localhost:8080/stats/flowentry/add
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

Hlaj Alessandro - Mat. 218549 

Dauti Andriano - Mat. 21…

Bonvecchio Francesco - Mat. 21 ….
