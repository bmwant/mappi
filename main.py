from rich.pretty import pprint


def check():
    from mappi.schema import Route, RouteType, ServerConfig

    pprint(ServerConfig.__fields__)
    pprint(Route.__fields__)

    print("schema", ServerConfig.schema())
    print("schema", Route.schema())
    for rt in RouteType:
        print(rt)


if __name__ == "__main__":
    check()
