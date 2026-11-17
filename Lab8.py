from dataclasses import dataclass


@dataclass
class Client:
    id: int
    name: str


@dataclass
class Order:
    number: int
    clientId: int
    sum: int


clients = [
    Client(101, "Коваленко"),
    Client(102, "Мельник"),
    Client(103, "Шевчук"),
    Client(104, "Бондар"),
    Client(105, "Ткачук"),
    Client(106, "Гриценко"),
]

orders = [
    Order(1, 103, 450),
    Order(2, 101, 120),
    Order(3, 105, 980),
    Order(4, 103, 300),
    Order(5, 102, 75),
    Order(6, 106, 1500),
    Order(7, 101, 220),
    Order(8, 103, 60),
]

blocked = [102, 104]

# --- Фрагмент 1 (старий варіант) ---
# for order in orders:
#     for client in clients:
#         if client.id == order.clientId:
#             print(f"Замовлення {order.number} - {client.name}")

# --- Фрагмент 1 (новий варіант: словник) ---
clients_by_id = {client.id: client for client in clients}
for order in orders:
    print(f"Замовлення {order.number} - {clients_by_id[order.clientId].name}")

print()

# --- Фрагмент 2 (старий варіант) ---
# total = 0
# for order in orders:
#     if order.clientId not in blocked:
#         total += order.sum
# print(f"Сума прийнятих замовлень: {total}")

# --- Фрагмент 2 (новий варіант: множина) ---
blocked_set = set(blocked)
total = 0
for order in orders:
    if order.clientId not in blocked_set:
        total += order.sum
print(f"Сума прийнятих замовлень: {total}")

print()

# --- Фрагмент 3 (старий варіант) ---
# counted = []
# for order in orders:
#     if order.clientId in counted:
#         continue
#     count = 0
#     for other in orders:
#         if other.clientId == order.clientId:
#             count += 1
#     counted.append(order.clientId)
#     print(f"{order.clientId}: {count}")

# --- Фрагмент 3 (новий варіант: словник) ---
counts_by_client = {}
for order in orders:
    counts_by_client[order.clientId] = counts_by_client.get(order.clientId, 0) + 1

seen = set()
for order in orders:
    if order.clientId not in seen:
        seen.add(order.clientId)
        print(f"{order.clientId}: {counts_by_client[order.clientId]}")

print()

# --- Фрагмент 4 (без змін — нова структура не потрібна) ---
best = orders[0]
for order in orders:
    if order.sum > best.sum:
        best = order
print(f"Найбільше замовлення: {best.sum}")

print()

# --- Фрагмент 5 (без змін — помилковий приклад у методичці, нова структура не потрібна) ---
for order in orders:
    byId = {}
    for client in clients:
        byId[client.id] = client
    print(f"Замовлення {order.number} - {byId[order.clientId].name}")