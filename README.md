# TaxiHub - Taxi Management CLI Application

**TaxiHub** is a command-line interface (CLI) application designed to simplify the management of a taxi company. It provides essential functionalities for adding and listing drivers, vehicles, and trips, as well as calculating fares. This tool is ideal for taxi companies looking for an organized and efficient way to manage their resources.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use TaxiHub, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:Abduljr0/phase3-final-project.git
   cd app
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database:**
   ```bash
   python seed.py
   ```

## Usage

After installation, you can run TaxiHub by executing the following command:

```bash
python main.py
```

This will start the CLI application, and you will be prompted to choose from a list of available commands.

## Commands

TaxiHub supports the following commands:

- `add_driver`: Add a new driver to the system.
- `list_drivers`: List all registered drivers.
- `add_vehicle`: Add a new vehicle to the system.
- `list_vehicles`: List all registered vehicles.
- `start_trip`: Start a new trip by assigning a driver and a vehicle.
- `complete_trip`: Complete an ongoing trip by entering the trip ID.
- `calculate_fare`: Calculate the fare for a completed trip.
- `list_trips`: List all recorded trips.

Each command has specific prompts to guide the user through the required inputs.

## Database

TaxiHub uses an SQLite database (`taxi_database.db`) to store and manage data related to drivers, vehicles, and trips. The database is automatically created and initialized during the installation process.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [ Apache License](LICENSE).

---
