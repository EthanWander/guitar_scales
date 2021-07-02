NOTES = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
STANDARD_TUNING = ["E", "A", "D", "G", "B", "E"]
NECK_DOTS = [2, 4, 6, 9]
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]
ARABIC_SCALE = [0, 1, 5, 6, 9, 10]


class Scale:
    def __init__(self, scale, root, tuning):
        self.scale = scale
        self.tuning = tuning
        self.root = root
        self.notes_in_scales = self.get_notes_in_scale()

    def get_notes_in_scale(self):
        root_index = NOTES.index(self.root)
        notes_in_scale = []
        for i in self.scale:
            notes_in_scale.append((root_index + i)%12)
        notes_in_scale.sort()
        return notes_in_scale
    
    def print_row(self, string_note):
        string_note_index = NOTES.index(string_note)
        print_out = string_note + "| "
        for i in range(13):
            if self.notes_in_scales.count((i + string_note_index) % 12):
                print_out = print_out + "x "
            else:
                print_out = print_out + "- "
        print(print_out)
    
    def print_neck_dots(self):
        print_out = "   : "
        for i in range(11):
            if NECK_DOTS.count(i):
                print_out = print_out + ". "
            else:
                print_out = print_out + "  "
        print_out = print_out + ":"
        print(print_out)

    def print(self):
        reversed_tuning = self.tuning
        reversed_tuning.reverse()
        self.print_neck_dots()
        for string_note in reversed_tuning:
            self.print_row(string_note)


def main():
    minor_scale = Scale(ARABIC_SCALE, "B", STANDARD_TUNING)
    minor_scale.print()


if __name__ == "__main__":
    main()
