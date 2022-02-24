from multiprocessing.sharedctypes import Value
import CommonDefinition
import NoteUtils

class Chord:
    # Define and generate a chord based on one note: Chord Type + Note + Note Location
    def __init__(self, p_chordType, p_note, p_noteLocation):
        if isinstance(p_note, NoteUtils.Note) != True:
            raise ValueError("Invalid class passed. Only support Note")
        if p_chordType not in CommonDefinition.Standard_Chord_Type:
            raise ValueError("Invalid chord type")

        self.chordType = p_chordType
        self.notes = {}
        self.notes[p_noteLocation] = p_note
        self.__generateBasedOnRule__()

    def __generateBasedOnRule__(self):
        self.__printChord__()

    def __printChord__(self):
        print(f"ChordType: {self.chordType}")
        content = ""
        for position, note in self.notes.items():
            content = content + str(note.name) + "(" + str(position) + "),"
        print(content)

