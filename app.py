import yaml

# Load the YAML configuration file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access configuration values
print(f"Database host: {config['database']['host']}")
print(f"Server port: {config['server']['port']}")

# You can use these values in your application
db_connection_string = f"postgresql://{config['database']['username']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['dbname']}"
print(f"Connection string: {db_connection_string}")