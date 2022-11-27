def test_config_fixture(make_read_config, mappi_server):
    read_config = make_read_config("status_500.yml")
    config = read_config()
    print(config)


# @pytest.mark.parametrize("make_config", ["status_500.yml"])
def test_parametrize():
    pass
