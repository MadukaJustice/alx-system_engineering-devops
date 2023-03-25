# kills a process named 'killmenow' using 'exec' and 'pkill'

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow',
}
