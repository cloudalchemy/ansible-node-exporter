prometheus-node-exporter
=====================================

Install Prometheus Node Exporter -  https://github.com/prometheus/node_exporter . Tested with Ubuntu 16.04

Requirements
------------

None

Role Variables
--------------

See defaults/main.yml. This role supports all collectors, just list the collectors using the prometheus_node_exporter_enabled_collectors variable. If the gmond collector is selected then Ganglia Gmond will be installed and started as a system service.

Dependencies
------------

Node

Example Playbook
----------------

    - name: The Prometheus Node Exporter role
      hosts: node-exporter
      become: yes
      become_method: sudo

      vars:
        prometheus_node_exporter_enabled_collectors:
          - gmond
          - loadavg

      roles:
        - ansible-role-prometheus-node-exporter

      tags:
        - node-exporter

