# =============================================================================
# Meritve teže
#
# V zdravstvenem domu so se odločili izvesti raziskavo o telesni teži.
# Nekaj prostovoljcev se je v okviru te raziskave hodilo občasno tehtati,
# osebje pa si je v datoteko zapisovalo rezultate tehtanj. V datoteko
# so zapisali imena prostovoljcev (vsako ime v svojo vrstico), pod imenom
# vsakega prostovoljca pa so dodali še meritve njegove teže. Vsaki meritvi
# so namenili eno vrstico, ki se prične z znakom `*`, sledi zaporedna
# številka dneva od začetka raziskave (celo število) in izmerjena teža
# v kilogramih (realno število). Podatki so ločeni s presledki,
# posamezne meritve za enega prostovoljca pa urejene po dnevu tehtanja.
# Primer takšne datoteke bi bil:
# 
#     Janez
#     * 2 55.2
#     * 5 56.1
#     * 8 55.8
#     * 11 55.0
#     Miha
#     * 4 88.2
#     * 7 87.4
#     * 12 86.9
#     * 22 85.4
#     Sonja
#     * 6 62.1
#     * 9 62.7
#     * 15 63.7
# =====================================================================@002839=
# 1. podnaloga
# Definiraj razred `Oseba`, s katerim bomo predstavili rezultate tehtanj za
# enega prostovoljca. Razred naj vsebuje konstruktor `__init__(self, ime)`,
# ki v atribut `ime` zapiše ime osebe, ki ga dobi za parameter, poleg tega pa
# nastavi še atribut `meritve`, katerega začetna vrednost naj bo prazen seznam.
# 
#     >>> janez = Oseba('Janez')
#     >>> janez.ime
#     'Janez'
#     >>> janez.meritve
#     []
# 
# Razredu dodaj še metodo `dodaj_meritev(self, dan, teza)`, pri čemer je `dan`
# zaporedna številka dneva od začetka raziskave, `teza` pa izmerjena teža
# prostovoljca na ta dan. Meritev doda na konec seznama meritev kot par
# (nabor dolžine 2).
# 
#     >>> janez.dodaj_meritev(2, 55.2)
#     >>> janez.dodaj_meritev(5, 56.1)
#     >>> janez.dodaj_meritev(8, 55.8)
#     >>> janez.dodaj_meritev(11, 55.0)
#     >>> janez.meritve
#     [(2, 55.2), (5, 56.1), (8, 55.8), (11, 55.0)]
# =============================================================================
class Oseba:
    def __init__(self,ime):
        self.ime = ime
        self.meritve = []

    def dodaj_meritev(self,dan,teza):
        return self.meritve.append((dan,teza))
    
# =====================================================================@002840=
# 2. podnaloga
# Sestavi funkcijo `preberi_podatke(ime_datoteke)`, ki prebere vsebino
# datoteke z imenom `ime_datoteke` ter vrne seznam objektov razreda `Oseba`,
# ki predstavljajo posamezne prostovoljce skupaj z njihovimi meritvami teže.
# 
#     >>> preberi_podatke('podatki.txt')
#     [Oseba(...), Oseba(...), Oseba(...)]
# =============================================================================
def preberi_podatke(ime_datoteke):
    seznam = []
    for oseba in open(ime_datoteke):
        seznam.append(oseba)
    return seznam
        
        
