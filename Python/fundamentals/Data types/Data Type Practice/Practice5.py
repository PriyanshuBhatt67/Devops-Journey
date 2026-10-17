#5.Create a dictionary representing a server with its hostname, port, and running status.

# Create a dictionary representing a server
server = {
    "hostname": "web-server-01",
    "port": 8080,
    "running": True
}

# Print the entire server dictionary
print(server)

# Access and print individual values
print("Hostname:", server["hostname"])
print("Port:", server["port"])
print("Running Status:", server["running"]) # OR can also write as

print(f"hostname : {server['hostname']}")
print(f"port     : {server['port']}")
print(f"running status : {server['running']}")
print(server.get("ip", "N/A"))   # safe access: 'N/A' (key missing)

