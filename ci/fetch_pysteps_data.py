"""
Install the pysteps data in a test environment and create a pystepsrc
configuration file pointing to that data.
"""

if __name__ == "__main__":
    import argparse
    from pysteps.datasets import create_default_pystepsrc, download_pysteps_data

    parser = argparse.ArgumentParser(description="Install pysteps data")

    parser.add_argument(
        "dest_dir", type=str, help="Directory where to install the Pysteps data"
    )
    args = parser.parse_args()

    download_pysteps_data(args.dest_dir, force=True)
    create_default_pystepsrc(args.dest_dir)
