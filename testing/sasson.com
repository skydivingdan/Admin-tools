server {         #trump.sasson-morris.com
	listen 80; # default_server;
	listen [::]:80;
	root /home/kent/public_html/sasson-morris.com/trump/;
	index index.php index.html index.htm;
	server_name trump.sasson-morris.com;
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
server {         #firewater.sasson-morris.com
	listen 80; # default_server;
	listen [::]:80;
	root /home/kent/public_html/sasson-morris.com/trump/;
	index index.php index.html index.htm;
	server_name trump.sasson-morris.com;
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
