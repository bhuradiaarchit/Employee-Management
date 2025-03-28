import mysql.connector
import tkinter as tk
from tkinter import messagebox
from config import DB_CONFIG  
conn = mysql.connector.connect(**DB_CONFIG)
print("Starting Employee Management System")
cursor = conn.cursor()
def add_employee():
    name = entry_name.get()
    position = entry_position.get()
    salary = entry_salary.get()
    if name and position and salary.isdigit():
        cursor.execute("INSERT INTO Employee (name, position, salary) VALUES (%s, %s, %s)", 
                       (name, position, int(salary)))
        conn.commit()
        messagebox.showinfo("Success", "Employee Added Successfully!")
    else:
        messagebox.showerror("Error", "Invalid Input! Fill all fields correctly.")
def remove_employee():
    emp_id = entry_id.get()
    if emp_id.isdigit():
        cursor.execute("DELETE FROM Employee WHERE id=%s", (emp_id,))
        conn.commit()
        messagebox.showinfo("Success", "Employee Removed Successfully!")
    else:
        messagebox.showerror("Error", "Invalid Employee ID!")
def promote_employee():
    emp_id = entry_id.get()
    new_salary = entry_salary.get()
    if emp_id.isdigit() and new_salary.isdigit():
        cursor.execute("UPDATE Employee SET salary=%s WHERE id=%s", (new_salary, emp_id))
        conn.commit()
        messagebox.showinfo("Success", "Salary Updated!")
    else:
        messagebox.showerror("Error", "Invalid Input!")
def display_employees():
    cursor.execute("SELECT * FROM Employee")
    rows = cursor.fetchall()
    display_text.delete("1.0", tk.END)  
    for row in rows:
        display_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}\n")
root = tk.Tk()
root.title("Employee Management System")
tk.Label(root, text="Employee Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)
tk.Label(root, text="Position:").grid(row=1, column=0)
entry_position = tk.Entry(root)
entry_position.grid(row=1, column=1)
tk.Label(root, text="Salary:").grid(row=2, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=2, column=1)
tk.Label(root, text="Employee ID:").grid(row=3, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=3, column=1)
tk.Button(root, text="Add Employee", command=add_employee).grid(row=4, column=0)
tk.Button(root, text="Remove Employee", command=remove_employee).grid(row=4, column=1)
tk.Button(root, text="Promote Employee", command=promote_employee).grid(row=5, column=0)
tk.Button(root, text="Display Employees", command=display_employees).grid(row=5, column=1)
display_text = tk.Text(root, height=10, width=50)
display_text.grid(row=6, column=0, columnspan=2)
root.mainloop()
conn.close()
