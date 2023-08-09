"""
File: babygraphics.py
Name: Weili Chen
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    average_distance = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE+year_index*average_distance
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i in range(len(lookup_names)):
        # line color for each name
        color = COLORS[i % len(COLORS)]
        name = lookup_names[i]
        for j in range(len(YEARS)-1):
            year1 = str(YEARS[j])
            spot1_x = get_x_coordinate(CANVAS_WIDTH, j)
            # if the lookup name is in the name_data and the rank is lower the max rank
            if year1 in name_data[name]:
                rank1 = int(name_data[name][year1])
                if rank1 < MAX_RANK:
                    spot1_y = rank1*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK + GRAPH_MARGIN_SIZE
                    canvas.create_text(spot1_x+TEXT_DX, spot1_y, text=f'{name} {rank1}', anchor=tkinter.SW, fill=color)
            # if the lookup name is not in the name_data or the rank is higher the max rank
            else:
                spot1_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_text(spot1_x+TEXT_DX, spot1_y, text=f'{name} *', anchor=tkinter.SW, fill=color)
            year2 = str(YEARS[j+1])
            spot2_x = get_x_coordinate(CANVAS_WIDTH, j + 1)
            if year2 in name_data[name]:
                rank2 = int(name_data[name][year2])
                if rank2 < MAX_RANK:
                    spot2_y = rank2*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK + GRAPH_MARGIN_SIZE
            else:
                spot2_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            # draw a line from spot1 to spot2
            canvas.create_line(spot1_x, spot1_y, spot2_x, spot2_y, width=LINE_WIDTH, fill=color)
        # the rank spot in the last year
        final_year = str(YEARS[-1])
        final_x = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)
        if final_year in name_data[name]:
            final_rank = int(name_data[name][final_year])
            if final_rank < MAX_RANK:
                final_y = final_rank*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK + GRAPH_MARGIN_SIZE
                canvas.create_text(final_x+TEXT_DX, final_y, text=f'{name} {final_rank}', anchor=tkinter.SW, fill=color)
        else:
            final_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_text(final_x + TEXT_DX, final_y, text=f'{name} *', anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
