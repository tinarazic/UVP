# =============================================================================
# Ulomki
# =====================================================================@001731=
# 1. podnaloga
# Izven razreda sestavite funkcijo `gcd(m, n)`, ki izračuna največji skupni
# delitelj števil `m` in `n`. Zgled:
# 
#     >>> gcd(35, 63)
#     7
# =============================================================================
def gcd(m,n):
    while n != 0:
        m, n = n, m%n
    return m
# =====================================================================@001732=
# 2. podnaloga
# Definirajte razred `Ulomek`, s katerim predstavimo ulomek. Števec in
# imenovalec sta celi števili, pri čemer je morebiten negativen predznak
# vedno v števcu. Ulomki naj bodo vedno okrajšani. Atributa naj se
# imenujeta `st` in `im`.
# 
# Najprej definirajte konstruktor `__init__(self, st, im)`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> u.st
#     1
#     >>> u.im
#     4
# =============================================================================
class Ulomek:
    
    def __init__(self, st, im):
        delitelj = gcd(st,im)
        self.st = st // delitelj
        self.im = im // delitelj
        if self.im < 0:
            self. im = -self.im
            self.st = -self.st
        
# =====================================================================@001733=
# 3. podnaloga
# Definirajte metodo  `__str__(self)`, ki predstavi ulomek z nizom
# oblike `'st/im'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> print(u)
#     1/4
# =============================================================================
class Ulomek(Ulomek):
    def __str__(self):
        return '{}/{}'.format(self.st,self.im)
# =====================================================================@001734=
# 4. podnaloga
# Definirajte še metodo  `__repr__(self)`, ki predstavi ulomek z nizom
# oblike `'Ulomek(st, im)'`. Zgled:
# 
#     >>> u = Ulomek(5, 20)
#     >>> u
#     Ulomek(1, 4)
# =============================================================================
class Ulomek(Ulomek):
    def __repr__(self):
        return 'Ulomek({}, {})'.format(self.st,self.im)
# =====================================================================@001735=
# 5. podnaloga
# Definirajte metodo  `__eq__(self, other)`, ki vrne `True` če sta dva
# ulomka enaka, in `False` sicer. Zgled:
# 
#     >>> Ulomek(1, 3) == Ulomek(2, 3)
#     False
#     >>> Ulomek(2, 3) == Ulomek(10, 15)
#     True
# =============================================================================
class Ulomek(Ulomek):
    def __eq__(self,other):
        if self.st == other.st and self.im == other.im:
            return True
        else:
            return False
# =====================================================================@001736=
# 6. podnaloga
# Definirajte metodo  `__add__(self, other)`, ki vrne vsoto dveh ulomkov.
# Ko definirate to metodo, lahko ulomke seštevate kar z operatorjem `+`.
# Na primer:
# 
#     >>> Ulomek(1, 6) + Ulomek(1, 4)
#     Ulomek(5, 12)
# =============================================================================
class Ulomek(Ulomek):
    def __add__(self,other):
        a = self.st
        b = self.im
        c = other.st
        d = other.im
        X= a*d +b*c
        Y= b * d
        return Ulomek(X,Y)
# =====================================================================@001737=
# 7. podnaloga
# Definirajte metodo  `__sub__(self, other)`, ki vrne razliko dveh ulomkov.
# Ko definirate to metodo, lahko ulomke odštevate kar z operatorjem `-`.
# Na primer:
# 
#     >>> Ulomek(1, 4) - Ulomek(1, 6)
#     Ulomek(1, 12)
# =============================================================================
class Ulomek(Ulomek):
    def __sub__(self,other):
        a = self.st
        b = self.im
        c = other.st
        d = other.im
        X= a*d  - b*c
        Y= b * d
        return Ulomek(X,Y)
# =====================================================================@001738=
# 8. podnaloga
# Definirajte metodo  `__mul__(self, other)`, ki vrne zmnožek dveh ulomkov.
# Ko definirate to metodo, lahko ulomke množite kar z operatorjem `*`.
# Na primer:
# 
#     >>> Ulomek(1, 3) * Ulomek(1, 2)
#     Ulomek(1, 6)
# =============================================================================
class Ulomek(Ulomek):
    def __mul__(self,other):
        a = self.st
        b = self.im
        c = other.st
        d = other.im
        X= a*c
        Y= b*d
        return Ulomek(X,Y)
# =====================================================================@001739=
# 9. podnaloga
# Definirajte metodo  `__truediv__(self, other)`, ki vrne kvocient dveh
# ulomkov. Ko definirate to metodo, lahko ulomke delite kar z operatorjem
# `/`. Na primer:
# 
#     >>> Ulomek(1, 6) / Ulomek(1, 4)
#     Ulomek(2, 3)
# =============================================================================
class Ulomek(Ulomek):
    def __truediv__(self,other):
        a = self.st
        b = self.im
        c = other.st
        d = other.im
        X= a*d
        Y= b*c
        return Ulomek(X,Y)