# =====================================================================@002841=
# 3. podnaloga
# Razredu `Oseba` dodaj metodo `teza_na_dan(self, dan)`, ki izračuna in
# vrne težo osebe na določen dan. Pri tem je `dan` zaporedna številka
# dneva od začetka raziskave.
# 
# Če oseba še nikoli ni bila stehtana, naj metoda vrne `None`,
# če oseba pred izbranim dnem še ni bila stehtana, naj vrne prvo izmerjeno težo,
# če oseba po izbranem dnevu ni bila stehtana, naj vrne zadnjo izmerjeno težo,
# če je oseba bila stehtana na izbrani dan, naj vrne takrat izmerjeno težo,
# sicer pa naj vrne približek teže, ki ga dobi kot vrednost linearne funkcije,
# ki poteka skozi zadnjo meritev pred izbranim dnem in prvo meritvijo po
# izbranem dnevu.
# 
#     >>> janez.teza_na_dan(5)
#     56.1
#     >>> janez.teza_na_dan(1)
#     55.2
#     >>> janez.teza_na_dan(20)
#     55.0
#     >>> janez.teza_na_dan(3)
#     55.5
# 
# Sestavi tudi funkcijo `najtezji_prostovoljec(ime_datoteke, dan)`,
# ki v seznamu oseb iz prejšnje podnaloge poišče najtežjega prostovoljca
# na določen dan in vrne njegovo ime. Pri tem je `dan` zaporedna številka
# dneva od začetka raziskave. Osebe, ki še niso bile stehtane, naj ignorira.
# Če ima več oseb isto težo, naj vrne ime prve takšne osebe iz seznama.
# Če še nobena oseba ni bila stehtana, naj vrne `None`.
# 
#     >>> najtezji_prostovoljec('podatki.txt', 10)
#     'Miha'
# =============================================================================
class Oseba(Oseba):
    def teza_na_dan(self,dan):
        if self.dodaj_meritev == []:
            return None


    def najtezji_prostovoljec(ime_datoteke,dan):
        if preberi_podatke(ime_datoteke) == []:
            return None
        



































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import io, json, os, re, sys, shutil, traceback, urllib.error, urllib.request
from contextlib import contextmanager


