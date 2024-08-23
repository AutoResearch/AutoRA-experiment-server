import random


def pytest_addoption(parser):
    parser.addoption(
        "--subset-percentage",
        action="store",
        default=None,
        help="Specify the percentage of tests to run as a subset (e.g., 0.3 for 30%)",
    )


def pytest_collection_modifyitems(config, items):
    subset_percentage = config.getoption("--subset-percentage")

    # If the subset percentage is provided, apply it
    if subset_percentage is not None:
        subset_percentage = float(subset_percentage)

        # Shuffle the test cases
        random.shuffle(items)

        # Calculate the number of tests to run based on percentage
        subset_count = int(len(items) * subset_percentage)

        # Select a subset of tests
        items[:] = items[:subset_count]
