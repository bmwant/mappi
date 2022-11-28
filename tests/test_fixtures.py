# def test_config_fixture(make_read_config, run_server):
#     read_config = make_read_config("status_500.yml")
#     config = read_config()
#     run_server(config)
#     print(config)


# @pytest.mark.parametrize("make_config", ["status_500.yml"])
def test_parametrize():
    pass


def test_free_port(free_port):
    print("This is the one", free_port)


def test_another_free_port(free_port):
    print("This is the second one", free_port)
