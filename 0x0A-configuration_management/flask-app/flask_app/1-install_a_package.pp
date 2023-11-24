#
package { 'python3-pip':
  ensure => present,
}

exec { 'install flask':
  command => 'pip3 install flask==2.1.0',
  path => '/usr/bin',
}
