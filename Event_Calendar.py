# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()
win.title('Event Calendar')

# Set the size of the tkinter window
win.geometry("700x350")

# Create an instance of Style widget
style = ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Event")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Date")

# Insert the data in Treeview widget
tree.insert('', 'end', text="1", values=('Prarambh', '12th Jan 23'))
tree.insert('', 'end', text="2", values=('Illusion', '13th Jan 23'))
tree.insert('', 'end', text="3", values=('First defaulter’s List', '9th Feb 23'))
tree.insert('', 'end', text="4", values=('Internal Assessment Test 1 ', '15th - 17th Feb 23'))
tree.insert('', 'end', text="5", values=('Marathi Rajya Bhasha Diwas ', '27th Feb 23'))
tree.insert('', 'end', text="6", values=('Internal Assessment Test 2 ', '23-27th March 23'))
tree.insert('', 'end', text="7", values=('Utsav and Annual Day ', '27th -30th March 23'))
tree.insert('', 'end', text="8", values=('Internal Assessment Test 3 ', '17-20th April 23'))
tree.insert('', 'end', text="9", values=('Submissions and mock vivas ', '14th-21st April 22'))
tree.insert('', 'end', text="10", values=('Internship Mela ', '5th - 6th April 23'))
tree.insert('', 'end', text="11", values=('Oral/Practical Examination ', '24th April-4th May 23'))
tree.insert('', 'end', text="12", values=('Theory Examination ', '10th May - 23rd May 23'))
tree.insert('', 'end', text="13", values=('Commencement of New Term ', '10th July 23'))

tree.pack()

# def edit():
#    # Get selected item to Edit
#    selected_item = tree.selection()[0]
#    tree.item(selected_item, text="blub", values=("foo", "bar"))

# def delete():
#    # Get selected item to Delete
#    selected_item = tree.selection()[0]
#    tree.delete(selected_item)

# # Add Buttons to Edit and Delete the Treeview items
# edit_btn = ttk.Button(win, text="Edit", command=edit)
# edit_btn.pack()
# del_btn = ttk.Button(win, text="Delete", command=delete)
# del_btn.pack()

win.mainloop()