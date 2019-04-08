# =============================================================================
# Permutacija
#
# Najbolj popularnih zapisov permutacije je po mnenju mnogih ciklični zapis
# (tj. permutacijo zapišemo kot produkt disjunktnih ciklov). Primer:
# 
#     (1 5 2) (3 6) (4)
# 
# Ciklov dolžine 1 (fiksnih točk) po navadi ne pišemo, torej zgornjo
# permutacijo običajno pišemo kar takole:
# 
#     (1 5 2) (3 6)
# =====================================================================@002145=
# 1. podnaloga
# Sestavite razred `Permutacija`, s katerim predstavimo permutacijo.
# Najprej sestavite konstruktor `__init__(self, cikli, stopnja=None)`, kjer
# je `cikli` seznam seznamov, ki predstavljajo cikle permutacije. Argument
# `stopnja` ima privzeto vrednost `None` – v tem primeru naj bo stopnja
# največje število, ki nastopa v katerem od ciklov. Razred naj ima atributa
# `stopnja` in `cikli`. Na prvem mestu v vsakem ciklu naj bo najmanjši
# element tega cikla (s cikličnim pomikom dobimo isti cikel). Tudi cikli
# naj bodo urejeni. Morebitne cikle dožine 1 naj konstruktor odstrani.
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.stopnja
#     7
#     >>> p.cikli
#     [[1, 5, 2], [3, 7]]
# =============================================================================

# =====================================================================@002146=
# 2. podnaloga
# V razredu `Permutacija` definirajte metodo `inverz(self)`, ki sestavi
# in vrne inverz dane permutacije. Inverz permutacije dobimo tako, da
# v cikličnem zapisu obrnemo vse cikle (vsakega posebej).
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> q = p.inverz()
#     >>> q.stopnja
#     7
#     >>> q.cikli
#     [[1, 2, 5], [3, 7]]
# =============================================================================

# =====================================================================@002147=
# 3. podnaloga
# V razredu `Permutacija` sestavite metodo `ciklicni_tip(self)`, ki vrne
# ciklični tip permutacije. To je nabor, ki ima toliko elementov, kot je
# dolžina najdaljšega cikla. Prvi element v tem naboru je število ciklov
# dolžine 1, drugi element je število ciklov dolžine 2, itn.
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.ciklicni_tip()
#     (2, 1, 1)
# =============================================================================

# =====================================================================@002148=
# 4. podnaloga
# V razredu `Permutacija` sestavite metodo `red(self)`, ki izračuna in
# vrne red permutacije. Naj bo $\pi$ permutacija. Red permutacije $\pi$ je
# najmanjše pozitivno število $k$, pri katerem je $\pi^k$ identiteta.
# 
# Namig 1: Red permutacije je najmanjši skupni večkratnik dolžin vseh ciklov.
# 
# Namig 2: Za poljubni dve naravni števili `a` in `b` velja, da je
# `gcd(a, b) * lcm(a, b) == a * b`. (Funkcija `gcd` računa največji
# skupni delitelj, funkcija `lcm` pa najmanjši skupni večkratnik.)
# 
#     >>> p = Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=7)
#     >>> p.red()
#     6
# =============================================================================





































































































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
            exec(Check.current_part['solution'], {'input': visible_input})
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
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).stopnja', 9)
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).cikli', [[1, 5, 2], [3, 7]])
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).stopnja', 7)
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).cikli', [[1, 5, 2], [3, 7]])
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).stopnja', 14)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).cikli', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).stopnja', 21)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).cikli', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).stopnja', 18)
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).cikli', [[2, 14, 8], [3, 7, 9, 13, 5], [4, 6, 11, 12], [15, 18]])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).inverz().stopnja', 9)
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).inverz().cikli', [[1, 2, 5], [3, 7]])
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).inverz().stopnja', 7)
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).inverz().cikli', [[1, 2, 5], [3, 7]])
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).inverz().stopnja', 14)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).inverz().cikli', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).inverz().stopnja', 21)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).inverz().cikli', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).inverz().stopnja', 18)
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).inverz().cikli', [[2, 8, 14], [3, 5, 13, 9, 7], [4, 12, 11, 6], [15, 18]])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).ciklicni_tip()', (4, 1, 1))
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).ciklicni_tip()', (2, 1, 1))
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).ciklicni_tip()', (0, 7))
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).ciklicni_tip()', (7, 7))
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).ciklicni_tip()', (4, 1, 1, 1, 1))
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]], stopnja=9).red()', 6)
            Check.equal('Permutacija([[7, 3], [4], [5, 2, 1]]).red()', 6)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]]).red()', 2)
            Check.equal('Permutacija([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], stopnja=21).red()', 2)
            Check.equal('Permutacija([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]]).red()', 60)
            Check.equal('Permutacija([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]]).red()', 210)
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
