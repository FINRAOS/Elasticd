# Elasticd 

### Objective
The goal is to have the frontends communicate with backends directly by using ip address and not DNS in cloud environments.  This will remove the unnecessary components in-between and the associated overhead.  

### Why Elasticd?
*	AWS is very dynamic in nature.  A lot of their services start with ‘E’ which stands for elastic
  *	IP addresses change all the time
  *	The number of server performing a task may increase or decrease at anytime
*	Industry standard technologies have not yet advanced to operating optimally in this dynamic AWS environment
*	A lot of these technologies cache DNS lookups for performance.  This is great in a static environment but a burden in AWS
*	A few technologies used at FINRA that require significant additional effort and workarounds:
  *	Varnish
  *	Apache
  *	Nginx (special configuration required)
*	Difficult to automatically configure frontends to know about the backends without using DNS
*	Requires additional components between the front ends and back ends
  *	More components mean more overhead in maintenance, testing, and development
  *	More components mean more failure points 

### Solution Description
Write a light weight application that informs the frontends of the backends allowing them to communicate directly using ip addresses.  
#### Features
*	Pluggable – ability to extend and component to suit your needs
*	Frontend agnostic 
  *	Provide additional implementations for different frontend technologies (Varnish, Nginx, etc)
*	Backend agnostic
  *	Elasticd only needs a way to find the ip address of the backend
*	Cloud agnostic
  *	Here at FINRA we use AWS but the resource locator can be extended for other cloud offerings

  ![Alt text](https://github.com/FINRAOS/Elasticd/blob/master/docs/img/elasticd.png?raw=true)

