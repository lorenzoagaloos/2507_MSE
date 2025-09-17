# 2507-YCCIA-MSE800-A
# Assessment 1 - Object Oriented Programming
# Student Name: Lorenzo Agaloos II
# Student Number: 270729354
# Date: 09-September-2025
# Description: This program simulates a simple car rental system using object-oriented programming principles.
# The objective of this assignment is to apply software engineering principles and practices to develop a 
# functional Car Rental System. You will utilize object-oriented programming concepts, design patterns, 
# and appropriate software development methodologies to create a robust and user-friendly system.

# Title: Auckland North Yoobee Car Rental System (ANY CaReS)

import sqlite3
from datetime import datetime, timedelta
import os
os.environ['PYTHONUNBUFFERED'] = '1'
import time
import hashlib
#import numpy as np


# Utility function to clear the terminal screen
def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

# User class to represent users in the system
# This class manages user information and authentication
class User:

    def __init__(self, username, role, full_name=None, email=None):
        self.username = username
        self.role = role
        self.full_name = full_name
        self.email = email
        self.is_logged_in = False

# Parent class for all vehicles in our system
# Demonstrates inheritance - common properties and methods for all vehicles
class Vehicle:
        
    def __init__(self, vehicle_id, make, model, year, mileage): # Initialize basic vehicle properties that all vehicles share
        self.id = vehicle_id
        self.make = make
        self.model = model  
        self.year = year
        self.mileage = mileage
    
    def get_basic_info(self): # Return basic vehicle information - inherited by all child classes
        return f"{self.year} {self.make} {self.model}"
    
    def get_age(self): # Calculate vehicle age - inherited by all child classes
        current_year = datetime.now().year
        return current_year - self.year
    
    def add_mileage(self, miles): # Add mileage to vehicle - inherited method by all child classes
        self.mileage += miles
        return self.mileage

# Car class to represent rental cars
# This class inherits from the Vehicle parent class
class Car(Vehicle):

    def __init__(self, car_id, make, model, year, mileage, available, min_rent, max_rent, daily_rate, pet_friendly):
        # Call parent constructor - initialize inherited properties
        super().__init__(car_id, make, model, year, mileage)
        
        # Add car-specific properties
        self.min_rent_days = min_rent
        self.max_rent_days = max_rent
        self.daily_rate = daily_rate
        self.pet_friendly = pet_friendly
        self.available = available
    
    # Display car information - uses inherited methods from Vehicle parent class
    def display_info(self):
        pet_status = "Pet Friendly Vehicle" if self.pet_friendly else "No Pets Allowed"
        availability = "Available" if self.available else "Rented"
        
        # Using inherited method get_basic_info() from Vehicle parent class
        basic_info = self.get_basic_info()
        
        # Using inherited method get_age() from Vehicle parent class  
        age = self.get_age()
        
        return f"""
Car ID: {self.id}
{basic_info} (Age: {age} years)
Mileage: {self.mileage:,} km
Daily Rate: ${self.daily_rate:.2f}
Rental Period: {self.min_rent_days}-{self.max_rent_days} days
{pet_status}
Status: {availability}
"""

# Additional class to represent child class inheritance from Vehicle parent class
# This is just to demonstrate inheritance - not used in the main system
# Currently for demonstration purposes only - will be planned for future expansion
class Motorcycle(Vehicle):

    def __init__(self, bike_id, make, model, year, mileage, engine_cc, helmet_included=True):
        # Call parent constructor
        super().__init__(bike_id, make, model, year, mileage)
        
        # Add motorcycle-specific properties
        self.engine_cc = engine_cc
        self.helmet_included = helmet_included
    
    def display_info(self):
        # Using inherited methods from Vehicle parent
        basic_info = self.get_basic_info()
        age = self.get_age()
        
        helmet_status = "Helmet Included" if self.helmet_included else "No Helmet Included"
        
        return f"""
Motorcycle ID: {self.id}
{basic_info} (Age: {age} years)
Engine: {self.engine_cc}cc
Mileage: {self.mileage:,} km
{helmet_status}
"""

# Booking class to represent a rental booking
# This class manages the relationship between users, cars, and rental periods
class Booking:
    
    def __init__(self, booking_id, user_id, car_id, start_date, end_date, total_cost, status, pet_included=False):
        self.id = booking_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.status = status
        self.pet_included = pet_included

