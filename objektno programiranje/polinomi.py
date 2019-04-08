# =============================================================================
# Polinomi
#
# Definirajte razred `Polinom`, s katerim predstavimo polinom v
# spremenljivki $x$. Polinom predstavimo s seznamom njegovih koeficientov,
# kjer je $k$-ti element seznama koeficient pri $x^k$.
# 
# Na primer, polinom $x^3 + 2x + 7$ predstavimo s `Polinom([7, 2, 0, 1])`.
# Razmislite, kaj predstavlja `Polinom([])`. Zadnji koeficient v seznamu
# mora biti neničelen.
# =====================================================================@001741=
# 1. podnaloga
# Sestavite konstruktor `__init__(self, koef)`, ki nastavi objektu
# nastavi atribut `koef` (koeficienti polinoma). Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.koef
#     [7, 2, 0, 1]
# 
# _Pozor_: Če kasneje spremenimo seznam, ki smo ga kot argument podali
# konstruktorju, se koeficienti polinoma ne smejo premeniti. Seznama,
# ki smo ga podali kot argument, konstruktor prav tako ne sme spremeninjati.
# Zgled:
# 
#     >>> l = [2, 0, 1]
#     >>> p = Polinom(l)
#     >>> l.append(3)
#     >>> p.koef
#     [2, 0, 1]
# =============================================================================

# =====================================================================@001742=
# 2. podnaloga
# Sestavite metodo `stopnja(self)`, ki vrne stopnjo polinoma. Zgled:
# 
#     >>> p = Polinom([7, 2, 0, 1])
#     >>> p.stopnja()
#     3
# 
# _Opomba_: Za razpravo glede stopnje ničelnega polinoma glejte [članek
# na Wikipediji](http://en.wikipedia.org/wiki/Degree_of_a_polynomial#Degree_of_the_zero_polynomial).
# =============================================================================

# =====================================================================@001743=
# 3. podnaloga
# Sestavite metodo `__repr__(self)`, ki vrne niz oblike
# `'Polinom([a_0, …, a_n])'`, kjer so `a_0, …, a_n` koeficienti polinoma.
# Zgled:
# 
#     >>> p = Polinom([5, 0, 1])
#     >>> p
#     Polinom([5, 0, 1])
# =============================================================================

# =====================================================================@001744=
# 4. podnaloga
# Sestavite metodo `__eq__(self, other)` za primerjanje polinomov. Zgled:
# 
#     >>> Polinom([3, 2, 0, 1]) == Polinom([3, 2])
#     False
#     >>> Polinom([3, 2, 1, 0]) == Polinom([3, 2, 1])
#     True
# =============================================================================

# =====================================================================@001745=
# 5. podnaloga
# Sestavite metodo `__call__(self, x)`, ki izračuna in vrne vrednost
# polinoma v `x`. Pri izračunu vrednosti uporabite Hornerjev algoritem.
# Če definiramo metodo `__call__`, objekt postane "klicljiv" (tj. lahko
# ga kličemo, kakor da bi bil funkcija). Zgled:
# 
#     >>> p = Polinom([3, 2, 0, 1])
#     >>> p(1)
#     6
#     >>> p(-3)
#     -30
#     >>> p(0.725)
#     4.8310781249999994
# =============================================================================

# =====================================================================@001746=
# 6. podnaloga
# Sestavite metodo `__add__(self, other)` za seštevanje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo vsota polinomov
# `self` in `other`. Zgled:
# 
#     >>> Polinom([1, 0, 1]) + Polinom([4, 2])
#     Polinom([5, 2, 1])
# 
# _Pozor_: Pri seštevanju se lahko zgodi, da se nekateri koeficienti
# pokrajšajo: $(x^3 + 2x + 7) + (-x^3 - 2x + 10) = 17$.
# =============================================================================

# =====================================================================@001747=
# 7. podnaloga
# Sestavite metodo `__mul__(self, other)` za množenje polinomov. Metoda
# naj sestavi in vrne nov objekt razreda `Polinom`, ki bo produkt polinomov
# `self` in `other`. Zgled:
# 
#     >>> Polinom([1, 0, 1]) * Polinom([4, 2])
#     Polinom([4, 2, 4, 2])
# =============================================================================

# =====================================================================@001748=
# 8. podnaloga
# Sestavite metodo `odvod(self, k)`, sestavi in vrne nov polinom, ki bo
# $k$-ti odvod polinoma `self`. Argument `k` naj ima privzeto vrednost 1.
# Zgled:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     >>> p.odvod()
#     Polinom([1, 8, -9, 20, -5])
#     >>> p.odvod(2)
#     Polinom([8, -18, 60, -20])
# =============================================================================

