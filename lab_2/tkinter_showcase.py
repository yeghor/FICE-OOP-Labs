import tkinter as tk


root = tk.Tk()
root.geometry("300x500")

canvas_editor = tk.Canvas(root, height=600, width=900)

def paint( event ):
   
    # Co-ordinates.
    x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 ) 
    
    # Colour
    Colour = "#000fff000" 
    
    # specify type of display
    canvas_editor.create_line( x1, y1, x2, 
                  y2, fill = Colour )


canvas_editor.bind( "<B1-Motion>", paint )
canvas_editor.pack(expand=True)

root.mainloop()