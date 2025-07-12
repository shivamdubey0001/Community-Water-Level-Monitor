import json
import datetime
import argparse
import os
import matplotlib.pyplot as plt

# This is the main file that handles all water level monitoring tasks
# Made simple so anyone can understand and use it

def load_data():
    """Load water level data from JSON file - if file doesn't exist, create empty one"""
    try:
        if os.path.exists('data.json'):
            with open('data.json', 'r') as file:
                return json.load(file)
        else:
            # Create empty data structure if file doesn't exist
            return {"readings": [], "last_updated": "", "total_entries": 0}
    except:
        print("⚠️  Problem reading data file, creating fresh one...")
        return {"readings": [], "last_updated": "", "total_entries": 0}

def save_data(data):
    """Save data back to JSON file - handles errors gracefully"""
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except:
        print("❌ Error saving data! Please check file permissions.")
        return False

def get_threshold():
    """Get alert threshold from file - default is 1.5 if file missing"""
    try:
        if os.path.exists('threshold.txt'):
            with open('threshold.txt', 'r') as file:
                return float(file.read().strip())
        else:
            return 1.5  # Default threshold
    except:
        print("⚠️  Problem reading threshold, using default 1.5 meters")
        return 1.5

def set_threshold(value):
    """Set new threshold value and save to file"""
    try:
        with open('threshold.txt', 'w') as file:
            file.write(str(value))
        print(f"✅ Threshold set to {value} meters")
        return True
    except:
        print("❌ Error setting threshold!")
        return False

def add_reading(city, level):
    """Add new water level reading with automatic timestamp"""
    try:
        # Load existing data
        data = load_data()

        # Get current time in readable format
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Create new reading entry
        new_reading = {
            "city": city,
            "level": float(level),
            "timestamp": timestamp,
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S")
        }

        # Add to data
        data["readings"].append(new_reading)
        data["last_updated"] = timestamp
        data["total_entries"] += 1

        # Save data
        if save_data(data):
            print(f"✅ Water level recorded: {city} - {level}m at {timestamp}")

            # Check if threshold exceeded
            threshold = get_threshold()
            if float(level) > threshold:
                print(f"🚨 WARNING: Water level {level}m exceeds threshold {threshold}m!")
                print(f"🚨 ALERT: High water level detected in {city}!")

            return True
        else:
            return False

    except ValueError:
        print("❌ Error: Water level must be a number!")
        return False
    except:
        print("❌ Unexpected error while adding reading!")
        return False

def list_readings():
    """Show all recorded water levels in a nice format"""
    try:
        data = load_data()
        readings = data["readings"]

        if not readings:
            print("📋 No water level readings found yet!")
            print("💡 Add your first reading using: python main.py add --city YourCity --level 1.5")
            return

        print(f"\n📊 Water Level Readings (Total: {len(readings)})")
        print("-" * 60)

        for i, reading in enumerate(readings, 1):
            city = reading["city"]
            level = reading["level"]
            timestamp = reading["timestamp"]
            print(f"{i}. {city}: {level}m on {timestamp}")

        print("-" * 60)
        print(f"Last updated: {data['last_updated']}")

    except:
        print("❌ Error displaying readings!")

def generate_graph(days=7):
    """Create a graph showing water level trends over time"""
    try:
        data = load_data()
        readings = data["readings"]

        if not readings:
            print("📋 No data available for graph!")
            print("💡 Add some readings first using: python main.py add")
            return

        # Filter readings by days
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        recent_readings = []

        for reading in readings:
            reading_date = datetime.datetime.strptime(reading["timestamp"], "%Y-%m-%d %H:%M:%S")
            if reading_date >= cutoff_date:
                recent_readings.append(reading)

        if not recent_readings:
            print(f"📋 No readings found in last {days} days!")
            return

        # Prepare data for plotting
        dates = []
        levels = []
        cities = []

        for reading in recent_readings:
            dates.append(datetime.datetime.strptime(reading["timestamp"], "%Y-%m-%d %H:%M:%S"))
            levels.append(reading["level"])
            cities.append(reading["city"])

        # Create the graph
        plt.figure(figsize=(12, 6))
        plt.plot(dates, levels, marker='o', linewidth=2, markersize=6)
        plt.title(f'Water Level Trend - Last {days} Days', fontsize=16, fontweight='bold')
        plt.xlabel('Date & Time', fontsize=12)
        plt.ylabel('Water Level (meters)', fontsize=12)
        plt.grid(True, alpha=0.3)

        # Add threshold line
        threshold = get_threshold()
        plt.axhline(y=threshold, color='red', linestyle='--', alpha=0.7, label=f'Threshold: {threshold}m')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()

        # Save graph
        plt.savefig('reports/water_level_graph.png', dpi=300, bbox_inches='tight')
        plt.show()

        print(f"✅ Graph generated for last {days} days!")
        print("📁 Graph saved as: reports/water_level_graph.png")

    except ImportError:
        print("❌ Matplotlib not installed! Run: pip install matplotlib")
    except:
        print("❌ Error generating graph!")