# Database class to handle database operations
# This class abstracts database interactions
# Will be using SQLite 3 for simplicity and ease of setup
class Database:
   
    def __init__(self):
        self.db_name = 'anycares.db'
        self.init_database()
    
    # Initialize database and create tables if they don't exist
    def init_database(self):

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
                ('Subaru', 'Outback', 2022, 12000, 1, 2, 28, 65.0, 1),
                ('Mazda', 'CX-5', 2021, 27000, 1, 1, 21, 55.0, 0),
                ('Chevrolet', 'Malibu', 2020, 40000, 1, 1, 14, 42.0, 1),
                ('Kia', 'Sorento', 2023, 9000, 1, 3, 30, 70.0, 0),
                ('Hyundai', 'Tucson', 2022, 16000, 0, 2, 28, 60.0, 1),
                ('Volkswagen', 'Jetta', 2021, 25000, 0, 1, 21, 48.0, 0),
            ]
            cursor.executemany('''
                INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate, pet_friendly)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', sample_cars)
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        # Hash password using SHA-256 for simplicity
        # For demonstration purposes only - consider using stronger hashing in production
        return hashlib.sha256(password.encode()).hexdigest()
    
    # Execute a query and return results if applicable
    def execute_query(self, query, params=None):

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

# Main application class to manage the Auckland North Yoobee Car Rental System
# This class integrates users, cars, bookings, and database operations
# Demonstrates composition by including instances of other classes
# Currently serves as a placeholder for future expansion
class anyCares:

    def __init__(self):
        self.db = Database()
        self.current_user = None
        self.running = True
    
    # Main application loop
    def start(self):
        
        # Display welcome message
        #print("\n")
        #print("=" * 60)
        #print("Welcome to the Auckland North Yoobee Car Rental System v1.0")
        #print("ANY-CaReS - Your Trusted Pet-Friendly Car Rental Partner")
        #print("=" * 60)
                
        # Main application loop
        while self.running:
            if self.current_user is None:
                self.show_login_menu()
            else:
                if self.current_user.role == 'admin':
                    self.show_admin_menu()
                else:
                    self.show_customer_menu()
        time.sleep(1)
        clear_screen()

   
    # Display login menu
    def show_login_menu(self):

        print("=" * 60)
        print("Welcome to the Auckland North Yoobee Car Rental System v1.0")
        print("ANY-CaReS - Your Trusted Pet-Friendly Car Rental Partner")
        print("=" * 60)
        print("\n1. Login")
        print("2. Register as Customer") 
        print("3. Exit")
        
        choice = input("\nPlease select an option (1-3): ").strip()
        
        if choice == '1':
            self.login()
        elif choice == '2':
            self.register_customer()
        elif choice == '3':
            
            time.sleep(0.5)
            clear_screen()
            print("\n")
            print("=" * 60)
            print("Thank you for using ANY CaReS. Safe Travels!")
            print("=" * 60)
            print("\n")

            # Clear screen for better UX
            time.sleep(3)
            clear_screen()
            self.running = False
    
        else:
            time.sleep(0.5)
            clear_screen()
            print("\n")
            print("=" * 60)
            print("Invalid selection. Please try again.")
            print("=" * 60)
            time.sleep(1.5)
            clear_screen()

   # User login method 
    def login(self):
        print("=" * 60)
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        hashed_password = self.db.hash_password(password)
        
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        result = self.db.execute_query(query, (username, hashed_password))
        
        if result:
            user_data = result[0]
            self.current_user = User(user_data[1], user_data[3], user_data[4], user_data[5])
            time.sleep(1)
            clear_screen()
            print("=" * 60)
            print(f"\nWelcome back, {self.current_user.full_name or self.current_user.username}!\n")
            
        else:
            print("\nInvalid username or password. Please try again.")
            time.sleep(1)
            clear_screen()
    
    # Logout method
    def logout(self):
        time.sleep(0.5)
        clear_screen()
        print("-" * 60)
        print(f"Have a good day, {self.current_user.full_name or self.current_user.username}!")
        self.current_user = None
        print("-" * 60)

        # Clear screen for better UX
        time.sleep(1.5)
        clear_screen()

    # Admin menu options
    def show_admin_menu(self):

        print("=" * 60)
        print(f"--- ANY CaReS Portal ({self.current_user.username}) ---")
        print("=" * 60)
        print("1. View All Cars")
        print("2. Add New Car")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. Manage Bookings")
        print("6. View All Users")
        print("7. Logoff")
        print("=" * 60)
        
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
            print("\nInvalid choice. Please try again.")
            # Clear screen for better UX
            time.sleep(1)
            clear_screen()

    # Admin - View all cars - method
    def view_all_cars(self):
        time.sleep(0.5)
        clear_screen()
        print("\n--- All Cars in Garage ---")
        
        query = "SELECT * FROM cars ORDER BY id"
        cars = self.db.execute_query(query)
        
        for car_data in cars:
            car = Car(*car_data)  # Car inherits from Vehicle class
            print(car.display_info())  # Uses inherited methods
            print("-" * 60)
    
    # Admin - Add new car - method
    def add_car(self):
        time.sleep(0.5)
        clear_screen()
        print("\n--- Add New Car to Inventory---\n")
        
        try:
            make = input("Car Make: ").strip()
            model = input("Car Model: ").strip()
            year = int(input("Year: "))
            mileage = int(input("Mileage (km): "))
            min_rent = int(input("Minimum rental days: "))
            max_rent = int(input("Maximum rental days: "))
            daily_rate = float(input("Daily rate ($): "))

            available = input("Available to rent? (y/n): ").lower()
            available = 1 if available == 'y' else 0      
            pet_friendly = input("Pet friendly? (y/n): ").lower()
            pet_friendly = 1 if pet_friendly == 'y' else 0
            
            query = '''
                INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate, pet_friendly)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            
            if self.db.execute_query(query, (make, model, year, mileage, available, min_rent, max_rent, daily_rate, pet_friendly)):
                print("\nCar added successfully!\n")
                time.sleep(1)
                clear_screen()
            else:
                print("Failed to add car to inventory.")
                time.sleep(1)
                clear_screen()
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            time.sleep(1)
            clear_screen()
    
    # Admin - Update car details - method
    def update_car(self):
        time.sleep(0.5)
        clear_screen()
        print("\n--- Update Car Details---")
        
        try:
            car_id = int(input("Enter Car ID to update: "))
            
            query = "SELECT * FROM cars WHERE id = ?"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("Car not found.")
                return
            
            car = Car(*car_data[0])  # Car inherits from Vehicle class
            print("Current car details:")
            print(car.display_info())  # Uses inherited methods
            
            print("\nEnter new values (press Enter to keep current value):")
            print("-" * 60)
            
            make = input(f"Make [{car.make}]: ").strip() or car.make
            model = input(f"Model [{car.model}]: ").strip() or car.model
            year_input = input(f"Year [{car.year}]: ").strip()
            year = int(year_input) if year_input else car.year
            
            mileage_input = input(f"Mileage [{car.mileage}]: ").strip()
            mileage = int(mileage_input) if mileage_input else car.mileage

            rate_input = input(f"Daily Rate [{car.daily_rate}]: ").strip()
            daily_rate = float(rate_input) if rate_input else car.daily_rate
     
            pet_input = input(f"Pet Friendly (1=yes, 0=no) [{car.pet_friendly}]: ").strip()
            pet_friendly = int(pet_input) if pet_input else car.pet_friendly

            available_input = input(f"Available (1=yes, 0=no) [{car.available}]: ").strip()
            available = int(available_input) if available_input else car.available


            
            update_query = '''
                UPDATE cars 
                SET make=?, model=?, year=?, mileage=?, available=?, daily_rate=?, pet_friendly=?
                WHERE id=?
            '''
            
            if self.db.execute_query(update_query, (make, model, year, mileage, available, daily_rate, pet_friendly, car_id)):
                time.sleep(1)
                clear_screen()
                print("\nCar details updated successfully!\n")
            else:
                print("\nFailed to update car details.\n")
                time.sleep(1)
                clear_screen()
                
        except ValueError:
            print("\nInvalid input. Try again.\n")
            time.sleep(1)
            clear_screen()
    
    # Admin - Delete car - method
    def delete_car(self):
        time.sleep(0.5)
        clear_screen()
        print("\n--- Delete Car ---")
        
        try:
            car_id = int(input("Enter Car ID to delete: "))
            
            # Check if car has active bookings
            booking_query = "SELECT COUNT(*) FROM bookings WHERE car_id = ? AND status = 'approved'"
            active_bookings = self.db.execute_query(booking_query, (car_id,))[0][0]
            
            if active_bookings > 0:
                print("\nDeleting car with active bookings not allowed.\n")
                time.sleep(1.5)
                clear_screen()
                return
            
            # Show car details before deletion
            query = "SELECT * FROM cars WHERE id = ?"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("\nCar not found.\n")
                time.sleep(1.5)
                clear_screen()
                return
            
            car = Car(*car_data[0])  # Car inherits from Vehicle class
            print("Car to delete:")
            print(car.display_info())  # Uses inherited methods
            
            confirm = input("Are you sure you want to delete this car? (y/n): ").lower()
            
            if confirm == 'y':
                delete_query = "DELETE FROM cars WHERE id = ?"
                if self.db.execute_query(delete_query, (car_id,)):
                    print("\nCar removed from ANY CaRes inventory successfully!\n")
                    time.sleep(1.5)
                    clear_screen()
                else:
                    print("\nFailed to delete car.\n")
                    time.sleep(1.5)
                    clear_screen()
        
        except ValueError:
            print("Invalid Car ID.")
            time.sleep(1.5)
            clear_screen()
    
    # Admin - Manage bookings - method
    def manage_bookings(self):
        time.sleep(0.5)
        clear_screen()
        print("\n--- Manage Car Rental Bookings ---\n")
        
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
            print("No pending bookings.\n")
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
            print("-" * 60)
        
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
                        print("\nBooking approved successfully!\n")
                    else:
                        print("\nFailed to approve booking.\n")
                        time.sleep(1.5)
                        clear_screen()
            
            elif action == 'r':
                update_booking = "UPDATE bookings SET status = 'rejected' WHERE id = ?"
                if self.db.execute_query(update_booking, (booking_id,)):
                    print("\nBooking rejected. Car remains available.\n")
                    time.sleep(1.5)
                    clear_screen()
                else:
                    print("\nFailed to reject booking.\n")
                    time.sleep(1.5)
                    clear_screen()
            
            else:
                print("\nInvalid action.\n")
                time.sleep(1.5)
                clear_screen()
        
        except ValueError:
            print("\nInvalid Booking ID.\n")
            time.sleep(1.5)
            clear_screen()
    
    # Admin - View all users - method
    def view_all_users(self):
        time.sleep(0.5)
        clear_screen()
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
            print("-" * 60)


    # Customer registration method
    def register_customer(self):

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
            print("\nRegistration successful! You can now login.")
        else:
            print("Registration failed. Please try again.")
    
    # Customer menu options
    def show_customer_menu(self):
        print("=" * 60)
        print(f"--- Customer Portal ({self.current_user.username}) ---")
        print("=" * 60)
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

    # Customer - View available cars - method
    # This method includes filtering for pet-friendly cars
    def view_available_cars(self):

        print("-" * 60)
        print("--- Available Cars ---")
        print("-" * 60)
        
        # Ask if they want pet-friendly cars
        pet_filter = input("\nDo you need a pet-friendly car? (y/n): ").lower()
        
        if pet_filter == 'y':
            query = "SELECT * FROM cars WHERE available = 1 AND pet_friendly = 1"
            time.sleep(0.5)
            clear_screen()
            print("\nShowing pet-friendly cars only:")
            print("-" * 60)
        else:
            query = "SELECT * FROM cars WHERE available = 1 AND pet_friendly = 0"
            time.sleep(0.5)
            clear_screen()
            print("\nShowing all available non pet-friendly cars:")
            print("-" * 60)
        
        cars = self.db.execute_query(query)
        
        if not cars:
            print("Sorry, no cars match your criteria.")
            return
        
        for car_data in cars:
            car = Car(*car_data)
            print(car.display_info())
            print("-" * 30)
    
    # Customer - Book a car - method
    # This method includes handling for pet fees if applicable
    def book_car(self):
        time.sleep(0.5)
        clear_screen()
        print("-" * 60)
        print("--- Book a Car ---")
        print("-" * 60)
        
        # Show available cars first
        self.view_available_cars()
        
        try:
            car_id = int(input("\nEnter Car ID to book: "))
            
            # Check if car exists and is available
            query = "SELECT * FROM cars WHERE id = ? AND available = 1"
            car_data = self.db.execute_query(query, (car_id,))
            
            if not car_data:
                print("Car not found or not available.")
                print("Please select a valid Car ID from the available cars list.")
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
                print(f"Base cost for {days} days: ${days * car.daily_rate:.2f}")

            print(f"\nBooking Summary:")

            # Using inherited method from Vehicle parent class
            print(f"Car: {car.get_basic_info()}")
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
                    print("\nBooking request submitted successfully!")
                    print("Your booking is pending admin approval.\n")
                else:
                    print("Booking failed. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid car ID.")
    
    # Customer - View my bookings - method
    # This method shows all bookings for the logged-in customer
    def view_my_bookings(self):
        time.sleep(0.5)
        clear_screen()
        print("\n" + "-" * 60)
        print("--- Transactions ---")
        print("-" * 60)
        
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
            print("=" * 60)


if __name__ == "__main__":

    try:
        time.sleep(0.5)
        clear_screen()
        system = anyCares()
        system.start()
    except KeyboardInterrupt:
        print("\nThank you for using ANY CaReS. Goodbye!")
    except Exception as e:
        print("\n")
        print("=" * 100)
        print(f"The option you selected is still under development: {e}")
        print("Please restart the application and try again.")
        print("=" * 100)
        print("\n")

