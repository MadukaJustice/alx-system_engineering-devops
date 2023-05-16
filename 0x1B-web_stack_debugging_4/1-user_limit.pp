# https://www.geeksforgeeks.org/how-to-change-the-number-of-open-file-limit-in-linux/

exec { 'increase open files limit':
  provider => shell,
  command  => 'sed -i -e "s/5/21000/g" -e "s/4/16000/g" /etc/security/limits.conf',
}
