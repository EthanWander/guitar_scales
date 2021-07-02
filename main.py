NOTES = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
STANDARD_TUNING = ["E", "A", "D", "G", "B", "E"]
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
MINOR_SCALE = [0, 2, 3, 5, 7, 8, 10]


class Scale:
    def __init__(self, scale, root, tuning):
        self.scale = scale
        self.tuning = tuning
        self.root = root

    def get_notes_in_scale(self):
        pass
    
    def print(self):
        pass


def main():
    minor_scale = Scale(MINOR_SCALE, "E", STANDARD_TUNING)
    minor_scale.print()


if __name__ == "__main__":
    main()