class Check:
    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []
        Check.current_part = None
        Check.part_counter = None

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6):
        if type(x) is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            return x if x else 0.0
        elif type(x) is complex:
            return complex(Check.clean(x.real, digits), Check.clean(x.imag, digits))
        elif type(x) is list:
            return list([Check.clean(y, digits) for y in x])
        elif type(x) is tuple:
            return tuple([Check.clean(y, digits) for y in x])
        elif type(x) is dict:
            return sorted([(Check.clean(k, digits), Check.clean(v, digits)) for (k, v) in x.items()])
        elif type(x) is set:
            return sorted([Check.clean(y, digits) for y in x])
        else:
            return x

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = clean or Check.clean
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env={}):
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        actual_result = eval(expression, globals(), local_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def run(statements, expected_state, clean=None, env={}):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        s = {}
        s.update(env)
        clean = clean or Check.clean
        exec(code, globals(), s)
        errors = []
        for (x, v) in expected_state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, s[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, encoding=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        sys.stdin = io.StringIO('\n'.join(content))
        try:
            yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            def visible_input(prompt):
                inp = input(prompt)
                print(inp)
                return inp
            exec(expression, {'input': visible_input})
        finally:
            output = sys.stdout.getvalue().strip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['je enaka'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def generator(expression, expected_values, should_stop=False, further_iter=0, env={}, clean=None):
        from types import GeneratorType
        local_env = locals()
        local_env.update(env)
        clean = clean or Check.clean
        gen = eval(expression, globals(), local_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(further_iter):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False
        
        if should_stop:
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\n'  # beginning of header
            r'(#( [^\n]*)?\n)+'       # description
            r'# =+\n'                 # end of header
            r'(?P<solution>.*?)'      # solution
            r'(?=\n# =+@)',           # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        try:
            Check.run(
                [
                    'janez = Oseba("Janez")',
                    'janez_ime = janez.ime',
                    'janez_meritve = janez.meritve'
                ],
                {
                    'janez_ime': 'Janez',
                    'janez_meritve': []
                }
            )
            Check.run(
                [
                    'janez = Oseba("Janez")',
                    'janez.dodaj_meritev(2, 55.2)',
                    'janez.dodaj_meritev(5, 56.1)',
                    'janez.dodaj_meritev(8, 55.8)',
                    'janez.dodaj_meritev(11, 55.0)',
                    'janez_meritve = janez.meritve'
                ],
                {
                    'janez_meritve': [(2, 55.2), (5, 56.1), (8, 55.8), (11, 55.0)]
                }
            )
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            podatki = [
                'Janez',
                '* 2 55.2',
                '* 5 56.1',
                '* 8 55.8',
                '* 11 55.0',
                'Miha',
                '* 4 88.2',
                '* 7 87.4',
                '* 12 86.9',
                '* 22 85.4',
                'Sonja',
                '* 6 62.1',
                '* 9 62.7',
                '* 15 63.7'
            ]
            izhod = []
            
            with Check.in_file('podatki.txt', podatki):
                Check.run(
                    [
                        'seznam = preberi_podatke("podatki.txt")',
                        'dolzina = len(seznam)',
                        'oseba0_tip = isinstance(seznam[0], Oseba)',
                        'oseba1_tip = isinstance(seznam[1], Oseba)',
                        'oseba2_tip = isinstance(seznam[2], Oseba)',
                        'oseba0_ime = seznam[0].ime',
                        'oseba1_ime = seznam[1].ime',
                        'oseba2_ime = seznam[2].ime',
                        'oseba0_meritve = seznam[0].meritve',
                        'oseba1_meritve = seznam[1].meritve',
                        'oseba2_meritve = seznam[2].meritve'
                    ],
                    {
                        'dolzina': 3,
                        'oseba0_tip': True,
                        'oseba1_tip': True,
                        'oseba2_tip': True,
                        'oseba0_ime': 'Janez',
                        'oseba1_ime': 'Miha',
                        'oseba2_ime': 'Sonja',
                        'oseba0_meritve': [(2, 55.2), (5, 56.1), (8, 55.8), (11, 55.0)],
                        'oseba1_meritve': [(4, 88.2), (7, 87.4), (12, 86.9), (22, 85.4)],
                        'oseba2_meritve': [(6, 62.1), (9, 62.7), (15, 63.7)]
                    }
                )
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.run(
                [
                    'janez = Oseba("Janez")',
                    'janez_teza0 = janez.teza_na_dan(0)',
                    'janez.dodaj_meritev(2, 55.2)',
                    'janez.dodaj_meritev(5, 56.1)',
                    'janez.dodaj_meritev(8, 55.8)',
                    'janez.dodaj_meritev(11, 55.0)',
                    'janez_teza5 = janez.teza_na_dan(5)',
                    'janez_teza1 = janez.teza_na_dan(1)',
                    'janez_teza20 = janez.teza_na_dan(20)',
                    'janez_teza3 = janez.teza_na_dan(3)',
                    'janez_teza4 = janez.teza_na_dan(4)',
                    'janez_teza7 = janez.teza_na_dan(7)'
                ],
                {
                    'janez_teza0': None,
                    'janez_teza5': 56.1,
                    'janez_teza1': 55.2,
                    'janez_teza20': 55.0,
                    'janez_teza3': 55.5,
                    'janez_teza4': 55.8,
                    'janez_teza7': 55.9
                }
            )
            
            podatki = [
                'Janez',
                '* 2 55.2',
                '* 5 56.1',
                '* 8 55.8',
                '* 11 55.0',
                'Miha',
                '* 4 88.2',
                '* 7 87.4',
                '* 12 86.9',
                '* 22 85.4',
                'Sonja',
                '* 6 62.1',
                '* 9 62.7',
                '* 15 63.7'
            ]
            
            with Check.in_file('prazno.txt', []):
                Check.equal('najtezji_prostovoljec("prazno.txt", 10)', None)
            
            with Check.in_file('brez_meritev.txt', ['Janez', 'Miha', 'Sonja']):
                Check.equal('najtezji_prostovoljec("brez_meritev.txt", 10)', None)
            
            with Check.in_file('podatki.txt', podatki):
                Check.equal('najtezji_prostovoljec("podatki.txt", 10)', 'Miha')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token 6c712ce844db84cfb7c9448f7d34169006653a8c'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        print('PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE! Poskusite znova.')
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print("Posodabljam datoteko... ", end="")
            backup_filename = backup(filename)
            r = urlopen(response['update'])
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    Check.summarize()

_validate_current_file()
