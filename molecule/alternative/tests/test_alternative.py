import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_files(host):
    files = [
        "/usr/local/bin/md_info_detail.sh",
        "/usr/local/bin/apt.sh"
        "/etc/systemd/system/textfile-collector-apt.sh.service"
        "/etc/systemd/system/textfile-collector-apt.sh.timer"
        "/etc/systemd/system/textfile-collector-md_info_detail.sh.service"
        "/etc/systemd/system/textfile-collector-md_info_detail.sh.timer"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file
        assert oct(f.mode) == '0o755'


def test_directories(host):
    dirs = [
        "/var/lib/node_exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_service(host):
    s = host.service("node_exporter")
#    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9100"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
