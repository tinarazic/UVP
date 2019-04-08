# =============================================================================
# Koti
#
# V tej nalogi boste pripravili razred, ki bo znal delati s koti ne glede na
# njihovo enoto. Za možne enote kotov glejte
# [stran na Wikipedii](https://en.wikipedia.org/wiki/Angle#Units), mi pa se
# bomo omejili na tiste, ki jih pozna vaš kalkulator, tj. stopinje, radiani in
# gradi.
# =====================================================================@002612=
# 1. podnaloga
# Definirajte razred `Kot` in v njem metodo `__init__(self, kot)`, ki si
# zapomni podani `kot`, ki ga shrani v atribut `vrednost` (kot decimalno
# število). Pri tem je `kot` lahko podan kot število (celo ali decimalno), pri
# čemer se predpostavi, da so pripadajoče enote radiani, ali pa je podan kot
# niz. Če niz predstavlja število, se spet šteje, da je kot v radianih. Če se
# niz konča s simbolom za stopinje `°`, se šteje, da je kot podan v stopinjah.
# Če se niz konča z `g`, se šteje, da je kot podan v gradih.
# 
# Dodajte še metodo `__call__(self)`, ki vrne kot v radianih.
# 
#     >>> a = Kot(5.3)
#     >>> a()
#     5.3
#     >>> a = Kot('-180°')
#     >>> a()
#     -3.141592653589793
#     >>> a = Kot('1000.5g')
#     >>> a()
#     15.71581724958294
# =============================================================================
import math
class Kot:
    
    def __init__(self,kot):
        self.kot = kot
          
        if type(kot) == int or type(kot) == float:
            self.vrednost = kot
        elif type(kot) == str:
            if kot.isdigit():
                self.vrednost = kot
            if kot[-1] == '°':
                self.vrednost = math.pi * int(kot[:-1]) / 180
            if kot[-1] == 'g':
                self.vrednost = 1/ 400 * int(kot[:-1])
    
            
        
# =====================================================================@002613=
# 2. podnaloga
# V razred `Kot` dodajte metodo `__eq__(self, other)`, ki vrne resničnostno
# vrednost, ali sta dana kota enaka, in metodo `__lt__(self, other)`, ki pove,
# ali je prvi kot manjši od drugega.
# 
#     >>> Kot('90°') == Kot('100g')
#     True
#     >>> Kot(1) < Kot('30°')
#     False
# =============================================================================
class Kot(Kot):
    def __eq__(self,other):
        if self.kot == other.kot:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.kot < other.kot:
            return True
        else:
            return False
# =====================================================================@002614=
# 3. podnaloga
# V razred `Kot` dodajte metodi `__add__(self, other)` in
# `__sub__(self, other)`, ki sešteje oziroma odšteje dva kota. Rezultat naj bo
# seveda v obeh primerih spet predstavnik razreda `Kot`.
# 
#     >>> a = Kot('90°') + Kot('100g')
#     >>> a()
#     3.141592653589793
#     >>> b = Kot(0) - Kot(2)
#     >>> b()
#     -2.0
# =============================================================================
class Kot(Kot):
    def __add__(self,other):
        return self.kot + other.kot
    def __sub__(self,other):
        return self.kot * other.kot
