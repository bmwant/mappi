from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = CURRENT_DIR / "data"
DEFAULT_CONFIG_FILENAME = "mappi.yml"


CONFIG_MESSAGE = """
Here is your configuration.
Copy highlighted code below into [yellow]mappi.yml[/] file
or redirect output to the file using

$ [yellow]mappi config > mappi.yml[/]

For the complete list of available options use

$ [yellow]mappi config --full > mappi.yml[/]
""".strip()
