import tkinter as tk
from tkinter import messagebox
from .binary_search_tree import BinarySearchTree

class TreeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Árbol Binario de Búsqueda")

        self.tree = BinarySearchTree()
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        self.label = tk.Label(self.master, text="Valor a insertar:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.insert_button = tk.Button(self.master, text="Insertar", command=self.insert_value)
        self.insert_button.pack()

        self.preorder_button = tk.Button(self.master, text="Preorden", command=self.preorder_traversal)
        self.preorder_button.pack()

        self.inorder_button = tk.Button(self.master, text="Inorden", command=self.inorder_traversal)
        self.inorder_button.pack()

        self.postorder_button = tk.Button(self.master, text="Postorden", command=self.postorder_traversal)
        self.postorder_button.pack()

    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.tree.root = self.tree.insert(self.tree.root, value)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor entero válido.")

    def draw_tree(self):
        self.canvas.delete("all")
        self.draw_node(self.tree.root, 400, 50, 200)

    def draw_node(self, node, x, y, h_spacing=100):
        if node:
            self.canvas.create_oval(x-20, y-20, x+20, y+20, outline="black")
            self.canvas.create_text(x, y, text=str(node.val))

            if node.left:
                self.canvas.create_line(x-20, y+20, x-h_spacing, y+100, arrow=tk.LAST)
                self.draw_node(node.left, x-h_spacing, y+100, h_spacing/2)

            if node.right:
                self.canvas.create_line(x+20, y+20, x+h_spacing, y+100, arrow=tk.LAST)
                self.draw_node(node.right, x+h_spacing, y+100, h_spacing/2)

    def preorder_traversal(self):
        result = []
        self.tree.preorder(self.tree.root, result)
        messagebox.showinfo("Preorden", " ".join(map(str, result)))

    def inorder_traversal(self):
        result = []
        self.tree.inorder(self.tree.root, result)
        messagebox.showinfo("Inorden", " ".join(map(str, result)))

    def postorder_traversal(self):
        result = []
        self.tree.postorder(self.tree.root, result)
        messagebox.showinfo("Postorden", " ".join(map(str, result)))

def main():
    root = tk.Tk()
    app = TreeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
