# Project 4
## Part 2 - Setup Load Balancing TODOs

Setup the following and add documentation or screenshots to your `README.md` file as specified.

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs.
   - Description of how file is configured
   - I edited the file "/etc/hosts". The file looks like the following:
   ![Hosts](images/Hosts.png)

2. Document how to SSH in between the systems utilizing their private IPs.
    - To SSH into both serbers from the proxy server, you have to use the command "ssh -i privatekey nameofserver". In my case, I used "ssh -i CEG3120-aws.pem webserv1" and "ssh -i CEG3120-aws.pem webserv2". Once you have those names inside the hosts file, you no longer have to use the IP addresses for the servers.
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
        - /etc/haproxy/haproxy.cfg
     - What configuration(s) were set (if any)
   ![Haproxy](images/Haproxy.png)
     - How to restart the service after a configuration change
        - sudo systemctl restart haproxy

4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
         - index.html was modified on both webservers at the location of /var/www/html
     - What configuration(s) were set (if any)
         - No configurations were set
     - Where site content files were located (and why)
         - The files were located in /var/www/html and under the file named index.html. They are located there because that is the default location for apache2.
     - How to restart the service after a configuration change
         - sudo systemctl restart apache2
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   ![Server1](images/Server1.png)
   - one screenshot that shows content from "server 2"
   ![Server2](images/Server2.png)
6. (Optional) - link to your proxy so I can click it.
   - 35.170.132.254