def generate_report():
    """Create a detailed text report of all readings"""
    try:
        data = load_data()
        readings = data["readings"]

        if not readings:
            print("📋 No data available for report!")
            return

        # Create report content
        report_content = []
        report_content.append("🌊 WATER LEVEL MONITORING REPORT")
        report_content.append("=" * 50)
        report_content.append(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_content.append(f"Total readings: {len(readings)}")
        report_content.append(f"Alert threshold: {get_threshold()}m")
        report_content.append("")

        # Add summary statistics
        levels = [r["level"] for r in readings]
        report_content.append("📊 SUMMARY STATISTICS:")
        report_content.append(f"Highest level: {max(levels)}m")
        report_content.append(f"Lowest level: {min(levels)}m")
        report_content.append(f"Average level: {sum(levels)/len(levels):.2f}m")
        report_content.append("")

        # Add all readings
        report_content.append("📋 ALL READINGS:")
        report_content.append("-" * 50)

        for i, reading in enumerate(readings, 1):
            city = reading["city"]
            level = reading["level"]
            timestamp = reading["timestamp"]
            alert = " ⚠️ ABOVE THRESHOLD" if level > get_threshold() else ""
            report_content.append(f"{i}. {city}: {level}m on {timestamp}{alert}")

        # Save report to file
        report_text = "\n".join(report_content)
        with open('reports/water_level_report.txt', 'w') as file:
            file.write(report_text)

        print("✅ Report generated successfully!")
        print("📁 Report saved as: reports/water_level_report.txt")
        print("\n" + "=" * 30)
        print("📋 QUICK SUMMARY:")
        print(f"Total readings: {len(readings)}")
        print(f"Highest level: {max(levels)}m")
        print(f"Average level: {sum(levels)/len(levels):.2f}m")
        print("=" * 30)

    except:
        print("❌ Error generating report!")

def main():
    """Main function that handles command line arguments and calls appropriate functions"""

    # Create parser for command line arguments
    parser = argparse.ArgumentParser(description='🌊 Community Water Level Monitor')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add reading command
    add_parser = subparsers.add_parser('add', help='Add new water level reading')
    add_parser.add_argument('--city', required=True, help='City or location name')
    add_parser.add_argument('--level', required=True, help='Water level in meters')

    # List readings command
    subparsers.add_parser('list', help='Show all recorded readings')

    # Generate graph command
    graph_parser = subparsers.add_parser('graph', help='Generate water level trend graph')
    graph_parser.add_argument('--days', type=int, default=7, help='Number of days to show (default: 7)')

    # Generate report command
    subparsers.add_parser('report', help='Generate detailed text report')

    # Threshold command
    threshold_parser = subparsers.add_parser('threshold', help='Set alert threshold')
    threshold_parser.add_argument('--set', type=float, help='Set threshold value in meters')
    threshold_parser.add_argument('--show', action='store_true', help='Show current threshold')

    # Parse arguments
    args = parser.parse_args()

    # Handle different commands
    if args.command == 'add':
        add_reading(args.city, args.level)

    elif args.command == 'list':
        list_readings()

    elif args.command == 'graph':
        generate_graph(args.days)

    elif args.command == 'report':
        generate_report()

    elif args.command == 'threshold':
        if args.set:
            set_threshold(args.set)
        elif args.show:
            current = get_threshold()
            print(f"Current threshold: {current}m")
        else:
            current = get_threshold()
            print(f"Current threshold: {current}m")
            print("Use --set VALUE to change threshold")

    else:
        # Show help if no command provided
        print("🌊 Water Level Monitor - Community Safety Tool")
        print("\nAvailable commands:")
        print("  add --city CITY --level LEVEL    Add water level reading")
        print("  list                             Show all readings")
        print("  graph --days DAYS                Generate trend graph")
        print("  report                           Generate detailed report")
        print("  threshold --set VALUE            Set alert threshold")
        print("\nExample: python main.py add --city Prayagraj --level 1.7")

if __name__ == "__main__":
    main()