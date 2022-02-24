from atexit import register
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
from os import name
import CommonDefinition as CommonDefinition


class Note:
    def __init__(self, p_name, p_register = 0):
        if p_name not in CommonDefinition.Standard_Note_Degree:
            raise ValueError(f"Invalid not name {p_name}, valid note names are listed in Standard_Note_Degree")
        self.name = p_name
        self.scaleLevel = CommonDefinition.Standard_Note_ScaleLevel[p_name] #音级
        self.degree = CommonDefinition.Standard_Note_Degree[p_name] #度数
        self.register = p_register #音区，0为中央C
        self.pitch = p_register * 8 + self.scaleLevel #绝对音高

    def __eq__(self, other):
        return isinstance(other, Note) and self.name == other.name and self.register == other.register


class NoteDiff:
    def __init__(self, p_note1, p_note2):
        if (isinstance(p_note1, Note) != True) or (isinstance(p_note2, Note) != True):
            raise ValueError("Invalid class passed. Only support Note")

        # high pitch - low pitch, note1 low, note2 high
        if (p_note1.pitch > p_note2.pitch):
            note_temp = p_note1
            p_note1 = p_note2
            p_note2 = note_temp

        # calculate the diff
        self.note1 = p_note1
        self.note2 = p_note2
        self.degreeDiff = p_note2.degree - p_note1.degree
        self.scaleLevelDiff = p_note2.scaleLevel - p_note1.scaleLevel
        self.pitchDiff = p_note2.pitch - p_note1.pitch

    def __print__(self):
        print(f"Note1 = {self.note1.name}, Note2 = {self.note2.name},\
                ScaleLevelDiff = {self.scaleLevelDiff}, DegreeDiff = {self.degreeDiff}, PitchDiff = {self.pitchDiff}")