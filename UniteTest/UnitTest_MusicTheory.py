from ..src.Class_Note import Note

def VerifyNoteDiff():
    note1 = Note('C', 0)
    note2 = Note('D', 0)

    noteDiff = NoteDiff(note1, note2)
    noteDiff.__print__()

if __name__ == "__main__":
    VerifyNoteDiff()