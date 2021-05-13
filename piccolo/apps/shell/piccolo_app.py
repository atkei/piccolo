from piccolo.conf.apps import AppConfig, Command
from .commands.run import run


APP_CONFIG = AppConfig(
    app_name="shell",
    migrations_folder_path="",
    commands=[Command(callable=run, aliases=["start"])],
)
