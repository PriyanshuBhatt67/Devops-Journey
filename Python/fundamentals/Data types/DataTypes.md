# Python Data Types – Complete Guide
### DevOps Journey | Python Fundamentals

> File: `DataTypes.md`  
> Goal: Cover the core concepts of Python Data Types with practical DevOps examples.

---

## 1. What are Data Types?

A **data type** tells Python what kind of value a variable is holding and what operations can be performed on it.

In DevOps automation we constantly work with:

| Need                        | Recommended Type |
|----------------------------|------------------|
| Server names, paths, logs  | `str`            |
| Ports, counts, exit codes  | `int`            |
| CPU / Memory percentages   | `float`          |
| Status flags               | `bool`           |
| List of servers / packages | `list`           |
| Configuration / inventory  | `dict`           |
| Unique hosts / tags        | `set`            |
| Missing / optional values  | `None`           |

---

## 2. All Built-in Data Types Overview

| Category   | Data Types                  | Mutable?          | Example Use in DevOps              |
|------------|-----------------------------|-------------------|------------------------------------|
| Numeric    | `int`, `float`, `complex`   | No                | Ports, CPU%, latency               |
| Text       | `str`                       | No                | Hostname, path, log message        |
| Boolean    | `bool`                      | No                | is_running, debug_mode             |
| Sequence   | `list`, `tuple`, `range`    | list = Yes<br>tuple = No | Server list, fixed config   |
| Mapping    | `dict`                      | Yes               | Config, inventory, API response    |
| Set        | `set`, `frozenset`          | set = Yes         | Unique hosts, packages             |
| Binary     | `bytes`, `bytearray`        | bytearray = Yes   | File content, network data         |
| None       | `NoneType`                  | –                 | Missing / optional value           |

---

## 3. Numeric Types

### 3.1 Integer (`int`)

Used for whole numbers: ports, counts, exit codes, retries.

```python
port = 8080
max_retries = 3
exit_code = 0
server_count = 15

print(type(port))           # <class 'int'>
print(port * 2)             # 16160
print(15 // 2)              # 7  (floor division)
print(15 % 2)               # 1  (remainder)
```

### 3.2 Float (`float`)

Used for decimal numbers: CPU percentage, memory, latency, disk space.

```python
cpu_usage = 67.5
memory_gb = 15.75
latency = 23.4

print(round(cpu_usage, 1))
print(f"CPU: {cpu_usage}%")
```

### 3.3 Complex (rarely used in DevOps)

```python
z = 3 + 4j
print(z.real, z.imag)       # 3.0  4.0
```

---

## 4. Boolean (`bool`)

Used for flags and conditions.

```python
is_running = True
debug = False
is_healthy = cpu_usage < 80

print(type(is_running))     # <class 'bool'>
```

### Truthy vs Falsy Values

| Falsy Values                                      | Truthy Values             |
|---------------------------------------------------|---------------------------|
| `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None` | Almost everything else |

```python
print(bool(0))          # False
print(bool(""))         # False
print(bool("hello"))    # True
print(bool([1, 2]))     # True
```

---

## 5. String (`str`)

Strings are **immutable**.

```python
hostname = "web-prod-01"
path = "/var/log/nginx/access.log"
region = "us-east-1"
```

### Useful String Methods

```python
print(hostname.upper())                 # WEB-PROD-01
print(hostname.lower())
print(hostname.startswith("web"))       # True
print(hostname.endswith("01"))          # True
print(path.split("/"))                  # ['', 'var', 'log', ...]
print(region.replace("us", "ap"))       # ap-east-1
print(len(hostname))
print("prod" in hostname)               # True
```

### f-strings (Most Important)

```python
print(f"Server {hostname} is running in {region}")
print(f"CPU Usage: {cpu_usage}%")
```

---

## 6. List (`list`) – Mutable

Perfect for collections of servers, packages, ports, etc.

```python
servers = ["web-01", "web-02", "db-01"]
ports = [80, 443, 8080]
```

### Common List Operations

