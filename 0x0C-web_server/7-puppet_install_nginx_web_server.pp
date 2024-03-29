# configure the server with Puppet and manage it
# Nginx should be listening on port 80
# must return the page containing the string Holberton School
# it must redirect to 301 moved permanently
include stdlib

$alx = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$new_str = '\trewrite ^/redirect_me/$ ${alx} permanent;'

exec {'restart':
  command => 'usr/sbin/service nginx restart',
  require => Package['nginx']
}

exec {'update':
  command  => 'usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Holberton School',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { '301 redirction':
  ensure   => 'present',
  after    => 'server_name _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $new_str,
  notify   => Exec['restart'],
  require  => File['/var/www/html/index.html']
}
