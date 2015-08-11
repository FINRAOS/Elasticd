# ElasticD for direct communication between frotends and backends 

##Table Of Contents
- [Objectives](#1)
- [Purpose](#2)
- [Solution](#3)
- [Features](#4)
- [Setup](#5)- 

### Objective <a name="1"></a>
The goal is to have frontends communicate directly with backends by using IP addresses instead of DNS in cloud environments. This will remove the unnecessary components in-between the two and associated overhead. 

### Why ElasticD? <a name="2"></a>
*	AWS is very dynamic in nature. A lot of their services start with ‘E’ for elastic. 
  *	IP addresses change all the time, allowing more flexibility.
  *	The number of server performing a task may increase or decrease at any time.
*	So far, standard industry technologies don’t operate optimally in this dynamic environment.
 * Many cache DNS lookups for performance. This is great in a static environment but a burden in AWS.
*	A few technologies used at FINRA required significant additional effort and workarounds included: 
  *	Varnish
  *	Apache
  *	Nginx (special configuration required)
*	It was difficult to automatically configure frontends and know about the backends without using DNS.
*	This required additional components between the front ends and back ends. 
  *	More components meant more overhead in maintenance, testing, and development.
  *	More components meant more failure points.

### Solution <a name="3"></a>
Create a light weight application that informs the frontends of the backends, allowing them to communicate directly with IP addresses.  

#### Features <a name="4"></a>
*	Pluggable
  *	 It's able to extend components to suit your needs.
*	Frontend agnostic 
  *	Additional implementations are available for different frontend technologies (Varnish, Nginx, etc).
*	Backend agnostic
  *	ElasticD only needs a way to find the backend's IP address.
*	Cloud agnostic
  *	At FINRA, we use AWS but the resource locator can be extended for other cloud offerings.

  ![Alt text](https://github.com/FINRAOS/Elasticd/blob/master/docs/img/elasticd.png?raw=true)

##Setup <a name="5"></a>
This section will walk you through how to start up the ElasticD services
You will need to install the following
*   Pip
*   Flask
*   Jinja2
*   boto
*   apscheduler

After that you can run 
python bin/run.py
or
python test/test_driver.py