# =====================================================================@001749=
# 9. podnaloga
# Sestavite metodo `__str__(self)`, ki predstavi polinom v čitljivi obliki,
# kot kaže primer:
# 
#     >>> p = Polinom([5, 1, 4, -3, 5, -1])
#     -x^5 + 5x^4 - 3x^3 + 4x^2 + x + 5
# 
# Za niz, ki ga funkcija vrne, naj velja naslednje:
# 
# * Polinom je sestavljen iz monomov oblike `ax^k`, kjer je `a` ustrezen
#   koeficient.
# * Monomi so med seboj povezani z znaki `+`; pred in za plusom je po en
#   presledek.
# * Namesto `x^1` bomo pisali samo `x`, `x^0` pa bomo izpustili in pisali
#   samo koeficient.
# * Če je koeficient 1, bomo namesto `1x^k` pisali `x^k`. Če je -1, bomo
#   namesto `-1x^k` pisali `-x^k`. To ne velja za prosti člen.
# * Če je koeficient negativen, bomo pri združevanju monomov uporabili
#   znak `-` namesto znaka `+`. Torej, namesto `ax^m + -bx^n` bomo pisali
#   `ax^m - bx^n`. To ne velja za vodilni člen.
# * Če je koeficient 0, bomo monom izpustili. To pravilo ne velja za
#   ničelni polinom.
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
            test_data = [
                ('Polinom([1, 2, 3]).koef', [1, 2, 3]),
                ('Polinom([1, 2, 0, 0]).koef', [1, 2]),
                ('Polinom([0, 0, 0, 0]).koef', []),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 7]).koef', [0, 0, 0, 0, 0, 0, 0, 7]),
            ]
            additional_tests = [
                (["l = [1, 2, 3, 0, 0, 0]",
                  "p = Polinom(l)",
                  "k = p.koef"],
                 {'l': [1, 2, 3, 0, 0, 0],
                  'k': [1, 2, 3]}),
                (["l = [1, 2, 3, 0, 0, 0]",
                  "p = Polinom(l)",
                  "l.extend([13, 14, 15])",
                  "k = p.koef"],
                 {'l': [1, 2, 3, 0, 0, 0, 13, 14, 15],
                  'k': [1, 2, 3]}),
                (["l = [1, 2, 3]",
                  "p = Polinom(l)",
                  "del l[-1]",
                  "del l[-1]", 
                  "k = p.koef"],
                 {'l': [1],
                  'k': [1, 2, 3]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
                        break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([7, 2, 0, 1]).stopnja()', 3),
                ('Polinom([1, 2, 3]).stopnja()', 2),
                ('Polinom([1, 2, 3, 4, 5, 13, -22]).stopnja()', 6),
                ('Polinom([1]).stopnja()', 0),
                ('Polinom([]).stopnja()', float('-inf')),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('repr(Polinom([1, 2, 3]))', "Polinom([1, 2, 3])"),
                ('repr(Polinom([1, 2, 3, 0, 0]))', "Polinom([1, 2, 3])"),
                ('repr(Polinom([]))', "Polinom([])"),
                ('repr(Polinom([0, 0]))', "Polinom([])"),
                ('repr(Polinom([1, 3]))', "Polinom([1, 3])"),
                ('repr(Polinom([7]))', "Polinom([7])"),
                ('repr(Polinom([1, -2, 3, -1]))', "Polinom([1, -2, 3, -1])"),
                ('repr(Polinom([1, 0, 0, -1]))', "Polinom([1, 0, 0, -1])"),
                ('repr(Polinom([0, 0, 0, -5]))', "Polinom([0, 0, 0, -5])"),
                ('repr(Polinom([-1, 2, -3, 1]))', "Polinom([-1, 2, -3, 1])"),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([1, 2, 3]) == Polinom([1, 2, 3, 0, 0])', True),
                ('Polinom([3, 2, 1, 0]) == Polinom([3, 2])', False),
                ('Polinom([3, 2, 1, 0]) == Polinom([3, 2, 1])', True),
                ('Polinom([1, 2, 3]) != Polinom([0, 1, 2, 3])', True),
                ('Polinom([1, 2, 3]) == Polinom([3, 2, 1])', False),
                ('Polinom([]) == Polinom([3, 2, 1])', False),
                ('Polinom([]) == Polinom([0])', True),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([3, 2, 0, 1])(1)', 6),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(0)', 1),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(1)', 9),
                ('Polinom([1, 1, 1, 1, 1, 1, 1, 1, 1])(3)', 9841),
                ('Polinom([3, 2, 0, 1])(-3)', -30),
                ('Polinom([3, 2, 0, 1])(0.725)', 4.8310781249999994),
                ('Polinom([])(1337)', 0),
                ('Polinom([])(-666)', 0),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([1, 2, 3, 0, 0, 0, 0, 7]) + Polinom([4, 5])', Polinom([5, 7, 3, 0, 0, 0, 0, 7])),
                ('Polinom([1, 2, 3]) + Polinom([4, 5, 0, 0, 0, 0, 0, 0, -1])', Polinom([5, 7, 3, 0, 0, 0, 0, 0, -1])),
                ('Polinom([1, 2, 3]) + Polinom([4, 5])', Polinom([5, 7, 3])),
                ('Polinom([1, 0, 1]) + Polinom([4, 2])', Polinom([5, 2, 1])),
                ('Polinom([1, 2, 3]) + Polinom([-1, -2])', Polinom([0, 0, 3])),
                ('Polinom([1, 2, 3]) + Polinom([0, 0, -3])', Polinom([1, 2])),
            ]
            additional_tests = [
                (["p = Polinom([1, 2, 3])",
                  "q = Polinom([1, 2, 3, 4, 5, 6, 7])",
                  "r = p + q",
                  "p_koef, q_koef = p.koef, q.koef"],
                 {'r': Polinom([2, 4, 6, 4, 5, 6, 7]),
                  'p_koef': [1, 2, 3],
                  'q_koef': [1, 2, 3, 4, 5, 6, 7]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
                        break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([1, 0, 1]) * Polinom([4, 2])', Polinom([4, 2, 4, 2])),
                ('Polinom([0, 0, 0, 0, 0, 0, 1]) * Polinom([0, 0, 0, 0, 0, 0, 1])',
                 Polinom([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])),
                ('Polinom([1, 0, 1]) * Polinom([])', Polinom([])),
                ('Polinom([]) * Polinom([4, 2])', Polinom([])),
                ('Polinom([]) * Polinom([])', Polinom([])),
                ('Polinom([1, 2, 3]) * Polinom([2])', Polinom([2, 4, 6])),
                ('Polinom([1, 2, 1]) * Polinom([1, 1])', Polinom([1, 3, 3, 1])),
                ('Polinom([1, 2, 1, 3, 1]) * Polinom([1, 1, 5, 4, 3, 1])', Polinom([1, 3, 8, 18, 20, 27, 22, 14, 6, 1])),
                ('Polinom([1, 2, 3]) * Polinom([0, 0, 0])', Polinom([])),
            ]
            additional_tests = [
                (["p = Polinom([1, 2, 3])",
                  "q = Polinom([1, 2, 3, 4, 5, 6, 7])",
                  "r = p * q",
                  "p_koef, q_koef = p.koef, q.koef"],
                 {'r': Polinom([1, 4, 10, 16, 22, 28, 34, 32, 21]),
                  'p_koef': [1, 2, 3],
                  'q_koef': [1, 2, 3, 4, 5, 6, 7]}),
            ]
            vse_ok = True
            for td in test_data:
                if not Check.equal(*td):
                    vse_ok = False
                    break
            if vse_ok:
                for td in additional_tests:
                    if Check.run(*td):
                        break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Polinom([5, 1, 4, -3, 5, -1]).odvod()', Polinom([1, 8, -9, 20, -5])),
                ('Polinom([5, 1, 4, -3, 5, -1]).odvod(2)', Polinom([8, -18, 60, -20])),
                ('Polinom([1, 2, 3]).odvod()', Polinom([2, 6])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod()', Polinom([2, 2, 0, 4, 10, 18])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod()',  Polinom([0, 0, 0, 0, 0, 0, 0, 8])),
                ('Polinom([5, 4, 3, 2, 1]).odvod()', Polinom([4, 6, 6, 4])),
                ('Polinom([1]).odvod()', Polinom([])),
                ('Polinom([]).odvod()', Polinom([])),
                ('Polinom([5, 4, 3, 2, 1]).odvod(0)', Polinom([5, 4, 3, 2, 1])),
                ('Polinom([1]).odvod(0)', Polinom([1])),
                ('Polinom([1, 2, 3]).odvod(2)', Polinom([6])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod(2)', Polinom([2, 0, 12, 40, 90])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(2)', Polinom([0, 0, 0, 0, 0, 0, 56])),
                ('Polinom([1, 2, 3]).odvod(3)', Polinom([])),
                ('Polinom([3, 2, 1, 0, 1, 2, 3]).odvod(3)', Polinom([0, 24, 120, 360])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(3)', Polinom([0, 0, 0, 0, 0, 336])),
                ('Polinom([0, 0, 0, 0, 0, 0, 0, 0, 1]).odvod(8)', Polinom([40320])),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('str(Polinom([1, 2, 3]))', "3x^2 + 2x + 1"),
                ('str(Polinom([-1, -2, -3]))', "-3x^2 - 2x - 1"),
                ('str(Polinom([-1, -1, 1]))', "x^2 - x - 1"),
                ('str(Polinom([1, 1, -1]))', "-x^2 + x + 1"),
                ('str(Polinom([1, 1, 1, 1, 1, 1, 1, 1]))', 'x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1'),
                ('str(Polinom([0, 0, 0, 0, 0, 0, 0, 1]))', 'x^7'),
                ('str(Polinom([5, 1, 4, -3, 5, -1]))', "-x^5 + 5x^4 - 3x^3 + 4x^2 + x + 5"),
                ('str(Polinom([1, 3]))', "3x + 1"),
                ('str(Polinom([1, -2, 3, -1]))', "-x^3 + 3x^2 - 2x + 1"),
                ('str(Polinom([1, 0, 0, -1]))', "-x^3 + 1"),
                ('str(Polinom([0, 0, 0, -5]))', "-5x^3"),
                ('str(Polinom([-1, 2, -3, 1]))', "x^3 - 3x^2 + 2x - 1"),
                ('str(Polinom([]))', "0"),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
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
