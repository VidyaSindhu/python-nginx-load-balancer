# python-nginx-load-balancer

the conf will be used by nginx, to use this, follow the instructions
1. Open the nginx.conf file in the directory in /etc/nginx/ using admin access
2. paste the directory path of the python.conf file inside the http {} section
3. run 3 different servers using the specified port in python.conf file.
4. restart the nginx, and open the "http://localhost/basic" and you will see the process ids of the different running servers
