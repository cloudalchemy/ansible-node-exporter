# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/node_exporter)

## [2.0.0] - 2021-04-19
**Merged pull requests:**

- Merge pull request [#219](https://github.com/cloudalchemy/ansible-node-exporter/issues/219) from cloudalchemy/skeleton
- :robot: sync with cloudalchemy/skeleton (SHA: 5ca88c27): Merge pull request [#9](https://github.com/cloudalchemy/ansible-node-exporter/issues/9) from cloudalchemy/superq/more_updates


## [1.0.0] - 2021-04-11
**Merged pull requests:**

- Merge pull request [#214](https://github.com/cloudalchemy/ansible-node-exporter/issues/214) from cloudalchemy/superq/envs
- Merge pull request [#213](https://github.com/cloudalchemy/ansible-node-exporter/issues/213) from cloudalchemy/superq/chglog
- Merge pull request [#212](https://github.com/cloudalchemy/ansible-node-exporter/issues/212) from cloudalchemy/superq/publisher_image
- Merge pull request [#209](https://github.com/cloudalchemy/ansible-node-exporter/issues/209) from cloudalchemy/autoupdate
- Merge pull request [#208](https://github.com/cloudalchemy/ansible-node-exporter/issues/208) from cloudalchemy/autoupdate
- Merge pull request [#207](https://github.com/cloudalchemy/ansible-node-exporter/issues/207) from nop33/fix-typos
- Merge pull request [#206](https://github.com/cloudalchemy/ansible-node-exporter/issues/206) from cloudalchemy/paulfantom-patch-1
- Merge pull request [#204](https://github.com/cloudalchemy/ansible-node-exporter/issues/204) from cloudalchemy/bjk/update_requirements
- Merge pull request [#202](https://github.com/cloudalchemy/ansible-node-exporter/issues/202) from cloudalchemy/autoupdate
- Merge pull request [#197](https://github.com/cloudalchemy/ansible-node-exporter/issues/197) from cloudalchemy/paulfantom/fix-release
- Merge pull request [#196](https://github.com/cloudalchemy/ansible-node-exporter/issues/196) from kmille/master
- Merge pull request [#195](https://github.com/cloudalchemy/ansible-node-exporter/issues/195) from cloudalchemy/paulfantom/scenario-latest
- Merge pull request [#182](https://github.com/cloudalchemy/ansible-node-exporter/issues/182) from parmsib/patch-1
- Merge pull request [#187](https://github.com/cloudalchemy/ansible-node-exporter/issues/187) from cloudalchemy/superq/internal_defaults
- Merge pull request [#193](https://github.com/cloudalchemy/ansible-node-exporter/issues/193) from cloudalchemy/paulfantom-patch-1
- Merge pull request [#188](https://github.com/cloudalchemy/ansible-node-exporter/issues/188) from ctrlaltdel/master
- Merge pull request [#191](https://github.com/cloudalchemy/ansible-node-exporter/issues/191) from cloudalchemy/superq/circle_release
- Merge pull request [#190](https://github.com/cloudalchemy/ansible-node-exporter/issues/190) from cloudalchemy/superq/circleci
- Merge pull request [#189](https://github.com/cloudalchemy/ansible-node-exporter/issues/189) from cloudalchemy/moleculev3
- Merge pull request [#184](https://github.com/cloudalchemy/ansible-node-exporter/issues/184) from thdhondt/patch-1


## [0.22.0] - 2020-10-02
### Chore
- troubleshooting document

**Merged pull requests:**

- Merge pull request [#179](https://github.com/cloudalchemy/ansible-node-exporter/issues/179) from kklimonda/master
- Merge pull request [#178](https://github.com/cloudalchemy/ansible-node-exporter/issues/178) from FilippoProjetto/patch-1
- Merge pull request [#172](https://github.com/cloudalchemy/ansible-node-exporter/issues/172) from pngmbh/troubleshooting


## [0.21.5] - 2020-07-21
**Merged pull requests:**

- Merge pull request [#170](https://github.com/cloudalchemy/ansible-node-exporter/issues/170) from bittopaz/patch-1


## [0.21.4] - 2020-07-20
**Merged pull requests:**

- Merge pull request [#169](https://github.com/cloudalchemy/ansible-node-exporter/issues/169) from cloudalchemy/superq/localhost_checksums


## [0.21.3] - 2020-06-18
**Merged pull requests:**

- Merge pull request [#163](https://github.com/cloudalchemy/ansible-node-exporter/issues/163) from sengel/missing_backslash


## [0.21.2] - 2020-06-18
**Merged pull requests:**

- always import install.yml when using local dir ([#162](https://github.com/cloudalchemy/ansible-node-exporter/issues/162))


## [0.21.1] - 2020-06-17
**Merged pull requests:**

- New prometheus/node_exporter upstream release! ([#159](https://github.com/cloudalchemy/ansible-node-exporter/issues/159))


## [0.21.0] - 2020-05-31
**Merged pull requests:**

- *: add support for node_exporter TLS settings ([#156](https://github.com/cloudalchemy/ansible-node-exporter/issues/156))


## [0.20.0] - 2020-04-30
**Merged pull requests:**

- Use symbolic permissions for textfile collector dir ([#150](https://github.com/cloudalchemy/ansible-node-exporter/issues/150))
- :robot: sync with cloudalchemy/skeleton (SHA: 40e7ce18): lock molecule to v2 ([#149](https://github.com/cloudalchemy/ansible-node-exporter/issues/149))
- always validate GitHub certificate as there is no reason not to… ([#148](https://github.com/cloudalchemy/ansible-node-exporter/issues/148))
- Install 'policycoreutils-python' on redhat/centos < 8 and fedora… ([#145](https://github.com/cloudalchemy/ansible-node-exporter/issues/145))
- Add quotes to node_exporter parametrs in systemd service ([#144](https://github.com/cloudalchemy/ansible-node-exporter/issues/144))


## [0.19.0] - 2020-01-31
**Merged pull requests:**

- remove system user management and convert variables to internal ones ([#142](https://github.com/cloudalchemy/ansible-node-exporter/issues/142))
- Do not manage system directories ([#140](https://github.com/cloudalchemy/ansible-node-exporter/issues/140))
- Add binary install directory ([#137](https://github.com/cloudalchemy/ansible-node-exporter/issues/137))


## [0.18.0] - 2020-01-16
**Merged pull requests:**

- :robot: sync with cloudalchemy/skeleton (SHA: 69fc5be8): Merge pull request [#4](https://github.com/cloudalchemy/ansible-node-exporter/issues/4) from cloudalchemy/travis_fix ([#138](https://github.com/cloudalchemy/ansible-node-exporter/issues/138))
- :robot: sync with cloudalchemy/skeleton (SHA: f4521f6a): use latest available python ([#136](https://github.com/cloudalchemy/ansible-node-exporter/issues/136))
- Fix syntax on SELinux installation for clearlinux ([#134](https://github.com/cloudalchemy/ansible-node-exporter/issues/134))
- tasks,vars: move selinux package dependencies into separate tasks to allow potential ootb support for more OSes ([#132](https://github.com/cloudalchemy/ansible-node-exporter/issues/132))
- :robot: sync with cloudalchemy/skeleton (SHA: bb0f0949): remove IRC link ([#133](https://github.com/cloudalchemy/ansible-node-exporter/issues/133))
- Updated README.md ([#129](https://github.com/cloudalchemy/ansible-node-exporter/issues/129))
- add option to propagate binaries without access to internet ([#126](https://github.com/cloudalchemy/ansible-node-exporter/issues/126))
- [REPO SYNC] add declarative label sync; add autolabelling PRs ([#123](https://github.com/cloudalchemy/ansible-node-exporter/issues/123))


## [0.17.0] - 2019-11-14
**Merged pull requests:**

- [REPO SYNC] molecule: use CI images from quay.io instead of dock… ([#121](https://github.com/cloudalchemy/ansible-node-exporter/issues/121))
- tasks: remove already covered entries when choosing an OS specific vars ([#118](https://github.com/cloudalchemy/ansible-node-exporter/issues/118))
- Run preflight tasks to register variables when check_mode is enabled ([#117](https://github.com/cloudalchemy/ansible-node-exporter/issues/117))
- tasks: do not touch any settings of system directory /usr/local/bin ([#116](https://github.com/cloudalchemy/ansible-node-exporter/issues/116))
- [REPO SYNC] Update releaser.sh ([#120](https://github.com/cloudalchemy/ansible-node-exporter/issues/120))
- [REPO SYNC] add support for CentOS8 ([#119](https://github.com/cloudalchemy/ansible-node-exporter/issues/119))


## [0.16.0] - 2019-10-18
**Merged pull requests:**

- add official support for CentOS8 ([#114](https://github.com/cloudalchemy/ansible-node-exporter/issues/114))
- molecule/default/tests: test if permissions of other files are u… ([#112](https://github.com/cloudalchemy/ansible-node-exporter/issues/112))
- tasks: do not use alias for createhome as it seems to be broken ([#111](https://github.com/cloudalchemy/ansible-node-exporter/issues/111))


## [0.15.0] - 2019-09-11
**Merged pull requests:**

- add RHEL8 and debian buster support; remove testing on debian jessie ([#101](https://github.com/cloudalchemy/ansible-node-exporter/issues/101))
- Synchronize files from cloudalchemy/skeleton ([#102](https://github.com/cloudalchemy/ansible-node-exporter/issues/102))
- :robot: synchronize with last commit in cloudalchemy/skeleton (SHA: 1f68dc21) ([#100](https://github.com/cloudalchemy/ansible-node-exporter/issues/100))
- Moving to python 3 and dropping support for python 2.x (on deploy… ([#99](https://github.com/cloudalchemy/ansible-node-exporter/issues/99))
- :robot: synchronize files from cloudalchemy/skeleton ([#97](https://github.com/cloudalchemy/ansible-node-exporter/issues/97))
- added restartsec and startlimitinterval configurations ([#96](https://github.com/cloudalchemy/ansible-node-exporter/issues/96))
- preflight: Fix detection of systemd version for systemd 240+ ([#93](https://github.com/cloudalchemy/ansible-node-exporter/issues/93))
- Updated README with correct default value ([#92](https://github.com/cloudalchemy/ansible-node-exporter/issues/92))
- node_exporter version check ([#91](https://github.com/cloudalchemy/ansible-node-exporter/issues/91))


## [0.14.0] - 2019-06-05
**Merged pull requests:**

- Fix wrong size of /home shown by node-exporter ([#87](https://github.com/cloudalchemy/ansible-node-exporter/issues/87))
- :tada: automated upstream release update ([#90](https://github.com/cloudalchemy/ansible-node-exporter/issues/90))
- make node_exporter executable file root-owned ([#89](https://github.com/cloudalchemy/ansible-node-exporter/issues/89))
- Add retries to package installs ([#88](https://github.com/cloudalchemy/ansible-node-exporter/issues/88))
- Create suse.yml ([#86](https://github.com/cloudalchemy/ansible-node-exporter/issues/86))
- New prometheus/node_exporter upstream release! ([#85](https://github.com/cloudalchemy/ansible-node-exporter/issues/85))
- Synchronize files from cloudalchemy/skeleton ([#84](https://github.com/cloudalchemy/ansible-node-exporter/issues/84))


## [0.13.1] - 2019-05-04
**Merged pull requests:**

- Fix systemd service startup ordering ([#83](https://github.com/cloudalchemy/ansible-node-exporter/issues/83))


## [0.13.0] - 2019-04-01
**Merged pull requests:**

- fix preflight check responsible for collector enablement ([#81](https://github.com/cloudalchemy/ansible-node-exporter/issues/81))
- Refactor preflight checks ([#79](https://github.com/cloudalchemy/ansible-node-exporter/issues/79))
- make SELinux settings ipv6 compatible ([#78](https://github.com/cloudalchemy/ansible-node-exporter/issues/78))
- fix(tasks/configure.yml): typo in task name ([#77](https://github.com/cloudalchemy/ansible-node-exporter/issues/77))
- Add systemd state to started for first run of the role ([#72](https://github.com/cloudalchemy/ansible-node-exporter/issues/72))
- reintroduce user management into defaults and add testing user creation ([#74](https://github.com/cloudalchemy/ansible-node-exporter/issues/74))


## [0.12.1] - 2019-02-19
**Merged pull requests:**

- Correctly enable extra collectors ([#70](https://github.com/cloudalchemy/ansible-node-exporter/issues/70))
- Lock down systemd service ([#68](https://github.com/cloudalchemy/ansible-node-exporter/issues/68))


## [0.12.0] - 2018-12-17
**Merged pull requests:**

- Better tags and configuration handling ([#66](https://github.com/cloudalchemy/ansible-node-exporter/issues/66))
- simplify automated CPU arch choosing ([#64](https://github.com/cloudalchemy/ansible-node-exporter/issues/64))
- add alternative tests ([#65](https://github.com/cloudalchemy/ansible-node-exporter/issues/65))


## [0.11.4] - 2018-12-05
**Merged pull requests:**

- Add support for multi-line ansible_managed strings ([#63](https://github.com/cloudalchemy/ansible-node-exporter/issues/63))


## [0.11.3] - 2018-12-03
**Merged pull requests:**

- New node_exporter upstream release! ([#62](https://github.com/cloudalchemy/ansible-node-exporter/issues/62))
- Remove setting niceness in systemd service file ([#60](https://github.com/cloudalchemy/ansible-node-exporter/issues/60))


## [0.11.2] - 2018-10-08
**Merged pull requests:**

- move to ansible 2.7 ([#58](https://github.com/cloudalchemy/ansible-node-exporter/issues/58))


## [0.11.1] - 2018-10-04
**Merged pull requests:**

- do not set specific capabilities ([#57](https://github.com/cloudalchemy/ansible-node-exporter/issues/57))


## [0.11.0] - 2018-09-19
**Merged pull requests:**

- Add support for Clear linux ([#55](https://github.com/cloudalchemy/ansible-node-exporter/issues/55))
- make textfile dir writable by node-exp group ([#56](https://github.com/cloudalchemy/ansible-node-exporter/issues/56))


## [0.10.2] - 2018-09-06
**Merged pull requests:**

- reload-daemon on systemd enable ([#53](https://github.com/cloudalchemy/ansible-node-exporter/issues/53))


## [0.10.1] - 2018-08-15
**Merged pull requests:**

- download checksum file only once ([#51](https://github.com/cloudalchemy/ansible-node-exporter/issues/51))


## [0.10.0] - 2018-07-15
**Merged pull requests:**

- import_tasks instead of include; bringing role up to ansible-prometheus standards; minor changes ([#48](https://github.com/cloudalchemy/ansible-node-exporter/issues/48))


## [0.9.0] - 2018-07-01
**Merged pull requests:**

- ansible 2.6 + allow remote docker host ([#46](https://github.com/cloudalchemy/ansible-node-exporter/issues/46))
- use tox for running test matrix ([#45](https://github.com/cloudalchemy/ansible-node-exporter/issues/45))


## [0.8.0] - 2018-06-10
**Merged pull requests:**

- Add support for textfile collector ([#42](https://github.com/cloudalchemy/ansible-node-exporter/issues/42))


## [0.7.0] - 2018-06-10
**Merged pull requests:**

- Install newer node_exporter by default ([#36](https://github.com/cloudalchemy/ansible-node-exporter/issues/36))
- specify file name for dest in get_url call ([#40](https://github.com/cloudalchemy/ansible-node-exporter/issues/40))


## [0.6.20] - 2018-05-27
**Merged pull requests:**

- Fix architecture var parsing ([#39](https://github.com/cloudalchemy/ansible-node-exporter/issues/39))
- Offer a better IRC Web clients to users ([#38](https://github.com/cloudalchemy/ansible-node-exporter/issues/38))


## [0.6.19] - 2018-05-23
**Merged pull requests:**

- Fix failing role on non-SELinux RedHat ([#37](https://github.com/cloudalchemy/ansible-node-exporter/issues/37))
- split download and unarchive and add checksum validation ([#35](https://github.com/cloudalchemy/ansible-node-exporter/issues/35))
- move to molecule 2.x ([#34](https://github.com/cloudalchemy/ansible-node-exporter/issues/34))


## [0.6.18] - 2018-04-13
**Merged pull requests:**

- Merge pull request [#33](https://github.com/cloudalchemy/ansible-node-exporter/issues/33) from nikosgraser/master


## [0.6.17] - 2018-04-12
**Merged pull requests:**

- Merge pull request [#32](https://github.com/cloudalchemy/ansible-node-exporter/issues/32) from Porkepix/skip_capabilities_check_mode


## [0.6.16] - 2018-04-06
**Merged pull requests:**

- Merge pull request [#31](https://github.com/cloudalchemy/ansible-node-exporter/issues/31) from Porkepix/fix_tests_as_filter
- Merge pull request [#30](https://github.com/cloudalchemy/ansible-node-exporter/issues/30) from Porkepix/fix_gitignore


## [0.6.15] - 2018-04-05

## [0.6.14] - 2018-04-02
**Merged pull requests:**

- retry downloads ([#29](https://github.com/cloudalchemy/ansible-node-exporter/issues/29))


## [0.6.13] - 2018-03-30
**Merged pull requests:**

- Merge pull request [#28](https://github.com/cloudalchemy/ansible-node-exporter/issues/28) from Porkepix/fix-check_mode


## [0.6.12] - 2018-03-26
**Merged pull requests:**

- Merge pull request [#26](https://github.com/cloudalchemy/ansible-node-exporter/issues/26) from cloudalchemy/bionic


## [0.6.11] - 2018-03-24
**Merged pull requests:**

- Merge pull request [#27](https://github.com/cloudalchemy/ansible-node-exporter/issues/27) from cloudalchemy/new_ansible


## [0.6.10] - 2018-03-05
**Merged pull requests:**

- Merge pull request [#25](https://github.com/cloudalchemy/ansible-node-exporter/issues/25) from swesterveld/fix-warning-jinja-templating-delimiters


## [0.6.9] - 2018-02-18
**Merged pull requests:**

- Merge pull request [#24](https://github.com/cloudalchemy/ansible-node-exporter/issues/24) from cloudalchemy/fedora_support
- resolve [#18](https://github.com/cloudalchemy/ansible-node-exporter/issues/18)


## [0.6.8] - 2018-02-14
**Merged pull requests:**

- Merge pull request [#23](https://github.com/cloudalchemy/ansible-node-exporter/issues/23) from swesterveld/fix_daemon_reload_for_role_include


## [0.6.7] - 2018-01-14
**Merged pull requests:**

- custom dockerfiles; support more OSes ([#21](https://github.com/cloudalchemy/ansible-node-exporter/issues/21))


## [0.6.6] - 2018-01-13
**Merged pull requests:**

- Add preflight checks ([#22](https://github.com/cloudalchemy/ansible-node-exporter/issues/22))


## [0.6.5] - 2018-01-13
**Merged pull requests:**

- Merge pull request [#20](https://github.com/cloudalchemy/ansible-node-exporter/issues/20) from cloudalchemy/paulfantom-patch-1


## [0.6.4] - 2018-01-09
**Merged pull requests:**

- Merge pull request [#19](https://github.com/cloudalchemy/ansible-node-exporter/issues/19) from cloudalchemy/issue17


## [0.6.3] - 2018-01-08

## [0.6.2] - 2018-01-06
**Merged pull requests:**

- Merge pull request [#15](https://github.com/cloudalchemy/ansible-node-exporter/issues/15) from cloudalchemy/minor_fix


## [0.6.1] - 2018-01-04
**Merged pull requests:**

- Merge pull request [#14](https://github.com/cloudalchemy/ansible-node-exporter/issues/14) from cloudalchemy/paulfantom-patch-1
- Merge pull request [#13](https://github.com/cloudalchemy/ansible-node-exporter/issues/13) from cloudalchemy/docs


## [0.6.0] - 2018-01-02
**Merged pull requests:**

- Merge pull request [#12](https://github.com/cloudalchemy/ansible-node-exporter/issues/12) from cloudalchemy/paulfantom-patch-1


## [0.5.11] - 2018-01-02
**Merged pull requests:**

- Merge pull request [#11](https://github.com/cloudalchemy/ansible-node-exporter/issues/11) from cloudalchemy/raspberrypi


## [0.5.10] - 2018-01-01
**Merged pull requests:**

- Merge pull request [#10](https://github.com/cloudalchemy/ansible-node-exporter/issues/10) from cloudalchemy/disabled_collectors


## [0.5.9] - 2017-12-27
**Merged pull requests:**

- Merge pull request [#9](https://github.com/cloudalchemy/ansible-node-exporter/issues/9) from anisse/patch-1


## [0.5.8] - 2017-12-27
**Merged pull requests:**

- Merge pull request [#8](https://github.com/cloudalchemy/ansible-node-exporter/issues/8) from anisse/patch-3


## [0.5.7] - 2017-12-15
**Merged pull requests:**

- Merge pull request [#6](https://github.com/cloudalchemy/ansible-node-exporter/issues/6) from cloudalchemy/go_arch
- Merge pull request [#7](https://github.com/cloudalchemy/ansible-node-exporter/issues/7) from cloudalchemy/version


## [0.5.6] - 2017-12-06
**Merged pull requests:**

- Merge pull request [#4](https://github.com/cloudalchemy/ansible-node-exporter/issues/4) from cloudalchemy/paulfantom-patch-1


## [0.5.5] - 2017-11-30

## [0.5.4] - 2017-11-30

## [0.5.3] - 2017-11-29
**Merged pull requests:**

- Merge pull request [#1](https://github.com/cloudalchemy/ansible-node-exporter/issues/1) from cloudalchemy/ci


## [0.5.1] - 2017-11-09
**Merged pull requests:**

- Merge pull request [#10](https://github.com/cloudalchemy/ansible-node-exporter/issues/10) from SoInteractive/version_upgrade


## [0.5.0] - 2017-10-16
**Merged pull requests:**

- Merge pull request [#9](https://github.com/cloudalchemy/ansible-node-exporter/issues/9) from SoInteractive/feature_travis


## [0.4.3] - 2017-10-12
**Merged pull requests:**

- Merge pull request [#8](https://github.com/cloudalchemy/ansible-node-exporter/issues/8) from SoInteractive/Add_selinux


## [0.4.2] - 2017-10-05
**Merged pull requests:**

- Merge pull request [#7](https://github.com/cloudalchemy/ansible-node-exporter/issues/7) from SoInteractive/systemd


## [0.4.1] - 2017-09-26
**Merged pull requests:**

- Merge pull request [#6](https://github.com/cloudalchemy/ansible-node-exporter/issues/6) from SoInteractive/fix_typo


## [0.4.0] - 2017-09-20
**Merged pull requests:**

- Merge pull request [#5](https://github.com/cloudalchemy/ansible-node-exporter/issues/5) from paulfantom/feature_installation


## [0.3.3] - 2017-08-09

## [0.3.4] - 2017-08-09
**Merged pull requests:**

- Merge pull request [#4](https://github.com/cloudalchemy/ansible-node-exporter/issues/4) from SoInteractive/testing_branch


## [0.3.2] - 2017-07-26

## [0.3.1] - 2017-07-26
**Merged pull requests:**

- Merge pull request [#3](https://github.com/cloudalchemy/ansible-node-exporter/issues/3) from SoInteractive/fix_user_uid


## [0.3.0] - 2017-07-21

## [0.2.0] - 2017-07-21
**Merged pull requests:**

- Merge pull request [#2](https://github.com/cloudalchemy/ansible-node-exporter/issues/2) from SoInteractive/feature_autoupdate_minor


## [0.1.2] - 2017-06-14

## [0.1.1] - 2017-06-14

## [0.1.0] - 2017-06-06

## [0.0.2] - 2017-05-18

## 0.0.1 - 2017-05-04

[Unreleased]: https://github.com/cloudalchemy/ansible-node-exporter/compare/2.0.0...HEAD
[2.0.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/1.0.0...2.0.0
[1.0.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.22.0...1.0.0
[0.22.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.5...0.22.0
[0.21.5]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.4...0.21.5
[0.21.4]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.3...0.21.4
[0.21.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.2...0.21.3
[0.21.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.1...0.21.2
[0.21.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.21.0...0.21.1
[0.21.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.20.0...0.21.0
[0.20.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.19.0...0.20.0
[0.19.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.18.0...0.19.0
[0.18.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.17.0...0.18.0
[0.17.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.16.0...0.17.0
[0.16.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.15.0...0.16.0
[0.15.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.14.0...0.15.0
[0.14.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.13.1...0.14.0
[0.13.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.13.0...0.13.1
[0.13.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.12.1...0.13.0
[0.12.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.12.0...0.12.1
[0.12.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.11.4...0.12.0
[0.11.4]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.11.3...0.11.4
[0.11.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.11.2...0.11.3
[0.11.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.11.1...0.11.2
[0.11.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.11.0...0.11.1
[0.11.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.10.2...0.11.0
[0.10.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.10.1...0.10.2
[0.10.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.10.0...0.10.1
[0.10.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.9.0...0.10.0
[0.9.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.8.0...0.9.0
[0.8.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.7.0...0.8.0
[0.7.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.20...0.7.0
[0.6.20]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.19...0.6.20
[0.6.19]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.18...0.6.19
[0.6.18]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.17...0.6.18
[0.6.17]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.16...0.6.17
[0.6.16]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.15...0.6.16
[0.6.15]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.14...0.6.15
[0.6.14]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.13...0.6.14
[0.6.13]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.12...0.6.13
[0.6.12]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.11...0.6.12
[0.6.11]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.10...0.6.11
[0.6.10]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.9...0.6.10
[0.6.9]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.8...0.6.9
[0.6.8]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.7...0.6.8
[0.6.7]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.6...0.6.7
[0.6.6]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.5...0.6.6
[0.6.5]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.4...0.6.5
[0.6.4]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.3...0.6.4
[0.6.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.2...0.6.3
[0.6.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.1...0.6.2
[0.6.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.11...0.6.0
[0.5.11]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.10...0.5.11
[0.5.10]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.9...0.5.10
[0.5.9]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.8...0.5.9
[0.5.8]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.7...0.5.8
[0.5.7]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.6...0.5.7
[0.5.6]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.5...0.5.6
[0.5.5]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.4...0.5.5
[0.5.4]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.3...0.5.4
[0.5.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.1...0.5.3
[0.5.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.4.3...0.5.0
[0.4.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.4.2...0.4.3
[0.4.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.4.1...0.4.2
[0.4.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.3.3...0.4.0
[0.3.3]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.3.4...0.3.3
[0.3.4]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.3.2...0.3.4
[0.3.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.1.2...0.2.0
[0.1.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.0.2...0.1.0
[0.0.2]: https://github.com/cloudalchemy/ansible-node-exporter/compare/0.0.1...0.0.2
