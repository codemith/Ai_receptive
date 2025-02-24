import tkinter as tk
from tkinter import ttk, messagebox

# --- Calculator  ---
def open_calculator():
    calc_win = tk.Toplevel(root)
    calc_win.title("Basic Calculator")
    
    tk.Label(calc_win, text="Number 1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry1 = tk.Entry(calc_win)
    entry1.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(calc_win, text="Operator:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    operator_var = tk.StringVar(value='+')
    op_menu = ttk.Combobox(calc_win, textvariable=operator_var, values=['+', '-', '*', '/'], state='readonly', width=5)
    op_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    
    tk.Label(calc_win, text="Number 2:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry2 = tk.Entry(calc_win)
    entry2.grid(row=2, column=1, padx=5, pady=5)
    
    result_label = tk.Label(calc_win, text="Result: ")
    result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            op = operator_var.get()
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    result_label.config(text="Error: Division by zero")
                    return
                result = num1 / num2
            result_label.config(text=f"Result: {result}")
        except ValueError:
            result_label.config(text="Invalid input.")
    
    tk.Button(calc_win, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# --- To-Do List  ---
def open_todo():
    todo_win = tk.Toplevel(root)
    todo_win.title("To-Do List")
    
    tasks = []
    
    def update_listbox():
        listbox.delete(0, tk.END)
        for task in tasks:
            listbox.insert(tk.END, task)
    
    tk.Label(todo_win, text="Enter Task:").pack(padx=5, pady=5)
    task_entry = tk.Entry(todo_win, width=40)
    task_entry.pack(padx=5, pady=5)
    
    def add_task():
        task = task_entry.get()
        if task:
            tasks.append(task)
            update_listbox()
            task_entry.delete(0, tk.END)
    
    tk.Button(todo_win, text="Add Task", command=add_task).pack(padx=5, pady=5)
    
    listbox = tk.Listbox(todo_win, width=50)
    listbox.pack(padx=5, pady=5)
    
    def remove_task():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            tasks.pop(index)
            update_listbox()
    
    tk.Button(todo_win, text="Remove Selected Task", command=remove_task).pack(padx=5, pady=5)

# --- Tic Tac Toe  ---
def open_tictactoe():
    game_win = tk.Toplevel(root)
    game_win.title("Tic Tac Toe")
    
    current_player = ['X']  # Use list for mutable reference
    board = [['' for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    moves = [0]
    
    def check_winner():
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return board[i][0]
        # Check columns
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != '':
                return board[0][j]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]
        return None
    
    def button_click(row, col):
        if board[row][col] == '':
            board[row][col] = current_player[0]
            buttons[row][col].config(text=current_player[0], state="disabled")
            moves[0] += 1
            winner = check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                game_win.destroy()
                return
            elif moves[0] == 9:
                messagebox.showinfo("Game Over", "It's a draw!")
                game_win.destroy()
                return
            # Switch player
            current_player[0] = 'O' if current_player[0] == 'X' else 'X'
    
    for i in range(3):
        for j in range(3):
            btn = tk.Button(game_win, text='', font=('Helvetica', 20), width=5, height=2,
                            command=lambda row=i, col=j: button_click(row, col))
            btn.grid(row=i, column=j, padx=5, pady=5)
            buttons[i][j] = btn

# --- Main Menu GUI ---
root = tk.Tk()
root.title("AI Tools Project GUI")

tk.Label(root, text="Select an Application", font=('Helvetica', 16)).pack(padx=10, pady=10)
tk.Button(root, text="Basic Calculator", width=20, command=open_calculator).pack(padx=5, pady=5)
tk.Button(root, text="To-Do List", width=20, command=open_todo).pack(padx=5, pady=5)
tk.Button(root, text="Tic Tac Toe", width=20, command=open_tictactoe).pack(padx=5, pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(padx=5, pady=5)

root.mainloop()
