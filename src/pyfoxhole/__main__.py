import sys
from importlib.metadata import version


def main() -> None:
    """Print version information"""
    print(f"{__package__} {version(__package__)}")


if __name__ == "__main__":
    sys.exit(main())
