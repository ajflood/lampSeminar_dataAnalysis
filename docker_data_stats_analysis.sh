#!/bin/bash
imageName="pythondatastats"
args="$@"

function checkFlags {
	for a  in $args; do
		#add the capability to rebuild with "-r" flag
		if [ $a = '-r' ]; then
			echo 'Rebuilding the image for you'
			build
		fi
	done
	}

function checkExists {
	#check if the image exists and if not then build one
	if [[ "$(docker images -q $imageName)" == "" ]]; then
		build
	fi
	}

function build {
# 	Actually building the docker image
	echo "Go get a coffee, I'm need to build your latex image"
	cd DockerFiles
	docker build -t $imageName -f $imageName-Dockerfile .
	cd ..
	}

function run {
	docker run -it \
			-v "$(pwd)":/data \
			--user=$(id -u) \
			--env="DISPLAY" \
			--volume="/etc/group:/etc/group:ro" \
			--volume="/etc/passwd:/etc/passwd:ro" \
			--volume="/etc/shadow:/etc/shadow:ro" \
			--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
			--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
			$imageName \
			/bin/bash
	}
	

checkFlags
checkExists
run
