#Kill a program

exec { 'pkill':
path    => '/usr/bin:/usr/sbin:/bin',
command => 'pkill -f killmenow'
}