# =====================================================================@001740=
# 10. podnaloga
# Izven razreda `Ulomek` definirajte funkcijo `priblizek(n)`, ki vrne
# vsoto $$\frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + … + \frac{1}{n!}.$$
# Funkcija naj uporablja razred `Ulomek`. Zgled:
# 
#     >>> priblizek(5)
#     Ulomek(163, 60)
# 
# Ali je izračunana vrednost blizu števila $e$?
# =============================================================================
def fakulteta (n):
    if n==0:
        return 1
    else:
        return n * fakulteta(n-1)
def priblizek(n):
    vsota= Ulomek(0,1)
    for i in range(0,n+1):
        vsota += Ulomek(1,fakulteta(i))
    return vsota




































































































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
                ('gcd(63, 35)', 7),
                ('gcd(40, 35)', 5),
                ('gcd(40, 19)', 1),
                ('gcd(15, 69)', 3),
                ('gcd(12345, 6789)', 3),
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
                ('Ulomek(5, 1).st', 5),
                ('Ulomek(5, 1).im', 1),
                ('Ulomek(5, 20).st', 1),
                ('Ulomek(5, 20).im', 4),
                ('Ulomek(20, 6).st', 10),
                ('Ulomek(20, 6).im', 3),
                ('Ulomek(5, 7).st', 5),
                ('Ulomek(5, 7).im', 7),
                ('Ulomek(7, 5).st', 7),
                ('Ulomek(7, 5).im', 5),
                ('Ulomek(-7, 5).st', -7),
                ('Ulomek(-7, 5).im', 5),
                ('Ulomek(-7, -5).st', 7),
                ('Ulomek(-7, -5).im', 5),
                ('Ulomek(0, 7).st', 0),
                ('Ulomek(0, 7).im', 1),
                ('Ulomek(40, -60).im', 3),
                ('Ulomek(40, -60).st', -2),
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
                ('str(Ulomek(20, 6))', '10/3'),
                ('str(Ulomek(0, 113))', '0/1'),
                ('str(Ulomek(40, -60))', '-2/3'),
                ('str(Ulomek(5, 20))', '1/4'),
                ('str(Ulomek(5, 7))', '5/7'),
                ('str(Ulomek(7, 5))', '7/5'),
                ('str(Ulomek(-7, 5))', '-7/5'),
                ('str(Ulomek(7, -5))', '-7/5'),
                ('str(Ulomek(-7, -5))', '7/5'),
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
                ('repr(Ulomek(20, 6))', 'Ulomek(10, 3)'),
                ('repr(Ulomek(0, 226))', 'Ulomek(0, 1)'),
                ('repr(Ulomek(40, -60))', 'Ulomek(-2, 3)'),
                ('repr(Ulomek(5, 20))', 'Ulomek(1, 4)'),
                ('repr(Ulomek(5, 7))', 'Ulomek(5, 7)'),
                ('repr(Ulomek(7, 5))', 'Ulomek(7, 5)'),
                ('repr(Ulomek(-7, 5))', 'Ulomek(-7, 5)'),
                ('repr(Ulomek(7, -5))', 'Ulomek(-7, 5)'),
                ('repr(Ulomek(-7, -5))', 'Ulomek(7, 5)'),
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
                ('Ulomek(1, 3) == Ulomek(2, 3)', False),
                ('Ulomek(2, 3) == Ulomek(10, 15)', True),
                ('Ulomek(0, 3) == Ulomek(0, 2215)', True),
                ('Ulomek(20, 6) == Ulomek(10, 3)', True),
                ('Ulomek(-10, 3) == Ulomek(10, 3)', False),
                ('Ulomek(10, -3) == Ulomek(10, 3)', False),
                ('Ulomek(1, 4) == Ulomek(4, 1)', False),
                ('Ulomek(20, 6) == Ulomek(10, 3)', True),
                ('Ulomek(40, -60) == Ulomek(-2, 3)', True),
                ('Ulomek(5, 20) == Ulomek(1, 4)', True),
                ('Ulomek(5, 7) == Ulomek(5, 7)', True),
                ('Ulomek(7, 5) == Ulomek(7, 5)', True),
                ('Ulomek(-7, 5) == Ulomek(-7, 5)', True),
                ('Ulomek(7, -5) == Ulomek(-7, 5)', True),
                ('Ulomek(-7, -5) == Ulomek(7, 5)', True),
                ('Ulomek(999999999, 1000000000) == Ulomek(999999998, 999999999)', False),
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
                ('Ulomek(1, 6) + Ulomek(1, 4)', Ulomek(5, 12)),
                ('Ulomek(1, -6) + Ulomek(-1, 4)', Ulomek(-5, 12)),
                ('Ulomek(1, 6) + Ulomek(-1, 4)', Ulomek(-1, 12)),
                ('Ulomek(1, -6) + Ulomek(1, 4)', Ulomek(1, 12)),
                ('Ulomek(1, 6) + Ulomek(1, 6)', Ulomek(1, 3)),
                ('Ulomek(1, 6) + Ulomek(-1, 6)', Ulomek(0, 1)),
                ('Ulomek(60, 1) + Ulomek(-1, 60)', Ulomek(3599, 60)),
                ('Ulomek(1, 2014) + Ulomek(1, 2015)', Ulomek(4029, 4058210)),
                ('Ulomek(1, 2014) + Ulomek(1, -2015)', Ulomek(1, 4058210)),
                ('Ulomek(757, 3000) + Ulomek(743, 3000)', Ulomek(1, 2)),
                ('Ulomek(1009, 2022) + Ulomek(1013, 2022)', Ulomek(1, 1)),
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
                ('Ulomek(1, 6) - Ulomek(1, 4)', Ulomek(-1, 12)),
                ('Ulomek(1, 4) - Ulomek(1, 6)', Ulomek(1, 12)),
                ('Ulomek(3, 6) - Ulomek(1, 6)', Ulomek(1, 3)),
                ('Ulomek(1, -6) - Ulomek(-1, 4)', Ulomek(1, 12)),
                ('Ulomek(1, 6) - Ulomek(-1, 4)', Ulomek(5, 12)),
                ('Ulomek(1, -6) - Ulomek(1, 4)', Ulomek(-5, 12)),
                ('Ulomek(1, 6) - Ulomek(1, 6)', Ulomek(0, 1)),
                ('Ulomek(1, 6) - Ulomek(-1, 6)', Ulomek(1, 3)),
                ('Ulomek(60, 1) - Ulomek(-1, 60)', Ulomek(3601, 60)),
                ('Ulomek(1, 2014) - Ulomek(1, 2015)', Ulomek(1, 4058210)),
                ('Ulomek(1, 2014) - Ulomek(1, -2015)', Ulomek(4029, 4058210)),
                ('Ulomek(757, 3000) - Ulomek(743, 3000)', Ulomek(7, 1500)),
                ('Ulomek(2003, 1980) - Ulomek(1013, 1980)', Ulomek(1, 2)),
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
                ('Ulomek(1, 3) * Ulomek(1, 2)', Ulomek(1, 6)),
                ('Ulomek(1, 6) * Ulomek(1, 4)', Ulomek(1, 24)),
                ('Ulomek(4, 9) * Ulomek(3, 2)', Ulomek(2, 3)),
                ('Ulomek(1, -6) * Ulomek(-1, 4)', Ulomek(1, 24)),
                ('Ulomek(1, 6) * Ulomek(-1, 4)', Ulomek(-1, 24)),
                ('Ulomek(1, -6) * Ulomek(1, 4)', Ulomek(-1, 24)),
                ('Ulomek(757, 3000) * Ulomek(743, 3000)', Ulomek(562451, 9000000)),
                ('Ulomek(60, 1) * Ulomek(-1, 60)', Ulomek(-1, 1)),
                ('Ulomek(25857, 160930) * Ulomek(277970, 33813)', Ulomek(247, 187)),
                ('Ulomek(25857, 1) * Ulomek(277970, 1)', Ulomek(7187470290, 1)),
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
                ('Ulomek(1, 6) / Ulomek(1, 4)', Ulomek(2, 3)),
                ('Ulomek(4, 9) / Ulomek(2, 3)', Ulomek(2, 3)),
                ('Ulomek(1, -6) / Ulomek(-1, 4)', Ulomek(2, 3)),
                ('Ulomek(1, 6) / Ulomek(-1, 4)', Ulomek(-2, 3)),
                ('Ulomek(1, -6) / Ulomek(1, 4)', Ulomek(-2, 3)),
                ('Ulomek(757, 3000) / Ulomek(743, 3000)', Ulomek(757, 743)),
                ('Ulomek(757, 3000) / Ulomek(3000, 743)', Ulomek(562451, 9000000)),
                ('Ulomek(60, 1) / Ulomek(-60, 1)', Ulomek(-1, 1)),
                ('Ulomek(160930, 25857) / Ulomek(277970, 33813)', Ulomek(187, 247)),
                ('Ulomek(25857, 1) / Ulomek(277970, 1)', Ulomek(25857, 277970)),
                ('Ulomek(25857, 1) / Ulomek(1, 277970)', Ulomek(7187470290, 1)),
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
                ('priblizek(3)', Ulomek(8, 3)),
                ('priblizek(1)', Ulomek(2, 1)),
                ('priblizek(0)', Ulomek(1, 1)),
                ('priblizek(5)', Ulomek(163, 60)),
                ('priblizek(10)', Ulomek(9864101, 3628800)),
                ('priblizek(20)', Ulomek(6613313319248080001, 2432902008176640000)),
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
