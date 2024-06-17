import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root, grid_size):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.grid_size = grid_size
        self.player = "X"
        self.board = [" " for _ in range(grid_size**2)]
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        for i in range(self.grid_size**2):
            button = tk.Button(self.root, text=" ", font="Arial 20", width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // self.grid_size, column=i % self.grid_size)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.player
            self.update_button(index)

            if self.check_winner(self.player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.player = "O" if self.player == "X" else "X"

    def update_button(self, index):
        if self.player == "X":
            self.buttons[index].config(text=self.player, fg="blue")
        else:
            self.buttons[index].config(text=self.player, fg="red")

    def check_winner(self, player):
        win_conditions = []
        
        # Rows
        for i in range(self.grid_size):
            win_conditions.append([i * self.grid_size + j for j in range(self.grid_size)])
        
        # Columns
        for j in range(self.grid_size):
            win_conditions.append([i * self.grid_size + j for i in range(self.grid_size)])
        
        # Diagonals
        win_conditions.append([i * (self.grid_size + 1) for i in range(self.grid_size)])  # Main diagonal
        win_conditions.append([i * (self.grid_size - 1) + (self.grid_size - 1) for i in range(self.grid_size)])  # Anti-diagonal

        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def check_draw(self):
        return all(cell != " " for cell in self.board)

    def reset_game(self):
        self.board = [" " for _ in range(self.grid_size**2)]
        for button in self.buttons:
            button.config(text=" ")
        self.player = "X"

def get_grid_size():
    try:
        size = int(entry.get())
        if size < 3 or size > 5:
            raise ValueError("Grid size should be between 3 and 5")
        return size
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def start_game():
    size = get_grid_size()
    if size:
        root.withdraw()  # Hide the grid size input window
        game_root = tk.Tk()
        game = TicTacToe(game_root, size)
        game_root.mainloop()
        root.deiconify()  # Show the grid size input window again when the game ends

if __name__ == "__main__":
    root = tk.Tk()
    
    label = tk.Label(root, text="Enter grid size (3-5):")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    submit_button = tk.Button(root, text="Start Game", command=start_game)
    submit_button.pack()

    root.mainloop()
