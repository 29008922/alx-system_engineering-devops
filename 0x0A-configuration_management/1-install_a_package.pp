# A puppet manifest installing flask v2.1.0 which is a package from pip3.
# Am also specifying the version of flask to install using the ensure attribute

package { 'python3-pip':
  ensure => present,
}
exec { 'install flask':
  command => 'pip3 install flask==2.1.0',
  path => '/usr/bin',
}
