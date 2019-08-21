# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/node-exporter)

**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#102](https://github.com/cloudalchemy/ansible-node-exporter/pull/102) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add RHEL8 and debian buster support; remove testing on debian jessie [\#101](https://github.com/cloudalchemy/ansible-node-exporter/pull/101) ([paulfantom](https://github.com/paulfantom))
- Update minimum required ansible version [\#100](https://github.com/cloudalchemy/ansible-node-exporter/pull/100) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Moving to python 3 and dropping support for python 2.x \(on deployer host\) [\#99](https://github.com/cloudalchemy/ansible-node-exporter/pull/99) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#97](https://github.com/cloudalchemy/ansible-node-exporter/pull/97) ([cloudalchemybot](https://github.com/cloudalchemybot))
- added restartsec and startlimitinterval configurations [\#96](https://github.com/cloudalchemy/ansible-node-exporter/pull/96) ([oguzhaninan](https://github.com/oguzhaninan))
- preflight: Fix detection of systemd version for systemd 240+ [\#93](https://github.com/cloudalchemy/ansible-node-exporter/pull/93) ([0xFelix](https://github.com/0xFelix))
- Updated README with correct default value [\#92](https://github.com/cloudalchemy/ansible-node-exporter/pull/92) ([nicholasamorim](https://github.com/nicholasamorim))
- node\_exporter version check [\#91](https://github.com/cloudalchemy/ansible-node-exporter/pull/91) ([rwos](https://github.com/rwos))

## [0.14.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2019-06-05)
**Merged pull requests:**

- New prometheus/node\_exporter upstream release! [\#90](https://github.com/cloudalchemy/ansible-node-exporter/pull/90) ([cloudalchemybot](https://github.com/cloudalchemybot))
- make node\_exporter executable file root-owned [\#89](https://github.com/cloudalchemy/ansible-node-exporter/pull/89) ([slrz](https://github.com/slrz))
- Add retries to package installs [\#88](https://github.com/cloudalchemy/ansible-node-exporter/pull/88) ([denmat](https://github.com/denmat))
- Fix wrong size of /home shown by node-exporter [\#87](https://github.com/cloudalchemy/ansible-node-exporter/pull/87) ([laurvas](https://github.com/laurvas))
- Create suse.yml [\#86](https://github.com/cloudalchemy/ansible-node-exporter/pull/86) ([jbhannah](https://github.com/jbhannah))
- New prometheus/node\_exporter upstream release! [\#85](https://github.com/cloudalchemy/ansible-node-exporter/pull/85) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#84](https://github.com/cloudalchemy/ansible-node-exporter/pull/84) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.13.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2019-05-04)
**Fixed bugs:**

- Disable collectors [\#80](https://github.com/cloudalchemy/ansible-node-exporter/issues/80)

**Merged pull requests:**

- Fix systemd service startup ordering [\#83](https://github.com/cloudalchemy/ansible-node-exporter/pull/83) ([ko-zu](https://github.com/ko-zu))

## [0.13.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2019-04-01)
**Closed issues:**

- IPv4 assumption in SELinux tasks [\#75](https://github.com/cloudalchemy/ansible-node-exporter/issues/75)
- Node\_exporter is not running with fresh install on Debian 9 [\#71](https://github.com/cloudalchemy/ansible-node-exporter/issues/71)

**Merged pull requests:**

- fix preflight check responsible for collector enablement [\#81](https://github.com/cloudalchemy/ansible-node-exporter/pull/81) ([paulfantom](https://github.com/paulfantom))
- Refactor preflight checks [\#79](https://github.com/cloudalchemy/ansible-node-exporter/pull/79) ([paulfantom](https://github.com/paulfantom))
- make SELinux settings ipv6 compatible [\#78](https://github.com/cloudalchemy/ansible-node-exporter/pull/78) ([paulfantom](https://github.com/paulfantom))
- fix\(tasks/configure.yml\): typo in task name [\#77](https://github.com/cloudalchemy/ansible-node-exporter/pull/77) ([angristan](https://github.com/angristan))
- reintroduce user management into defaults and add testing user creation [\#74](https://github.com/cloudalchemy/ansible-node-exporter/pull/74) ([paulfantom](https://github.com/paulfantom))
- Add systemd state to started for first run of the role [\#72](https://github.com/cloudalchemy/ansible-node-exporter/pull/72) ([MCyprien](https://github.com/MCyprien))

## [0.12.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2019-02-19)
**Merged pull requests:**

- Correctly enable extra collectors [\#70](https://github.com/cloudalchemy/ansible-node-exporter/pull/70) ([SuperQ](https://github.com/SuperQ))
- Lock down systemd service [\#68](https://github.com/cloudalchemy/ansible-node-exporter/pull/68) ([ecksun](https://github.com/ecksun))

## [0.12.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-12-17)
**Merged pull requests:**

- Better tags and configuration handling [\#66](https://github.com/cloudalchemy/ansible-node-exporter/pull/66) ([paulfantom](https://github.com/paulfantom))
- add alternative tests [\#65](https://github.com/cloudalchemy/ansible-node-exporter/pull/65) ([paulfantom](https://github.com/paulfantom))
- simplify automated CPU arch choosing [\#64](https://github.com/cloudalchemy/ansible-node-exporter/pull/64) ([paulfantom](https://github.com/paulfantom))

## [0.11.4](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-12-05)
**Merged pull requests:**

- Add support for multi-line ansible\_managed strings [\#63](https://github.com/cloudalchemy/ansible-node-exporter/pull/63) ([etcet](https://github.com/etcet))

## [0.11.3](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-12-03)
**Closed issues:**

- Nice'ness fails node\_exporter [\#59](https://github.com/cloudalchemy/ansible-node-exporter/issues/59)

**Merged pull requests:**

- New node\_exporter upstream release! [\#62](https://github.com/cloudalchemy/ansible-node-exporter/pull/62) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Remove setting niceness in systemd service file [\#60](https://github.com/cloudalchemy/ansible-node-exporter/pull/60) ([paulfantom](https://github.com/paulfantom))

## [0.11.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-10-08)
**Merged pull requests:**

- move to ansible 2.7 [\#58](https://github.com/cloudalchemy/ansible-node-exporter/pull/58) ([paulfantom](https://github.com/paulfantom))

## [0.11.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-10-04)
**Merged pull requests:**

- do not set specific capabilities [\#57](https://github.com/cloudalchemy/ansible-node-exporter/pull/57) ([paulfantom](https://github.com/paulfantom))

## [0.11.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-09-19)
**Closed issues:**

- Python crashes when running role [\#54](https://github.com/cloudalchemy/ansible-node-exporter/issues/54)

**Merged pull requests:**

- make textfile dir writable by node-exp group [\#56](https://github.com/cloudalchemy/ansible-node-exporter/pull/56) ([jillro](https://github.com/jillro))
- Add support for Clear linux [\#55](https://github.com/cloudalchemy/ansible-node-exporter/pull/55) ([bswinnerton](https://github.com/bswinnerton))

## [0.10.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-09-06)
**Fixed bugs:**

- Rate limit errors due to checksum fetching [\#50](https://github.com/cloudalchemy/ansible-node-exporter/issues/50)

**Merged pull requests:**

- reload-daemon on systemd enable [\#53](https://github.com/cloudalchemy/ansible-node-exporter/pull/53) ([jewzaam](https://github.com/jewzaam))

## [0.10.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-08-15)
**Merged pull requests:**

- download checksum file only once [\#51](https://github.com/cloudalchemy/ansible-node-exporter/pull/51) ([paulfantom](https://github.com/paulfantom))

## [0.10.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-07-15)
**Implemented enhancements:**

- import\_tasks instead of include; bringing role up to ansible-prometheus standards; minor changes [\#48](https://github.com/cloudalchemy/ansible-node-exporter/pull/48) ([paulfantom](https://github.com/paulfantom))

## [0.9.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-07-01)
**Fixed bugs:**

- Problems with `node\_exporter\_textfile\_dir` [\#43](https://github.com/cloudalchemy/ansible-node-exporter/issues/43)

**Closed issues:**

- node-exporter service handler is triggered before deployment [\#44](https://github.com/cloudalchemy/ansible-node-exporter/issues/44)

**Merged pull requests:**

- ansible 2.6 + allow remote docker host [\#46](https://github.com/cloudalchemy/ansible-node-exporter/pull/46) ([paulfantom](https://github.com/paulfantom))
- use tox for running test matrix [\#45](https://github.com/cloudalchemy/ansible-node-exporter/pull/45) ([paulfantom](https://github.com/paulfantom))

## [0.8.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-06-10)
**Merged pull requests:**

- Add support for textfile collector [\#42](https://github.com/cloudalchemy/ansible-node-exporter/pull/42) ([SuperQ](https://github.com/SuperQ))

## [0.7.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-06-10)
**Implemented enhancements:**

- Socket activation [\#41](https://github.com/cloudalchemy/ansible-node-exporter/issues/41)

**Merged pull requests:**

- specify file name for dest in get\_url call [\#40](https://github.com/cloudalchemy/ansible-node-exporter/pull/40) ([sarphram](https://github.com/sarphram))
- Install newer node\_exporter by default [\#36](https://github.com/cloudalchemy/ansible-node-exporter/pull/36) ([paulfantom](https://github.com/paulfantom))

## [0.6.20](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-05-27)
**Merged pull requests:**

- Fix architecture var parsing [\#39](https://github.com/cloudalchemy/ansible-node-exporter/pull/39) ([SuperQ](https://github.com/SuperQ))
- Offer a better IRC Web clients to users [\#38](https://github.com/cloudalchemy/ansible-node-exporter/pull/38) ([Porkepix](https://github.com/Porkepix))

## [0.6.19](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-05-23)
**Merged pull requests:**

- Fix failing role on non-SELinux RedHat [\#37](https://github.com/cloudalchemy/ansible-node-exporter/pull/37) ([noraab](https://github.com/noraab))
- split download and unarchive and add checksum validation [\#35](https://github.com/cloudalchemy/ansible-node-exporter/pull/35) ([paulfantom](https://github.com/paulfantom))
- move to molecule 2.x [\#34](https://github.com/cloudalchemy/ansible-node-exporter/pull/34) ([paulfantom](https://github.com/paulfantom))

## [0.6.18](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-04-13)
**Merged pull requests:**

- Make node\_exporter.service template compatible with both Python 2 and 3 [\#33](https://github.com/cloudalchemy/ansible-node-exporter/pull/33) ([nikosgraser](https://github.com/nikosgraser))

## [0.6.17](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-04-12)
**Merged pull requests:**

- Skip capabilities set in check\_mode [\#32](https://github.com/cloudalchemy/ansible-node-exporter/pull/32) ([Porkepix](https://github.com/Porkepix))

## [0.6.16](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-04-06)
**Merged pull requests:**

- Fix test done using a filter [\#31](https://github.com/cloudalchemy/ansible-node-exporter/pull/31) ([Porkepix](https://github.com/Porkepix))
- Fix \_\_pycache\_\_ in .gitignore [\#30](https://github.com/cloudalchemy/ansible-node-exporter/pull/30) ([Porkepix](https://github.com/Porkepix))

## [0.6.15](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-04-05)
## [0.6.14](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-04-02)
**Merged pull requests:**

- retry downloads [\#29](https://github.com/cloudalchemy/ansible-node-exporter/pull/29) ([paulfantom](https://github.com/paulfantom))

## [0.6.13](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-03-30)
**Merged pull requests:**

- Fix check mode [\#28](https://github.com/cloudalchemy/ansible-node-exporter/pull/28) ([Porkepix](https://github.com/Porkepix))

## [0.6.12](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-03-26)
**Merged pull requests:**

- Ubuntu bionic \(18.04\) support [\#26](https://github.com/cloudalchemy/ansible-node-exporter/pull/26) ([paulfantom](https://github.com/paulfantom))

## [0.6.11](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-03-24)
**Merged pull requests:**

- ansible 2.5 [\#27](https://github.com/cloudalchemy/ansible-node-exporter/pull/27) ([paulfantom](https://github.com/paulfantom))

## [0.6.10](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-03-05)
**Closed issues:**

- Adding option to configure collectors [\#18](https://github.com/cloudalchemy/ansible-node-exporter/issues/18)

**Merged pull requests:**

- Modify when-statement to not include jinja2 templating delimiters such [\#25](https://github.com/cloudalchemy/ansible-node-exporter/pull/25) ([swesterveld](https://github.com/swesterveld))

## [0.6.9](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-02-18)
**Closed issues:**

- Preflight checks [\#16](https://github.com/cloudalchemy/ansible-node-exporter/issues/16)

**Merged pull requests:**

- fedora support + issue 18 [\#24](https://github.com/cloudalchemy/ansible-node-exporter/pull/24) ([paulfantom](https://github.com/paulfantom))

## [0.6.8](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-02-14)
**Merged pull requests:**

- Make Prometheus node exporter restart/reload with sudo privileges. [\#23](https://github.com/cloudalchemy/ansible-node-exporter/pull/23) ([swesterveld](https://github.com/swesterveld))

## [0.6.7](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-14)
**Merged pull requests:**

- custom docker images; support more OSes [\#21](https://github.com/cloudalchemy/ansible-node-exporter/pull/21) ([paulfantom](https://github.com/paulfantom))

## [0.6.6](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-13)
**Merged pull requests:**

- Add preflight checks [\#22](https://github.com/cloudalchemy/ansible-node-exporter/pull/22) ([jkrol2](https://github.com/jkrol2))

## [0.6.5](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-13)
**Closed issues:**

- Permission denied to fs [\#17](https://github.com/cloudalchemy/ansible-node-exporter/issues/17)

**Merged pull requests:**

- Set home directory for node-exp user [\#20](https://github.com/cloudalchemy/ansible-node-exporter/pull/20) ([paulfantom](https://github.com/paulfantom))

## [0.6.4](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-09)
**Merged pull requests:**

- Fix \#17 [\#19](https://github.com/cloudalchemy/ansible-node-exporter/pull/19) ([paulfantom](https://github.com/paulfantom))

## [0.6.3](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-08)
## [0.6.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-06)
**Merged pull requests:**

- minor fix, added i386 to arch [\#15](https://github.com/cloudalchemy/ansible-node-exporter/pull/15) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.6.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-04)
**Merged pull requests:**

- Lower niceness to increase app priority [\#14](https://github.com/cloudalchemy/ansible-node-exporter/pull/14) ([paulfantom](https://github.com/paulfantom))
- docs [\#13](https://github.com/cloudalchemy/ansible-node-exporter/pull/13) ([paulfantom](https://github.com/paulfantom))

## [0.6.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-02)
**Merged pull requests:**

- Update generatetag.sh [\#12](https://github.com/cloudalchemy/ansible-node-exporter/pull/12) ([paulfantom](https://github.com/paulfantom))

## [0.5.11](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-02)
**Merged pull requests:**

- support older raspberry pi [\#11](https://github.com/cloudalchemy/ansible-node-exporter/pull/11) ([paulfantom](https://github.com/paulfantom))

## [0.5.10](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2018-01-01)
**Closed issues:**

- Option to disable collectors [\#2](https://github.com/cloudalchemy/ansible-node-exporter/issues/2)

**Merged pull requests:**

- added node exporter disabled collectors option [\#10](https://github.com/cloudalchemy/ansible-node-exporter/pull/10) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.5.9](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-12-27)
**Merged pull requests:**

- armv7l ansible arch translates to armv7 go arch [\#9](https://github.com/cloudalchemy/ansible-node-exporter/pull/9) ([anisse](https://github.com/anisse))

## [0.5.8](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-12-27)
**Implemented enhancements:**

- Support multiple go architectures [\#5](https://github.com/cloudalchemy/ansible-node-exporter/issues/5)

**Merged pull requests:**

- Remove unused command line flags [\#8](https://github.com/cloudalchemy/ansible-node-exporter/pull/8) ([anisse](https://github.com/anisse))

## [0.5.7](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-12-15)
**Merged pull requests:**

- update node\_exporter version [\#7](https://github.com/cloudalchemy/ansible-node-exporter/pull/7) ([paulfantom](https://github.com/paulfantom))
- auto set go architecture [\#6](https://github.com/cloudalchemy/ansible-node-exporter/pull/6) ([paulfantom](https://github.com/paulfantom))

## [0.5.6](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-12-06)
**Merged pull requests:**

- Stop pipeline on any error [\#4](https://github.com/cloudalchemy/ansible-node-exporter/pull/4) ([paulfantom](https://github.com/paulfantom))

## [0.5.5](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-11-30)
## [0.5.4](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-11-30)
## [0.5.3](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-11-28)
**Merged pull requests:**

- fix CI; remove company from role description [\#1](https://github.com/cloudalchemy/ansible-node-exporter/pull/1) ([paulfantom](https://github.com/paulfantom))

## [0.5.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-11-09)
## [0.5.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-10-16)
## [0.4.3](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-10-12)
## [0.4.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-10-05)
## [0.4.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-09-26)
## [0.4.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-09-20)
## [0.3.4](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-08-09)
## [0.3.3](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-08-09)
## [0.3.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-07-26)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-07-26)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-07-21)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-07-21)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-06-14)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-06-14)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-06-06)
## [0.0.2](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-05-18)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/node-exporter) (2017-04-19)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*