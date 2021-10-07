# enable holberton user to open a file without error

# increas hard limt
exec { 'increase-hard-limt':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 40000/g'"
}

# increase soft limit
exec { 'increase-soft-limit':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 40000/g'"
}
