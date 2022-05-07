from config.app_config import AppConfig


class MainShell:
    @staticmethod
    def execute() -> None:
        conf = AppConfig().config
        max_print_count = int(conf.get("Common", "max_print_count"))

        for _ in range(max_print_count):
            print("Hello World!")


if __name__ == "__main__":
    MainShell.execute()
