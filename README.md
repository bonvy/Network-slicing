# SDN Network Topology

---

<aside>
👉 Project**:   Interactive topology display for SDN networks. This project provides a mechanism to quickly create a Mininet topology up a GUI to interact with the network. Furthermore this software exploit RYU Northbound RestAPI to gain topology informations.**

</aside>

### **Table of contents**

---

# Quick Start

---

### **Prerequisites**

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

Open your VM ad execute **~$ ifconfig** to, check your host **Inet IP  (**something like **192.168.56.102)** then link your host terminal to comnetsemu as follow: 

```jsx
mypc@mypc:~$ ssh comnetsemu@192.168.56.102
```

Using the same procedure you cann create any number of terminals to manage the network.

### Start RYU controller

First of all run the code below so you’ll lunch the RYU controller that is able to easy create and manage the network.  

```jsx
comnetsemu@comnetsemu:~$ ryu-manager --observe-links gui_start.py simple_switch.py
```

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled.png)

### Setting up the mininet topology

First step, in the terminal flush any previous topology configuration to avoid any problem typing:

```jsx
~$ mn -c
```

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%201.png)

Now you can create a generic network: 

```jsx
~$ sudo mn --controller remote --topo tree,depth=3
```

Or run your custom topology:  

```jsx
~$ sudo -E python3 network.py
```

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%202.png)

**Tips:** when you have finished remeber to exit mininet  so you will avoid any future mininet start up mistakes .

### RYU Northbound Visualizer

Now that all is set up to check the network browse your  locahost like **192.168.56.102:8080.**

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%203.png)

 ****

It will open a Ryu visualizer page that wil show you all the switches linked between them and all the hosts linked to their own switches.  Clicking on to the different nodes you will retrieve informations related to the node that you selected.

### No topology has been istantiated

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%204.png)

### Generic topology

### Custom topology

![B6593DCA8EB144F9A40F6F0CFD6957AC.png](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/B6593DCA8EB144F9A40F6F0CFD6957AC.png)

### Retrieve information manually (mininet)

You can also check some infromations about the different nodes of the topology directly in mininet.

**Display nodes:**

```jsx
mininet> nodes
```

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%205.png)

**Display network links:** 

```jsx
mininet> links 
```

**Display all and list the links in the network:** 

```jsx
mininet> net
```

![Untitled](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/Untitled%206.png)

**Ping a host to a target host (ping reachability):** 

```jsx
mininet> h1 ping h2
```

**Test connection among hosts (we generate traffic among nodes):** 

```jsx
mininet> pingall
```

![60C018DE4FCB4FDC864FEFA69CC9F0A6.png](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/60C018DE4FCB4FDC864FEFA69CC9F0A6.png)

**FlowTable (dumped informations about flows):**

```jsx
mininet> dpctl dump-flows #all-flowTable-of-the-switch
mininet> dpctl dump-flows NUMBER #all-flowTable-of-the-specified-switch
```

![EA7C4B01BA8540DF963C60C7025CE0EE.png](SDN%20Network%20Topology%20e9016259d57445db897d422bf7ba2acd/EA7C4B01BA8540DF963C60C7025CE0EE.png)

### RYU RestAPI

[**ryu.app.ofctl_rest](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html)** provides **REST APIs** for retrieving infromation about the **switch stats** and  **update the switch stats**.  If  you want to try  open your browser and type: 

### Get Switches stats (aggiungere immagini esempio)

- Get the list of the switches connected to the controller → **localhost:8080/stats/switches**
- Get the list of the  hosts → **localhost:8080/stats/host**
- Get the links of the topology → loaclhost:8080/stats/links
- Get all flows stats of the switch which specified with Datapath ID → **localhost:8080/stats/flow/<dpid>**
- Get all switch table stats specified with Datapath ID → **localhost:8080/stats/table/<dpid>**
- Get ports stats of the switch which specified with Datapath ID → **localhost:8080/stats/port/<dpid>**

### Update the switch stats

- Add a flow entry to the switch → localhost:8080/stats/flowentry/add
- Delete all matching flow entry of the switch → localhost:8080/stats/flowentry/delete
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