```python
servers.append("cache-01")          # add at end
servers.insert(0, "lb-01")          # add at position
servers.remove("web-02")            # remove by value
servers.pop()                       # remove last item

print(servers[0])                   # indexing
print(servers[-1])                  # last item
print(len(servers))
print("db-01" in servers)

# Slicing
print(servers[1:3])

# List Comprehension
upper_servers = [s.upper() for s in servers]
```

---

## 7. Tuple (`tuple`) – Immutable

Use when the data should **not** change.

```python
db_config = ("localhost", 5432, "mydb")
http_ok = (200, 201, 204)

print(db_config[1])         # 5432
# db_config[1] = 3306      → Error (immutable)
```

**When to use Tuple:**
- Fixed configuration
- Return multiple values from a function
- Dictionary keys

---

## 8. Dictionary (`dict`) – Most Important for DevOps

```python
server = {
    "hostname": "app-01",
    "ip": "10.0.1.15",
    "port": 8080,
    "role": "backend",
    "healthy": True,
    "cpu": 45.2
}
```

### Common Dictionary Operations

```python
print(server["hostname"])
print(server.get("region", "unknown"))     # safe access

server["memory"] = 16                      # add
server["healthy"] = False                  # update
del server["cpu"]                          # delete

print(server.keys())
print(server.values())
print(server.items())

for key, value in server.items():
    print(f"{key} → {value}")
```

---

## 9. Set (`set`) – Unique Values

```python
hosts = {"web-01", "web-02", "db-01", "web-01"}  # duplicate removed
packages = {"nginx", "python3", "curl"}

hosts.add("cache-01")
hosts.discard("web-02")

print("web-01" in hosts)
```

### Set Operations

```python
a = {"web-01", "web-02", "db-01"}
b = {"web-01", "api-01"}

print(a | b)        # Union
print(a & b)        # Intersection
print(a - b)        # Difference
print(a ^ b)        # Symmetric difference
```

---

## 10. NoneType (`None`)

Represents “no value” or “empty”.

```python
result = None

if result is None:
    print("No result available")
```

> Always use `is None` or `is not None` (never `== None`).

---

## 11. Type Checking & Conversion

```python
value = "8080"

print(type(value))                  # <class 'str'>
print(isinstance(value, str))       # True

# Conversions
port = int("8080")
cpu = float("67.5")
text = str(404)
flag = bool(1)
```

### Safe Conversion

```python
user_input = "8080"

try:
    port = int(user_input)
    print(f"Valid port: {port}")
except ValueError:
    print("Invalid port number")
```

---

## 12. Mutable vs Immutable (Very Important)

| Mutable (can change)       | Immutable (cannot change)                     |
|----------------------------|-----------------------------------------------|
| `list`, `dict`, `set`      | `int`, `float`, `str`, `tuple`, `bool`, `frozenset` |

```python
# Mutable example
a = [1, 2, 3]
b = a
a.append(4)
print(b)            # [1, 2, 3, 4]  ← both changed

# Immutable example
x = "hello"
y = x
x = "world"
print(y)            # hello  ← y still points to old object
```

---

## 13. Membership & Identity Operators

```python
servers = ["web-01", "db-01"]

print("web-01" in servers)       # Membership → True
print("api-01" not in servers)

a = [1, 2]
b = a
c = [1, 2]

print(a is b)       # True   (same object)
print(a is c)       # False  (different objects)
print(a == c)       # True   (same value)
```

- `in` / `not in` → check membership
- `is` / `is not` → check identity (same object in memory)
- `==` / `!=` → check value equality

---

## 17. Quick Reference Cheat Sheet

```python
# Checking types
type(x)
isinstance(x, int)

# Conversions
int()   float()   str()   bool()
list()  tuple()   dict()  set()

# List methods
.append()   .insert()   .remove()   .pop()   .extend()

# Dict methods
.get()   .keys()   .values()   .items()   .update()

# Set operations
.add()   .discard()
|   &   -   ^          # union, intersection, difference, symmetric difference

# Useful operators
in / not in            # membership
is / is not            # identity
== / !=                # equality
```

---

**Keep building consistently.**  
Small daily progress > occasional long sessions.
```
