#Container MVP

A miniminal viable product for running containers in production. This repo contains the contents of the 
dockerfile and demo app which visually demonstrates a multihost, multi-AZ, multicontainer solution with the 
ability to interact with an external database as defined by a config file. 

## Rancher
The dockerfile defined here will need to be used in conjuction with rancher-compose. Rancher compose will allow
you to interact with rancher through the cli. [Grab rancher-compose from their github repo](https://github.com/rancher/rancher-compose).
Rancher will provide service discovery, container orchestration, an orchestration platform, and a plethora of other services. 

## Usage
Define an env file as templated by env-example, or simply make a copy of env-example.
`cp env-example env`

Modify the env file with valid values.

Run the rancher-compose command to spin up a stack of containers. 

```bash
# Note as a Prereq to using rancher-compose you should set a couple of env vars
# Set the url that Rancher is on
$ export RANCHER_URL=http://rancher.maxwell-ondemand.com:8080
# Set the access key, i.e. username
$ export RANCHER_ACCESS_KEY=<username_of_key>
# Set the secret key, i.e. password
$ export RANCHER_SECRET_KEY=<password_of_key>

# Creating and starting a service with environment variables and picking a stack
$ rancher-compose -f docker-compose.yml -p mvp up -d
# To change the scale of an existing service
$ rancher-compose -p mvp scale web=5

```

