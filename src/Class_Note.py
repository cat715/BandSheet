from atexit import register
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
from os import name
import PandaMusic.Sources.CommonDefinition as CommonDefinition


class Note:
    def __init__(self, p_name, p_register = 0):
        if p_name not in CommonDefinition.Standard_Note_Degree:
            raise ValueError("Invalid not name {p_name}, valid note names are listed in Standard_Note_Degree")
        self.name = p_name
        self.scaleLevel = CommonDefinition.Standard_Note_ScaleLevel[p_name] #音级
        self.degree = CommonDefinition.Standard_Note_Degree[p_name] #度数
        self.register = p_register #音区，0为中央C
        self.pitch = register * 8 + self.scaleLevel #绝对音高

    @property
    def degree(self):
        return self.degree

    @property
    def scaleLevel(self):
        return self.scaleLevel

    def __eq__(self, other):
        return isinstance(other, Note) and self.name == other.name and self.register == other.register


class NoteDiff:
    def __init__(self, p_note1, p_note2):
        if isinstance(p_note1, Note) != True or isinstance(p_note2, Note):
            raise ValueError("Invalid class passed. Only support Note")

        # high pitch - low pitch
        if (p_note1.pitch < p_note2.pitch):
            note_temp = p_note1
            p_note1 = p_note2
            p_note2 = note_temp

        # calculate the diff
        self.degreeDiff = p_note1.degree - p_note2.degree
        self.scaleLevelDiff = p_note1.scaleLevel - p_note2.scaleLevel
        self.pitchDiff = p_note1.pitch - p_note2.pitch

    def __print__(self):
        print("DegreeDiff = {self.degreeDiff}, ScaleLevelDiff = {self.scaleLevelDiff},\
               PitchDiff = {self.pitchDiff}")