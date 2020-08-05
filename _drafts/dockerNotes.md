'''
$ docker pull ubuntu:18.04
$ docker run -it ubuntu:18.04 bash
$ docker images
$ docker tag ubuntu:latest myubuntu:latest
$ docker [image] inspect ubuntu:18.04
$ docker history ubuntu:18.04
$ docker search ——filter=is-official=true nginx
$ docker rmi myubuntu:latest
$ docker ps -a
$ docker rm a21c0840213e
$ docker image prune -f
$ docker [container] commit -m "Added a new file" -a "Docker Newbee" a925cb40b3f0 test:0.1
OPENVZ模板的下载地址为http://openvz.org/Download/templates/precreated
$ cat ubuntu-18.04-x86_64-minimal.tar.gz | docker import - ubuntu:18.04
$ docker [image] build -t python:3 .
$ docker save -o ubuntu_18.04.tar ubuntu:18.04
$ docker load -i ubuntu_18.04.tar
$ docker push user/test:latest
$ docker create -it ubuntu:latest
$ docker start af
$ docker run ubuntu /bin/echo 'Hello world'
$ docker run -it ubuntu:18.04 /bin/bash
$ docker logs ce554267d7a4
$ docker pause test
$ docker stop ce5
$ docker ps -qa
$ docker restart ce554267d7a4
$ docker attach nostalgic_hypatia
$ docker exec -it 243c32535da7 /bin/bash
$ docker rm -f 2ae
$ docker export -o test_for_run.tar ce5
$ docker export e81 >test_for_stop.tar
$ docker import test_for_run.tar - test/ubuntu:v1.0
$ docker container inspect test
$ docker top test
$ docker [container] cp data test:/tmp/
$ docker container diff test
$ docker container port test
$ docker update ——cpu-quota 1000000 test
'''