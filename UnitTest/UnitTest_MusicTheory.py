import sys
import pathlib
import NoteUtils as NoteUtils
import ChordUtils as ChordUtils

def VerifyNoteDiff():
    # =========== Case 1 ============
    note1 = NoteUtils.Note('C', 0)
    note2 = NoteUtils.Note('D', 0)
    noteDiff = NoteUtils.NoteDiff(note1, note2)
    noteDiff.__print__()

    # =========== Case 2 ============
    note1 = NoteUtils.Note('C#', 0)
    note2 = NoteUtils.Note('D', 0)
    noteDiff = NoteUtils.NoteDiff(note1, note2)
    noteDiff.__print__()

def TestGenerateChordWithOneNote():
    note1 = NoteUtils.Note('C', 0)
    chord = ChordUtils.Chord('Major', note1, 3)

if __name__ == "__main__":
    #print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
    #print (str(pathlib.Path(sys.path[0]).parent))
    #print("In module products __package__, __name__ ==", __package__, __name__)
    #sys.path.append("D:\\Code\\Music\\PandaMusic\\")
    
    #VerifyNoteDiff()
    TestGenerateChordWithOneNote()