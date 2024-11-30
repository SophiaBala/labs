class CafeQueue:
    def __init__(self):
        self.vip_queue = []
        self.regular_queue = []
        self.order_of_arrival = []

    def add_client(self, client_name, is_vip=False, ordered_ice_cream=False):
        self.order_of_arrival.append(
            (client_name, "VIP" if is_vip else "Regular", "Ice Cream" if ordered_ice_cream else "No Ice Cream"))

        if is_vip or ordered_ice_cream:
            self.vip_queue.append(client_name)
        else:
            self.regular_queue.append(client_name)

    def serve_client(self):
        if self.vip_queue:
            return self.vip_queue.pop(0)
        elif self.regular_queue:
            return self.regular_queue.pop(0)
        else:
            return "Черга порожня"

    def display_order_of_arrival(self):
        return self.order_of_arrival

    def display_queues(self):
        return {
            "VIP Queue": self.vip_queue,
            "Regular Queue": self.regular_queue
        }

cafe = CafeQueue()

cafe.add_client("John")
cafe.add_client("Alice", is_vip=True)
cafe.add_client("Bob")
cafe.add_client("Diana", is_vip=True)
cafe.add_client("Eve", ordered_ice_cream=True)
cafe.add_client("Charlie", ordered_ice_cream=True)

print("Порядок за відвідуванням:")
for client, status, ice_cream in cafe.display_order_of_arrival():
    print(f"Клієнт: {client}, Статус: {status}, Замовлення: {ice_cream}")

print("\nОбслуговування клієнтів у порядку пріоритету:")
while True:
    served_client = cafe.serve_client()
    if served_client == "Черга порожня":
        print(served_client)
        break
    else:
        print(f"Обслуговується: {served_client}")

print("\nСтан черг після обслуговування:")
queues = cafe.display_queues()
print(f"VIP Queue: {queues['VIP Queue']}")
print(f"Regular Queue: {queues['Regular Queue']}")
