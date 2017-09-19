from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(File):
    present = [
        "/etc/systemd/system/node_exporter.service",
        "/opt/node_exporter"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "node_exporter"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled
            assert s.is_running


def test_socket(Socket):
    present = [
        "tcp://127.0.0.1:9100"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
