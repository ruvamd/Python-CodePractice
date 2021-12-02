import argparse
from loguru import logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file name to process")
    args = parser.parse_args()
    try:
        with open(args.filename, "w") as f:
            f.write("hello")
    except Exception as ex:
        logger.info(f"file error: {ex}")


if __name__ == "__main__":
    main()
