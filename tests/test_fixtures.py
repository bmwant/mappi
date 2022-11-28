# def test_config_fixture(make_read_config, run_server):
#     read_config = make_read_config("status_500.yml")
#     config = read_config()
#     run_server(config)
#     print(config)


# @pytest.mark.parametrize("make_config", ["status_500.yml"])
def test_parametrize():
    pass


def my_get(url, params=None):
    print("This is url", url)


def test_free_port(free_port):
    from tests.utils import update_url

    f = update_url(my_get, "http://localhost:54322")
    f("/path")
