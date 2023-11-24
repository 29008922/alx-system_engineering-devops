# A puppet manifest installing flask v2.1.0 which is a package from pip3.

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
