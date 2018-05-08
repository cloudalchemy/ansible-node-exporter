<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

# Ansible Role: node exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-node-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-node-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.node_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/node-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-node-exporter.svg)](https://github.com/cloudalchemy/ansible-node-exporter/tags)
[![IRC](https://img.shields.io/badge/chat-on%20freenode-blue.svg)](http://webchat.freenode.net/?channels=cloudalchemy)

## Description

Deploy prometheus [node exporter](https://github.com/prometheus/node_exporter) using ansible.

## Requirements

- Ansible >= 2.3

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `node_exporter_version` | 0.15.2 | Node exporter package version |
| `node_exporter_web_listen_address` | "0.0.0.0:9100" | Address on which node exporter will listen |
| `node_exporter_enabled_collectors` | [ conntrack, diskstats, entropy, filefd, filesystem, hwmon, loadavg, mdadm, meminfo, netdev, netstat, stat, textfile, time, vmstat, systemd, ntp ] | List of enabled collectors |
| `node_exporter_disabled_collectors` | [ logind ] | List of disabled collectors | 

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  become: yes
  roles:
    - cloudalchemy.node-exporter
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule>2.13.0' docker 'testinfra>=1.7.0' jmespath
```
This should be similar to one listed in `.travis.yml` file in `install` section.
After installing test suit you can run test by running
```sh
molecule test --all
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
