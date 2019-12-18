from enum import Enum

class InputModes(Enum):
    SKYKEYBOARD = [1, 'Sky keyboard', 'Type on keyboard as you would in Sky']
    SKY = [2, 'Sky ABC1-5', 'Sky column/row notation:\n   A1 A2 A3 A4 A5\n   B1 B2 B3 B4 B5\n   C1 C2 C3 C4 C5']
    WESTERN = [3, 'Western CDEFGAB2-7', 'Western (note name + octave, e.g. C4 D4 E4 ...)']
    DOREMI = [4, 'Dorémi do re mi fa sol', 'Dorémi (note name + octave, e.g. do4 re4 mi4 ...)']
    JIANPU = [5, 'Jianpu 1234567+-', 'Jianpu (note names as 1 2 3 4 5 6 7, followed by + or - for octaves)']
    WESTERNCHORDS = [6, 'Chords CDEFGAB', 'Abbrev. chord name (C, F, Dm, Bdim, A+, Csus2, Dsus4, C6, Cmaj7, Dm11)']

class RenderModes(Enum):
    HTML = 1
    SVG = 2
    PNG = 3
    SKYASCII = 4
    WESTERNASCII = 5
    JIANPUASCII = 6

class CSSModes(Enum):
    XML = 1
    HREF = XML
    LINK = XML
    IMPORT = 2
    EMBED = 3
    HARD = EMBED
