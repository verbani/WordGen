import random
import PySimpleGUI as sg


def SyllableGen():
    vowel = ('a', 'ae', 'ao', 'ai', 'au', 'ay',
             'e', 'ea', 'ee', 'ei', 'eo', 'eu', 'ey',
             'i', 'ia', 'ie', 'io', 'iu', 'iy', 'ieu',
             'o', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy',
             'u', 'ua', 'ue', 'ui', 'uo', 'uu', 'uy',
             'y', 'ya', 'ye', 'yo', 'yu'
           )
    presonant=('B',
               'C', 'Cz', 'Ch', 'Cr', 'Chr', 'Cl',
               'D', 'Dr',
               'F', 'Fr', 'Fl',
               'G', 'Gh', 'Gr',
               'H', 'Hr',
               'J', 'Jh',
               'K', 'Kr', 'Kh',
               'L',
               'M', 'Mh',
               'N', 'Nh', 'Ng',
               'P', 'Pr', 'Ps', 'Ph', 'Pf',
               'Q', 'Qr', 'Qh',
               'R', 'Rh',
               'S', 'Sh', 'Sr', 'Shr',
               'T', 'Th', 'Thr', 'Tr',
               'V', 'Vr', 'Vh',
               'W', 'Wh', 'Wr', 'Whr',
               'X',
               'Z', 'Zh',
               ""
               )
    postsonant=(
                'b',
                'c', 'ch', 'ck', 'chk', 'cc',
                'd', 'dr',
                'f', 'ft',
                'g', 'gh',
                'j',
                'k', 'kt',
                'l', 'ld', 'lf', 'lt',
                'm',
                'n', 'nh', 'ng', 'nt', 'nd',
                'p', 'pt',
                'q',
                'r', 'rn', 'rm', 'rd', 'rc', 'rk', 'rv', 'rp', 'rt', 'rb', 'rp', 'rg', 'rl',
                's', 'sh', 'st', 'sk', 'ss',
                't', 'th', 'tr', 'tl',
                'v', 'vl',
                'w', 'wk', 'wl',
                'x',
                'z',
                ''
    )
    postvowel=(
        'a',
        'e',
        'i', 'ia', 'ie',
        'o', 'ou',
        'u', 'uo',
        'y', 'ya', 'ye',
        ''
    )
    resonant=(
        'b',
        'c', 'ck', 'ct', 'cc', 'chk',
        'd', 'dr',
        'f', 'ff',
        'g', 'gh',
        'j',
        'k', 'kt',
        'l',
        'm',
        'n', 'nh', 'ng', 'nt', 'nd',
        'p', 'pt',
        'q',
        'r', 'rd', 'rt', 'rg', 'rk', 'rl',
        's', 'st', 'sh', 'sk', 'shk',
        't', 'th', 'tr', 'tl',
        'v',
        'w', 'wk', 'wl',
        'x',
        'z', 'zz',
        ''
    )
    x = len(presonant)
    y = len(vowel)
    z = len(postsonant)
    q = len(postvowel)
    r = len(resonant)
    x1 = random.randint(0, x-1)
    y1 = random.randint(0, y-1)
    z1 = random.randint(0, z-1)
    # No postsonant means no postvowel
    if z1 == z-1:
        q1 = q-1
    else:
        q1 = random.randint(0, q - 1)
    # No postvowel means no resonant
    if q1 == q-1:
        r1 = r-1
    else:
        r1 = random.randint(0, r-1)
    # Final resonant check
    if r1 == r-1:
        q2 = q-1
    else: q2 = random.randint(0, q-1)
    # Simple upper for vowel first
    if x1 == x - 1:
        v1 = vowel[y1].upper()
    else:
        v1 = vowel[y1]
    return presonant[x1] + v1 + postsonant[z1] + postvowel[q1] + resonant[r1] + postvowel[q2]


def SyllableGen2():
    # Throwaway test func
    vowel=('a', 'aa', 'ae', 'ao', 'ai', 'au', 'ay',
           'e', 'ea', 'ee', 'ei', 'eo', 'eu', 'ey',
           'i', 'ia', 'ie', 'ii', 'io', 'iu', 'iy',
           'o', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy',
           'u', 'ua', 'ue', 'ui', 'uo', 'uu', 'uy',
           'y', 'ya', 'ye', 'yo', 'yu'
           )
    presonant=('b',
               'c', 'cz', 'ch',
               'd', 'dr',
               'f', 'fr',
               'g', 'gh',
               'h',
               'j',
               'k',
               'l',
               'm',
               'n', 'nh', 'ng',
               'p',
               'q', 'qh',
               'r',
               's', 'sh',
               't', 'th',
               'v',
               'w', 'wh',
               'x',
               'yh',
               'z', 'zh',
               "'"
               )

    x = len(presonant)
    y = len(vowel)
    x1 = random.randint(0, x-1)
    x2 = random.randint(0, x-1)
    x3 = random.randint(0, x-1)
    x4 = random.randint(0, x-1)
    y1 = random.randint(0, y-1)
    y2 = random.randint(0, y-1)
    y3 = random.randint(0, y-1)

    return presonant[x1].upper() + vowel[y1] + presonant[x2] + vowel[y2] + presonant[x3] + vowel[y3] + presonant[x4]


layout = [[sg.Text('Click to Gen', size=(25, 3), key='result')], [sg.Button("Gen")], [sg.Button("GenF")]]

window = sg.Window('WordGen', layout, size=(400, 100))

while True:
    event, values = window.read()
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break
    elif event == "Gen":
        window['result'].Update(SyllableGen() + " " + SyllableGen() + " " + SyllableGen() + " " + SyllableGen())
    elif event == "Gen2":
        window['result'].Update(SyllableGen() + " " + SyllableGen())

window.close()