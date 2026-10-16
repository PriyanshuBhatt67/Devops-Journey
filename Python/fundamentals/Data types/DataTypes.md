# Python Data Types – Complete Guide
### DevOps Journey | Python Fundamentals

> File: `DataTypes.md`  
> Goal: Cover almost all important concepts of Python Data Types with practical DevOps examples.

---

## 1. What are Data Types?

A **data type** tells Python what kind of value a variable is holding and what operations can be performed on it.

In DevOps automation we constantly work with:
- Server names → `str`
- Ports & counts → `int`
- CPU / Memory → `float`
- Status flags → `bool`
- List of servers → `list`
- Configuration → `dict`
- Unique values → `set`

---

## 2. All Built-in Data Types Overview

| Category       | Data Types                  | Mutable? | Example Use in DevOps              |
|----------------|-----------------------------|----------|------------------------------------|
| Numeric        | `int`, `float`, `complex`   | No       | Ports, CPU%, latency               |
| Text           | `str`                       | No       | Hostname, path, log message        |
| Boolean        | `bool`                      | No       | is_running, debug_mode             |
| Sequence       | `list`, `tuple`, `range`    | list=Yes | Server list, fixed config          |
| Mapping        | `dict`                      | Yes      | Config, inventory, API response    |
| Set            | `set`, `frozenset`          | set=Yes  | Unique hosts, packages             |
| Binary         | `bytes`, `bytearray`        | bytearray=Yes | File content, network data    |
| None           | `NoneType`                  | –        | Missing / optional value           |

---

## 3. Numeric Types

### 3.1 Integer (`int`)

```python
port = 8080
max_retries = 3
exit_code = 0
server_count = 15

print(type(port))           # <class 'int'>
print(port * 2)             # 16160
print(15 // 2)              # 7 (floor division)
print(15 % 2)               # 1 (remainder)
### 3.2 Float (`float`)
cpu_usage = 67.5
memory_gb = 15.75
latency = 23.4

print(round(cpu_usage, 1))
print(f"CPU: {cpu_usage}%")

### 3.3 Complex (`rarely used in DevOps`)
z = 3 + 4j
print(z.real, z.imag)

## 4. Boolean (`bool`)
is_running = True
debug = False
is_healthy = cpu_usage < 80

print(type(is_running))     # <class 'bool'>