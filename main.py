NOTES = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
STANDARD_TUNING = ["E", "A", "D", "G", "B", "E"]
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]


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

    def print(self):
        reversed_tuning = self.tuning
        reversed_tuning.reverse()
        for string_note in reversed_tuning:
            self.print_row(string_note)


def main():
    minor_scale = Scale(MINOR_SCALE, "E", STANDARD_TUNING)
    minor_scale.print()


if __name__ == "__main__":
    main()
