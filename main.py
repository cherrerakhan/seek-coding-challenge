import sys

from traffic_counter import TrafficCounter

def main(argv):
    if len(argv) < 2:
        print("\nMissing text file, to run code: python main.py traffic_data.txt")
        sys.exit(1)

    traffic_data = argv[1]
    stats = TrafficCounter(traffic_data)
    stats.display_stats()

if __name__ == "__main__":
    main(sys.argv)