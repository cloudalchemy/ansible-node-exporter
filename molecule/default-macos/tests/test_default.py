import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/var/lib/node_exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/usr/local/bin/node_exporter"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.run("sudo launchctl list homebrew.mxcl.node_exporter")
    assert s.succeeded


def test_process(host):
    r = host.run("ps -A -o user,pid,comm | grep node_exporter | grep -v grep")
    splitted = r.stdout.split()

    assert 'node-exp' == splitted[0]
    assert '/usr/local/bin/node_exporter' == splitted[2]
