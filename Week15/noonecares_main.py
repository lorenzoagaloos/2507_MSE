# Auckland North Yoobee - Car Rental System (ANY-CRS)
# Main Application File
# Developed by: [Student Name] - Master's in Software Engineering
# Date: September 2025
# 
# This is the main file that runs our car rental system
# It handles user interface and connects all parts together

import sqlite3
from datetime import datetime, timedelta
import hashlib
import os

class Database:
    """
    This class handles all database operations
    I'm using SQLite because it's simple and doesn't need server setup
    """
    
    def __init__(self):
        self.db_name = 'car_rental.db'
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                full_name TEXT,
                email TEXT,
                phone TEXT
            )
        ''')
        
        # Create cars table with pet-friendly feature
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                mileage INTEGER,
                available INTEGER DEFAULT 1,
                min_rent_days INTEGER DEFAULT 1,
                max_rent_days INTEGER DEFAULT 30,
                daily_rate REAL NOT NULL,
                pet_friendly INTEGER DEFAULT 0
            )
        ''')
        
        # Create bookings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                car_id INTEGER,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                total_cost REAL,
                status TEXT DEFAULT 'pending',
                pet_included INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (car_id) REFERENCES cars (id)
            )
        ''')
        
        # Insert default admin user if not exists
        cursor.execute('SELECT * FROM users WHERE username = ?', ('admin',))
        if not cursor.fetchone():
            admin_password = self.hash_password('admin123')
            cursor.execute('''
                INSERT INTO users (username, password, role, full_name, email)
                VALUES (?, ?, ?, ?, ?)
            ''', ('admin', admin_password, 'admin', 'System Administrator', 'admin@any-crs.com'))
        
        # Insert some sample cars if table is empty
        cursor.execute('SELECT COUNT(*) FROM cars')
        if cursor.fetchone()[0] == 0:
            sample_cars = [
                ('Toyota', 'Corolla', 2022, 15000, 1, 1, 14, 45.0, 1),
                ('Honda', 'Civic', 2021, 22000, 1, 1, 21, 50.0, 0),
                ('Ford', 'Explorer', 2023, 8000, 1, 3, 30, 75.0, 1),
                ('Nissan', 'Altima', 2020, 35000, 1, 1, 14, 40.0, 0),
                ('Subaru', 'Outback', 2022, 12000, 1, 2, 28, 65.0, 1)
            ]
            cursor.executemany('''
                INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate, pet_friendly)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', sample_cars)
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hash password for security - simple but effective"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            conn.close()
            return results
        else:
            conn.commit()
            conn.close()
            return cursor.rowcount

class User:
    """
    User class to handle user information and authentication
    This represents both customers and admin users
    """
    
    def __init__(self, username, role, full_name=None, email=None):
        self.username = username
        self.role = role
        self.full_name = full_name
        self.email = email
        self.is_logged_in = False

class Car:
    """
    Car class to represent rental cars in our system
    Each car has properties like make, model, and our special pet-friendly feature
    """
    
    def __init__(self, car_id, make, model, year, mileage, available, min_rent, max_rent, daily_rate, pet_friendly):
        self.id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent_days = min_rent
        self.max_rent_days = max_rent
        self.daily_rate = daily_rate
        self.pet_friendly = pet_friendly
    
    def display_info(self):
        """Display car information in a nice format"""
        pet_status = "Pet Friendly ✓" if self.pet_friendly else "No Pets ✗"
        availability = "Available" if self.available else "Rented"
        
        return f"""
Car ID: {self.id}
{self.year} {self.make} {self.model}
Mileage: {self.mileage:,} km
Daily Rate: ${self.daily_rate:.2f}
Rental Period: {self.min_rent_days}-{self.max_rent_days} days
{pet_status}
Status: {availability}
"""

class Booking:
    """
    Booking class to handle rental reservations
    This manages the relationship between users, cars, and rental periods
    """
    
    def __init__(self, booking_id, user_id, car_id, start_date, end_date, total_cost, status, pet_included=False):
        self.id = booking_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.status = status
        self.pet_included = pet_included

