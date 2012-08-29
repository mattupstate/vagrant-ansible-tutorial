#!/bin/sh

ansible-playbook devops/deploy.yml -i devops/hosts --private-key=$HOME/.vagrant.d/insecure_private_key
