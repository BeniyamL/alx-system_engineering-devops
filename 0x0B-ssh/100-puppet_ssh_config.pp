# configure SSH file to log without password and manage using puppet
include stdlib

file_line { 'log without pasword':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication'
}

file_line { 'identify file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile'
}

