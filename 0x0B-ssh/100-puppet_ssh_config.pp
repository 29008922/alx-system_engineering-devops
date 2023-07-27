#!/usr/bin/env bash
#configuration of file using puppet


file { 'etc/ssh/ssh_config':
	ensure => pesent,

content => "

	#ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
