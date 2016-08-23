#!/urs/bin/python
####   This will hopefully edit the config file for Nginx to allow a user to add and delete subdomains
####   on a shared webserver.   Its a work in progress so don't judge.   Currently its only set for one 
####   user to use.  Utimately I'd like it to read the name of the logged in user and pick the proper
####   nginx file based on the logged in user.   I'll have to redo the naming convention on the server
####   before this can be rolled into production.   

import sys
import fileinput
import os

#nginx config file name
filename = "/home/dan/scripts-and-other-files/admin/testing/morris.com"

def start():
  print "What subdomain and domain would you like to work with? sub.domain.tld?"
  x = raw_input("> ")
  print x.split(".")[0]
  print x.split(".")[1],"woot ",x.split(".")[2]
  
def add_domain():
  print "What is the name of the subdomain you'd like to add? "
  sub = raw_input("> ")
  target = open(filename, 'a')
  target.write( """#%s.sasson-morris.com
server {         
	listen 80; # default_server;
	listen [::]:80;
	root /home/kent/public_html/sasson-morris.com/%s/;
	index index.php index.html index.htm;
	# Make site accessible from http://localhost/
	server_name %s.sasson-morris.com;
	location / {
		try_files $uri $uri/ =404;
	}
	error_page 404 /404.html;
	error_page 500 502 503 504 /50x.html;
	location = /50x.html {
		root /var/www/;
	}
	location ~ \.php$ {
		try_files $uri =404;
		fastcgi_split_path_info ^(.+\.php)(/.+)$;
		fastcgi_pass unix:/var/run/php5-fpm.sock;
		fastcgi_index index.php;
		include fastcgi_params;
	}
	location ~ /\.ht {
		deny all;
	}
}
  """ % (sub, sub, sub))
  target.write("\n")
  print "the server block for %s.sasson-morris.com has been added to %s" % (sub, filename)
  target.close()

def linecount(file):
  with open(file) as F: 
    for j,l in enumerate(F):
      pass
    return j + 1 

def del_sub():
  print "Which subdomain would you like to remove?"
  sub = raw_input('> ')
  newfile = "%s.bak" % filename
  os.rename(filename, newfile)
  with open(newfile) as f1:
    with open(filename, 'a') as f2:
      Lines = f1.readlines()
      count = linecount(newfile)
      i = 0
      while i < count:
        if Lines[i].strip() != ("#%s.sasson-morris.com" % sub):
          j = i 
          while j < (i+28):
            f2.write(Lines[j])
            j += 1 
          i = i + 28
        else:
          print "Skipping %s.sasson-morris.com" % sub
          i = i + 28


print ("Hello world")
start()
#getsub()
#add_domain()
#del_sub()

