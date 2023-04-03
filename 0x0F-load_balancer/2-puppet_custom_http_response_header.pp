# Creating a custom HTTP header response, with Puppet
# 	The name of the custom HTTP header must be X-Served-By
# 	The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'command':
  command  => 'apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
