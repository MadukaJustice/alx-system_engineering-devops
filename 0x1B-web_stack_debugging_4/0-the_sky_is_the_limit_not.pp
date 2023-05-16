# https://serverfault.com/questions/1003364/nginx-500-24-too-many-open-files

exec { 'increase request limit':
  provider => shell,
  command  => 'sed -i "s/15/4069/g" /etc/default/nginx | service nginx restart',
}
