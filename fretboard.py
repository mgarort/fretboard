import svgwrite
import numpy as np

def denumpify(array):
    """
    Denumpify single-row array of integers.
    """
    return [int(elem) for elem in list(array)]

class Fretboard():
    """
    Basic class to draw a fretboard and mark specific positions in it.
    """

    def __init__(self,filepath='fretboard.svg',start_fret=0,end_fret=19):

        self.filepath=filepath

        # A classical guitar typically has 19 frets: 12 in the mast and 7 in
        # the body.
        self.start_fret = start_fret
        self.end_fret = end_fret

        # List of tuples ((string,fret), color)
        self.markings = []

    def mark(self,marking):
        """
        Mark one or more frets with circles. Can indicate positions and colors.
        """
        self.markings.append(marking)

    def draw(self):
        """
        Draw the fretboard and the marked positions.
        """
        # Drawing constants
        string_sep = 1
        string_width = [2,3,4,5,6,7]
        fret_sep = 2
        margin_above = 2
        margin_below = 2
        margin_left = 2
        margin_right = 2
        scaling_factor = 50
        label_padding = 0.3
        label_alignment = - np.array((0.6,0.45))
        label_fontsize=55
        radius=0.375
        # Define useful variables
        fretboard_topright = np.array((margin_left,margin_above))
        string_length = (self.end_fret - self.start_fret) * 2
        canvas_size = denumpify(np.array((string_length + margin_left + margin_right,
                                          string_sep*6 + margin_above + margin_below))*scaling_factor)
        num_frets = self.end_fret - self.start_fret
        # Draw strings from and until fret, in different widths
        dwg = svgwrite.Drawing(self.filepath,profile='tiny',size=canvas_size)
        dwg.add( dwg.rect( insert=(0,0), size=canvas_size, fill='white' ) )
        # Draw strings
        for i in range(6):
            line_start = denumpify(
                    (fretboard_topright+np.array((0,string_sep*i)))*scaling_factor
                    )
            line_end = denumpify(
                    (fretboard_topright+np.array((string_length,string_sep*i)))*scaling_factor
                    )
            dwg.add( dwg.line( start=line_start, end=line_end, stroke='black', stroke_width=string_width[i] ) )
        # Draw frets
        for i in range(num_frets + 1):
            fret_start = denumpify(
                    (fretboard_topright+np.array((fret_sep*i, 0)))*scaling_factor
                    )
            fret_end = denumpify(
                    (fretboard_topright+np.array((fret_sep*i, string_sep*5)))*scaling_factor
                    )
            dwg.add( dwg.line( start=fret_start, end=fret_end, stroke='black', stroke_width=5 ) )
        # Label fret numbers
        start_label_position = denumpify(
                (fretboard_topright + label_alignment)*scaling_factor
                )
        dwg.add( dwg.text( str(self.start_fret), insert=start_label_position, stroke='black' , font_size=label_fontsize) )
        end_label_position = denumpify(
                (fretboard_topright + label_alignment + np.array((num_frets*fret_sep,0)))*scaling_factor
                )
        dwg.add( dwg.text( str(self.end_fret), insert=end_label_position, stroke='black' , font_size=label_fontsize) )
        # Add markings
        for marking in self.markings:
            string = marking[0][0]
            fret = marking[0][1]
            color = marking[1]
            center = denumpify(
                    (fretboard_topright + np.array((fret*fret_sep - fret_sep/2, string-1)))*scaling_factor
                        )
            radius=radius*scaling_factor
            dwg.add( dwg.circle( center=center, r=radius, stroke=color) )
        dwg.save()
