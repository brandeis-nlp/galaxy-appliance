#!/bin/bash
set -eu

# Since the .tgz packages are not kept in source control this script can be used
# to download any required packages.

# The script is expected to be called from the Makefile which will have set
# the PACKAGE_LIST environment variable.

#SERVER=http://www.anc.org/downloads/docker
SERVER=http://downloads.lappsgrid.org

if [ ! -d packages ] ; then
	mkdir packages
fi

cd packages

case "$1" in
	download)
		for package in $PACKAGE_LIST ; do
			wget $SERVER/$package.tgz
		done
		;;
	update)
		for package in $PACKAGE_LIST ; do
			if [ -e $package.tgz ] ; then
				echo "Skipping $package"
			else
				wget $SERVER/$package.tgz
			fi
		done
		;;
	clean)
		rm *.tgz
		;;
	*)
		echo "Unrecognized command $1"
		;;
esac


