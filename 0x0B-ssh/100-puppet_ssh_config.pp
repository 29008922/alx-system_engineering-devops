#!/usr/bin/env bash
#writting a script using puppet to configure files


file { 'etc/ssh/ssh_config':
	ensure => present,

content => "
	
	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentification no
	",
}