class CarRentalSystem:
    """
    Main system class - this is where everything comes together
    It's like the brain of our car rental application
    """
    
    def __init__(self):
        self.db = Database()
        self.current_user = None
        self.running = True
    
    def start(self):
        """Main application loop"""
        print("=" * 50)
        print("Welcome to Auckland North Yoobee Car Rental System")
        print("ANY-CRS - Your Trusted Car Rental Partner")
        print("=" * 50)
        
        while self.running:
            if self.current_user is None:
                self.show_login_menu()
            else:
                if self.current_user.role == 'admin':
                    self.show_admin_menu()
                else:
                    self.show_customer_menu()
    
    def show_login_menu(self):
        """Display login/registration options"""
        print("\n1. Login")
        print("2. Register as Customer") 
        print("3. Exit")
        
        choice = input("\nPlease select an option (1-3): ").strip()
        
        if choice == '1':
            self.login()
        elif choice == '2':
            self.register_customer()
        elif choice == '3':
            print("Thank you for using ANY-CRS!")
            self.running = False
        else:
            print("Invalid choice. Please try again.")
    
    def login(self):
        """Handle user login"""
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        hashed_password = self.db.hash_password(password)
        
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        result = self.db.execute_query(query, (username, hashed_password))
        
        if result:
            user_data = result[0]
            self.current_user = User(user_data[1], user_data[3], user_data[4], user_data[5])
            print(f"\nWelcome back, {self.current_user.full_name or self.current_user.username}!")
        else:
            print("Invalid username or password. Please try again.")
    
    def register_customer(self):
        """Register new customer"""
        print("\n--- Customer Registration ---")
        
        username = input("Choose a username: ").strip()
        
        # Check if username already exists
        query = "SELECT * FROM users WHERE username = ?"
        if self.db.execute_query(query, (username,)):
            print("Username already exists. Please choose another one.")
            return
        
        password = input("Choose a password: ").strip()
        full_name = input("Enter your full name: ").strip()
        email = input("Enter your email: ").strip()
        phone = input("Enter your phone number: ").strip()
        
        hashed_password = self.db.hash_password(password)
        
        query = '''
            INSERT INTO users (username, password, role, full_name, email, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        
        if self.db.execute_query(query, (username, hashed_password, 'customer', full_name, email, phone)):
            print("Registration successful! You can now login.")
        else:
            print("Registration failed. Please try again.")
    
    def show_customer_menu(self):
        """Display customer menu options"""
        print(f"\n--- Customer Portal ({self.current_user.username}) ---")
        print("1. View Available Cars")
        print("2. Book a Car")
        print("3. View My Bookings") 
        print("4. Logout")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            self.view_available_cars()
        elif choice == '2':
            self.book_car()
        elif choice == '3':
            self.view_my_bookings()
        elif choice == '4':
            self.logout()
        else:
            print("Invalid choice. Please try again.")
    
    def show_admin_menu(self):
        """Display admin menu options"""
        print(f"\n--- Admin Portal ({self.current_user.username}) ---")
        print("1. View All Cars")
        print("2. Add New Car")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. Manage Bookings")
        print("6. View All Users")
        print("7. Logout")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == '1':
            self.view_all_cars()
        elif choice == '2':
            self.add_car()
        elif choice == '3':
            self.update_car()
        elif choice == '4':
            self.delete_car()
        elif choice == '5':
            self.manage_bookings()
        elif choice == '6':
            self.view_all_users()
        elif choice == '7':
            self.logout()
        else:
            print("Invalid choice. Please try again.")
    
    def view_available_cars(self):
        """Show available cars to customers"""
        print("\n--- Available Cars ---")
        
        # Ask if they want pet-friendly cars
        pet_filter = input("\nDo you need a pet-friendly car? (y/n): ").lower()
        
        if pet_filter == 'y':
            query = "SELECT * FROM cars WHERE available = 1 AND pet_friendly = 1"
            print("\nShowing pet-friendly cars only:")
        else:
            query = "SELECT * FROM cars WHERE available = 1"
            print("\nShowing all available cars:")
        
        cars = self.db.execute_query(query)
        
        if not cars:
            print("Sorry, no cars match your criteria.")
            return
        
        for car_data in cars:
            car = Car(*car_data)
            print(car.display_info())
            print("-" * 30)
    
    def book_car(self):
        """Handle car booking process"""
        print("\n--- Book a Car ---")
        
        # Show available cars first
        self.view_available_cars()
        
        try:
            car_id = int(input("\nEnter Car ID to book: "))
            
            # Check if car exists and is available
            query = "SELECT * FROM cars WHERE id = ? AND available = 1"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("Car not found or not available.")
                return
            
            car = Car(*car_data[0])
            
            # Get rental dates
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            
            # Simple date validation
            try:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                end = datetime.strptime(end_date, "%Y-%m-%d")
                
                if start >= end or start < datetime.now():
                    print("Invalid dates. Start date must be today or later, and end date must be after start date.")
                    return
                    
                days = (end - start).days
                
                if days < car.min_rent_days or days > car.max_rent_days:
                    print(f"Rental period must be between {car.min_rent_days} and {car.max_rent_days} days for this car.")
                    return
                    
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
            
            # Ask about pets if car is pet-friendly
            pet_included = 0
            if car.pet_friendly:
                pet_choice = input("Will you be bringing pets? (y/n): ").lower()
                pet_included = 1 if pet_choice == 'y' else 0
            
            # Calculate total cost
            total_cost = days * car.daily_rate
            
            # Add pet fee if applicable
            if pet_included:
                pet_fee = 15.0 * days  # $15 per day pet fee
                total_cost += pet_fee
                print(f"Pet fee: ${pet_fee:.2f} (${15.0}/day)")
            
            print(f"\nBooking Summary:")
            print(f"Car: {car.year} {car.make} {car.model}")
            print(f"Dates: {start_date} to {end_date} ({days} days)")
            print(f"Total Cost: ${total_cost:.2f}")
            
            confirm = input("\nConfirm booking? (y/n): ").lower()
            
            if confirm == 'y':
                # Get user ID
                user_query = "SELECT id FROM users WHERE username = ?"
                user_result = self.db.execute_query(user_query, (self.current_user.username,))
                user_id = user_result[0][0]
                
                # Create booking
                booking_query = '''
                    INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, pet_included)
                    VALUES (?, ?, ?, ?, ?, ?)
                '''
                
                if self.db.execute_query(booking_query, (user_id, car_id, start_date, end_date, total_cost, pet_included)):
                    print("Booking request submitted successfully!")
                    print("Your booking is pending admin approval.")
                else:
                    print("Booking failed. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid car ID.")
    
    def view_my_bookings(self):
        """Show customer's bookings"""
        print("\n--- My Bookings ---")
        
        # Get user ID
        user_query = "SELECT id FROM users WHERE username = ?"
        user_result = self.db.execute_query(user_query, (self.current_user.username,))
        user_id = user_result[0][0]
        
        # Get bookings with car info
        query = '''
            SELECT b.id, b.start_date, b.end_date, b.total_cost, b.status, b.pet_included,
                   c.make, c.model, c.year
            FROM bookings b
            JOIN cars c ON b.car_id = c.id
            WHERE b.user_id = ?
            ORDER BY b.id DESC
        '''
        
        bookings = self.db.execute_query(query, (user_id,))
        
        if not bookings:
            print("You have no bookings yet.")
            return
        
        for booking in bookings:
            pet_info = " (with pets)" if booking[5] else ""
            print(f"""
Booking ID: {booking[0]}
Car: {booking[8]} {booking[6]} {booking[7]}
Dates: {booking[1]} to {booking[2]}
Total Cost: ${booking[3]:.2f}{pet_info}
Status: {booking[4].upper()}
""")
            print("-" * 30)
    
    def view_all_cars(self):
        """Admin view of all cars"""
        print("\n--- All Cars ---")
        
        query = "SELECT * FROM cars ORDER BY id"
        cars = self.db.execute_query(query)
        
        for car_data in cars:
            car = Car(*car_data)
            print(car.display_info())
            print("-" * 30)
    
    def add_car(self):
        """Admin function to add new car"""
        print("\n--- Add New Car ---")
        
        try:
            make = input("Car Make: ").strip()
            model = input("Car Model: ").strip()
            year = int(input("Year: "))
            mileage = int(input("Mileage (km): "))
            min_rent = int(input("Minimum rental days: "))
            max_rent = int(input("Maximum rental days: "))
            daily_rate = float(input("Daily rate ($): "))
            
            pet_friendly = input("Pet friendly? (y/n): ").lower()
            pet_friendly = 1 if pet_friendly == 'y' else 0
            
            query = '''
                INSERT INTO cars (make, model, year, mileage, min_rent_days, max_rent_days, daily_rate, pet_friendly)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            if self.db.execute_query(query, (make, model, year, mileage, min_rent, max_rent, daily_rate, pet_friendly)):
                print("Car added successfully!")
            else:
                print("Failed to add car.")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    def update_car(self):
        """Admin function to update car details"""
        print("\n--- Update Car ---")
        
        try:
            car_id = int(input("Enter Car ID to update: "))
            
            query = "SELECT * FROM cars WHERE id = ?"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("Car not found.")
                return
            
            car = Car(*car_data[0])
            print("Current car details:")
            print(car.display_info())
            
            print("\nEnter new values (press Enter to keep current value):")
            
            make = input(f"Make [{car.make}]: ").strip() or car.make
            model = input(f"Model [{car.model}]: ").strip() or car.model
            year_input = input(f"Year [{car.year}]: ").strip()
            year = int(year_input) if year_input else car.year
            
            mileage_input = input(f"Mileage [{car.mileage}]: ").strip()
            mileage = int(mileage_input) if mileage_input else car.mileage
            
            rate_input = input(f"Daily Rate [{car.daily_rate}]: ").strip()
            daily_rate = float(rate_input) if rate_input else car.daily_rate
            
            available_input = input(f"Available (1=yes, 0=no) [{car.available}]: ").strip()
            available = int(available_input) if available_input else car.available
            
            pet_input = input(f"Pet Friendly (1=yes, 0=no) [{car.pet_friendly}]: ").strip()
            pet_friendly = int(pet_input) if pet_input else car.pet_friendly
            
            update_query = '''
                UPDATE cars 
                SET make=?, model=?, year=?, mileage=?, daily_rate=?, available=?, pet_friendly=?
                WHERE id=?
            '''
            
            if self.db.execute_query(update_query, (make, model, year, mileage, daily_rate, available, pet_friendly, car_id)):
                print("Car updated successfully!")
            else:
                print("Failed to update car.")
                
        except ValueError:
            print("Invalid input.")
    
    def delete_car(self):
        """Admin function to delete a car"""
        print("\n--- Delete Car ---")
        
        try:
            car_id = int(input("Enter Car ID to delete: "))
            
            # Check if car has active bookings
            booking_query = "SELECT COUNT(*) FROM bookings WHERE car_id = ? AND status = 'approved'"
            active_bookings = self.db.execute_query(booking_query, (car_id,))[0][0]
            
            if active_bookings > 0:
                print("Cannot delete car with active bookings.")
                return
            
            # Show car details before deletion
            query = "SELECT * FROM cars WHERE id = ?"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("Car not found.")
                return
            
            car = Car(*car_data[0])
            print("Car to delete:")
            print(car.display_info())
            
            confirm = input("Are you sure you want to delete this car? (y/n): ").lower()
            
            if confirm == 'y':
                delete_query = "DELETE FROM cars WHERE id = ?"
                if self.db.execute_query(delete_query, (car_id,)):
                    print("Car deleted successfully!")
                else:
                    print("Failed to delete car.")
        
        except ValueError:
            print("Invalid Car ID.")
    
    def manage_bookings(self):
        """Admin function to manage rental bookings"""
        print("\n--- Manage Bookings ---")
        
        # Show all pending bookings
        query = '''
            SELECT b.id, b.start_date, b.end_date, b.total_cost, b.status, b.pet_included,
                   c.make, c.model, c.year, u.full_name, u.username
            FROM bookings b
            JOIN cars c ON b.car_id = c.id
            JOIN users u ON b.user_id = u.id
            WHERE b.status = 'pending'
            ORDER BY b.id
        '''
        
        pending_bookings = self.db.execute_query(query)
        
        if not pending_bookings:
            print("No pending bookings.")
            return
        
        print("Pending Bookings:")
        for booking in pending_bookings:
            pet_info = " (with pets)" if booking[5] else ""
            print(f"""
Booking ID: {booking[0]}
Customer: {booking[9]} ({booking[10]})
Car: {booking[8]} {booking[6]} {booking[7]}
Dates: {booking[1]} to {booking[2]}
Total Cost: ${booking[3]:.2f}{pet_info}
""")
            print("-" * 30)
        
        try:
            booking_id = int(input("\nEnter Booking ID to process (0 to return): "))
            
            if booking_id == 0:
                return
            
            action = input("Approve or Reject? (a/r): ").lower()
            
            if action == 'a':
                # Approve booking and mark car as unavailable
                update_booking = "UPDATE bookings SET status = 'approved' WHERE id = ?"
                car_query = "SELECT car_id FROM bookings WHERE id = ?"
                car_result = self.db.execute_query(car_query, (booking_id,))
                
                if car_result:
                    car_id = car_result[0][0]
                    update_car = "UPDATE cars SET available = 0 WHERE id = ?"
                    
                    if self.db.execute_query(update_booking, (booking_id,)) and \
                       self.db.execute_query(update_car, (car_id,)):
                        print("Booking approved successfully!")
                    else:
                        print("Failed to approve booking.")
            
            elif action == 'r':
                update_booking = "UPDATE bookings SET status = 'rejected' WHERE id = ?"
                if self.db.execute_query(update_booking, (booking_id,)):
                    print("Booking rejected.")
                else:
                    print("Failed to reject booking.")
            
            else:
                print("Invalid action.")
        
        except ValueError:
            print("Invalid Booking ID.")
    
    def view_all_users(self):
        """Admin function to view all users"""
        print("\n--- All Users ---")
        
        query = "SELECT username, role, full_name, email, phone FROM users ORDER BY role, username"
        users = self.db.execute_query(query)
        
        for user in users:
            print(f"""
Username: {user[0]}
Role: {user[1].upper()}
Full Name: {user[2] or 'Not provided'}
Email: {user[3] or 'Not provided'}
Phone: {user[4] or 'Not provided'}
""")
            print("-" * 30)
    
    def logout(self):
        """Log out current user"""
        print(f"Goodbye, {self.current_user.full_name or self.current_user.username}!")
        self.current_user = None

# This is the main entry point of our application
if __name__ == "__main__":
    try:
        system = CarRentalSystem()
        system.start()
    except KeyboardInterrupt:
        print("\n\nThank you for using ANY-CRS!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the application.")