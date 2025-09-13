#W7A1_p2-optimize_code.py
# Improved code with Singleton pattern for database connection

import threading
import time
import sqlite3

class SingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = sqlite3.connect('app.db', check_same_thread=False)

    def get_connection(self):
        return self.connection


class UserService:

    # #fetch user by id
    def get_user(self, user_id):
        singleton = Singleton()
        conn = singleton.get_connection() # Reuse Connection
        cursor = conn.cursor()
        cursor.execute("Select * from users where id = ?", (user_id,))
        result = cursor.fetchone()
        return result
 
    
class OrderService:

    def get_orders(self, user_id):
        singleton = Singleton()
        conn = singleton.get_connection() # Reuse Connection
        cursor = conn.cursor()
        cursor.execute("Select * from orders where id = ?", (user_id,))
        result = cursor.fetchone()
        return result

# Print how long it took to process
import time
start_time = time.time()
user_service = UserService()
order_service = OrderService()
user = user_service.get_user(1)
orders = order_service.get_orders(1)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")



