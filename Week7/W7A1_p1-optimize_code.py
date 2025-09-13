#W7A1_p1-optimize_code.py
# Original code with inefficiencies

import time
import sqlite3

class UserService:

    def get_user(self, user_id):
        conn = sqlite3.connect('app.db') # New Connection
        cursor = conn.cursor()
        cursor.execute("Select * from users where id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result

    
class OrderService:

    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db') # New Connection
        cursor = conn.cursor()
        cursor.execute("Select * from orders where id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
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



