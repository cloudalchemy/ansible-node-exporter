<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

Ansible Role: Node Exporter
===========================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-node-exporter.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-node-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.node_exporter-blue.svg)](https://galaxy.ansible.com/SoInteractive/node-exporter/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-node-exporter.svg)](https://github.com/SoInteractive/ansible-node-exporter/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Prometheus Node Exporter

Role supports all collectors, just list the collectors using the node_exporter_enabled_collectors variable. If the gmond collector is selected then Ganglia Gmond will be installed and started as a system service.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: yes
  become_method: sudo
  vars:
    node_exporter_enabled_collectors:
      - gmond
      - loadavg
  roles:
    - SoInteractive.node-exporter
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