# =====================================================================@002615=
# 4. podnaloga
# V razred `Kot` dodajte metodo `okrajsaj()`, ki vrne vrednost z intervala
# $[0, 2\pi)$, ki predstavlja isti geometrijski kot (v radianih) kot dani kot.
# 
#     >>> a = Kot('480°')
#     >>> a.okrajsaj()
#     2.094395102393195
#     >>> b = Kot(-1)
#     >>> b.okrajsaj()
#     5.283185307179586
# =============================================================================
import math
class Kot(Kot):
    def okrajsaj():
        return self.kot - kot // 2 * math.pi
        




































































































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
            import math
            test_data = [
                (["alpha = Kot(5.3)",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 5.3, 'y': 5.3}),
                (["alpha = Kot(math.pi / 2)",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 1.57079633, 'y': 1.57079633}),
                (["alpha = Kot(math.pi / 4)",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 0.78539816, 'y': 0.78539816}),
                (["alpha = Kot(-math.pi / 6)",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': -0.52359878, 'y': -0.52359878}),
                (["alpha = Kot('5.3')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 5.3, 'y': 5.3}),
                (["alpha = Kot('-5.3e-2')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': -0.053, 'y': -0.053}),
                (["alpha = Kot('5.3e2')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 530.0, 'y': 530.0}),
                (["alpha = Kot('-180°')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': -3.1415927, 'y': -3.1415927}),
                (["alpha = Kot('60°')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 1.04719755, 'y': 1.04719755}),
                (["alpha = Kot('30°')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 0.52359878, 'y': 0.52359878}),
                (["alpha = Kot('3050e-2°')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 0.53232542, 'y': 0.53232542}),
                (["alpha = Kot('1000.5g')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 15.71581725, 'y': 15.71581725}),
                (["alpha = Kot('105g')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': 1.64933614, 'y': 1.64933614}),
                (["alpha = Kot('-105g')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': -1.64933614, 'y': -1.64933614}),
                (["alpha = Kot('-105.002g')",
                  "y = round(alpha.vrednost, 8)",
                  "x = round(alpha(), 8)"],
                 {'x': -1.64936756, 'y': -1.64936756}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break  # Test has failed!
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            import math
            Check.equal("Kot('90°') == Kot('100g')", True)
            Check.equal("Kot(1) < Kot('30°')", False)
            Check.equal("Kot('45°') == Kot('50g')", True)
            Check.equal("Kot(math.pi / 6) == Kot('30°')", True)
            Check.equal("Kot(math.pi / 4) == Kot('45°')", True)
            Check.equal("Kot(math.pi / 4) == Kot('45g')", False)
            Check.equal("Kot(math.pi / 4) == Kot('50g')", True)
            Check.equal("Kot(math.pi / 4) == Kot('50°')", False)
            Check.equal("Kot(math.pi / 3) == Kot('30°')", False)
            Check.equal("Kot(1) < Kot(2)", True)
            Check.equal("Kot('30°') < Kot('30g')", False)
            Check.equal("Kot('30g') < Kot('30°')", True)
            Check.equal("Kot('30°') < Kot(math.pi / 4)", True)
            Check.equal("Kot(math.pi / 6) < Kot('45°')", True)
            Check.equal("Kot(math.pi / 6) < Kot('50g')", True)
            Check.equal("Kot('45°') < Kot(math.pi / 6)", False)
            Check.equal("Kot('50g') < Kot(math.pi / 6)", False)
            Check.equal("Kot(2) < Kot(1)", False)
            Check.equal("Kot(1) < Kot(1)", False)
            Check.equal("Kot('1') < Kot(2)", True)
            Check.equal("Kot(2) < Kot('1')", False)
            Check.equal("Kot('1') < Kot('1')", False)
            Check.equal("Kot('1') == Kot(1)", True)
            Check.equal("Kot(1) == Kot('2')", False)
            Check.equal("Kot(1) == Kot(1)", True)
            Check.equal("Kot(1) == Kot(2)", False)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            import math
            test_data = [
                (["alpha = Kot('90°') + Kot('100g')",
                  "x = round(alpha(), 8)"],
                 {'x': 3.14159265}),
                (["alpha = Kot(0) - Kot(2)",
                  "x = round(alpha(), 8)"],
                 {'x': -2}),
                (["alpha = Kot('90°') - Kot('100g')",
                  "x = round(alpha(), 8)"],
                 {'x': 0.0}),
                (["alpha = Kot(0) + Kot('2')",
                  "x = round(alpha(), 8)"],
                 {'x': 2.0}),
                (["alpha = Kot('30°') + Kot('30°')",
                  "x = round(alpha(), 8)"],
                 {'x': 1.04719755}),
                (["alpha = Kot(math.pi / 6) + Kot('30°')",
                  "x = round(alpha(), 8)"],
                 {'x': 1.04719755}),
                (["alpha = Kot('30°') + Kot('60°')",
                  "x = round(alpha(), 8)"],
                 {'x': 1.57079633}),
                (["alpha = Kot('30°') - Kot('60°')",
                  "x = round(alpha(), 8)"],
                 {'x': -0.52359878}),
                (["alpha = Kot('60°') - Kot(math.pi / 6)",
                  "x = round(alpha(), 8)"],
                 {'x': 0.52359878}),
                (["alpha = Kot(0) - Kot('0') + Kot('0°') - Kot('0g')",
                  "x = round(alpha(), 8)"],
                 {'x': 0.0}),
            ]
            for td in test_data:
                if not Check.run(*td):
                    break  # Test has failed!
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal("round(Kot('480°').okrajsaj(), 8)", 2.0943951)
            Check.equal("round(Kot('-480°').okrajsaj(), 8)", 4.1887902)
            Check.equal("round(Kot('-1').okrajsaj(), 8)", 5.28318530)
            Check.equal("round(Kot('1').okrajsaj(), 8)", 1.0)
            Check.equal("round(Kot('1.2').okrajsaj(), 8)", 1.2)
            Check.equal("round(Kot('3.14').okrajsaj(), 8)", 3.14)
            Check.equal("round(Kot('0').okrajsaj(), 8)", 0)
            Check.equal("round(Kot(0).okrajsaj(), 8)", 0)
            Check.equal("round(Kot('0g').okrajsaj(), 8)", 0)
            Check.equal("round(Kot('0°').okrajsaj(), 8)", 0)
            Check.equal("round(Kot(2 * math.pi).okrajsaj(), 8)", 0)
            Check.equal("round(Kot('360°').okrajsaj(), 8)", 0)
            Check.equal("round(Kot('400g').okrajsaj(), 8)", 0)
            Check.equal("round(Kot(100 * math.pi + 1).okrajsaj(), 8)", 1.0)
            Check.equal("round(Kot('5050°').okrajsaj(), 8)", 0.17453293)
            Check.equal("round(Kot('-5050°').okrajsaj(), 8)", 6.10865238)
            Check.equal("round(Kot('5610g').okrajsaj(), 8)", 0.15707963)
            Check.equal("round(Kot('-5610g').okrajsaj(), 8)", 6.12610567)
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
