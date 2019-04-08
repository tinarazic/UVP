# =============================================================================
# Datumi
#
# Koledar, ki ga trenutno uporabljamo v krščanskem (zahodnem) svetu, se
# imenuje [gregorijanski koledar](http://sl.wikipedia.org/wiki/Gregorijanski_koledar).
# Pri tej nalogi bomo implementirali razred `Datum`, ki bo omogočal
# predstavitev datumov v gregorijanskem koledarju in računanje z njimi.
# =====================================================================@001717=
# 1. podnaloga
# Sestavite funkcijo `je_prestopno(leto)`, ki preveri, ali je dano `leto`
# prestopno (po gregorijanskem koledarju). Zgled:
# 
#     >>> je_prestopno(2004)
#     True
#     >>> je_prestopno(1900)
#     False
# =============================================================================
def je_prestopno(leto):
        return leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0
# =====================================================================@001718=
# 2. podnaloga
# Sestavite funkcijo `stevilo_dni(leto)`, ki vrne število dni v danem letu.
# Zgled:
# 
#     >>> stevilo_dni(2015)
#     365
#     >>> stevilo_dni(2016)
#     366
# 
# _Nasvet_: Uporabite funkcijo `je_prestopno`.
# =============================================================================
def stevilo_dni(leto):
    if je_prestopno(leto) == True:
        return 366
    else:
        return 365
# =====================================================================@001719=
# 3. podnaloga
# Sestavite funkcijo `dolzine_mesecev(leto)`, ki vrne seznam dolžine 12,
# ki ima za elemente števila dni po posameznih mesecih v danem letu.
# Zgled:
# 
#     >>> dolzine_mesecev(2015)
#     [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# =============================================================================

# =====================================================================@001720=
# 4. podnaloga
# Definirajte razred `Datum`, s katerim predstavimo datum.
# Najprej sestavite konstruktor `__init__(self, dan, mesec, leto)`.
# Nastali objekt naj ima atribute `dan`, `mesec` in `leto`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d.dan
#     8
#     >>> d.mesec
#     2
#     >>> d.leto
#     1849
# =============================================================================

# =====================================================================@001721=
# 5. podnaloga
# Sestavite metodo `__str__(self)`, ki predstavi datum v obliki
# `'dan. mesec. leto'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> print(d)
#     8. 2. 1849
# =============================================================================

# =====================================================================@001722=
# 6. podnaloga
# Sestavite še metodo `__repr__(self)`, ki vrne niz oblike
# `'Datum(dan, mesec, leto)'`. Zgled:
# 
#     >>> d = Datum(8, 2, 1849)
#     >>> d
#     Datum(8, 2, 1849)
# =============================================================================

# =====================================================================@001723=
# 7. podnaloga
# Sestavite metodo `je_veljaven(self)`, ki preveri, ali je datum
# veljaven. Zgled:
# 
#     >>> d1 = Datum(8, 2, 1849)
#     >>> d1.je_veljaven()
#     True
#     >>> d2 = Datum(5, 14, 2014)
#     >>> d2.je_veljaven()
#     False
# =============================================================================

# =====================================================================@001724=
# 8. podnaloga
# Sestavite metodo `__lt__(self, other)`, ki datum primerja z drugim
# datumom (metoda naj vrne `True`, če je prvi datum manjši, in `False`,
# če ni).
# 
# Ko definirate to metodo, lahko datume primerjate kar z operatorjema
# `<` in `>`. Na primer:
# 
#     >>> Datum(31, 12, 1999) < Datum(1, 1, 2000)
#     True
# =============================================================================

# =====================================================================@001725=
# 9. podnaloga
# Sestavite metodo `__eq__(self, other)`, ki datum primerja z drugim
# datumom (metoda naj vrne `True`, če sta datuma enaka, in `False`,
# če nista).
# 
# Ko definirate to metodo, lahko datume primerjate kar z operatorjema
# `==` in `!=`. Na primer:
# 
#     >>> Datum(31, 12, 1999) != Datum(1, 1, 2000)
#     True
# =============================================================================

# =====================================================================@001726=
# 10. podnaloga
# Sestavite metodo `dan_v_letu(self)`, ki izračuna, koliko dni je minilo
# od začetka leta do danega datuma. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_letu()
#     305
# 
# _Nasvet_: Ali si lahko kako pomagate s funkcijo `dolzine_mesecev`?
# =============================================================================

# =====================================================================@001727=
# 11. podnaloga
# Sestavite metodo `razlika(self, other)`, ki kot argument dobi še en
# objekt razreda `Datum` in vrne število dni med datumoma. Zgled:
# 
#     >>> d1 = Datum(1, 11, 2014)
#     >>> d2 = Datum(14, 10, 2014)
#     >>> d1.razlika(d2)
#     18
# =============================================================================

# =====================================================================@001728=
# 12. podnaloga
# Sestavite metodo `dan_v_tednu(self)`, ki vrne številko dneva v tednu
# (1 = ponedeljek, 2 = torek, …, 7 = nedelja). Lahko si pomagate z
# [Zellerjevim obrazcem](http://en.wikipedia.org/wiki/Zeller's_congruence).
# Druga možnost je, da izračunate razliko med datumom `self` in nekim
# fiksnim datumom, za katerega že poznate dan v tednu. Zgled:
# 
#     >>> d = Datum(1, 11, 2014)
#     >>> d.dan_v_tednu()
#     6
# =============================================================================

# =====================================================================@001729=
# 13. podnaloga
# Sestavite metodo `teden_v_letu(self)`, ki vrne številko tedna v letu.
# Nov teden se vedno začne s ponedeljkom. Prvi teden v letu lahko traja
# le en dan (če se začne na nedeljo) ali pa 7 dni (če se začne na
# ponedeljek). Zgled:
# 
#     >>> d = Datum(3, 11, 2014)
#     >>> d.teden_v_letu()
#     45
# =============================================================================

# =====================================================================@001730=
# 14. podnaloga
# Izven razreda `Datum` sestavite še funkcijo `datum(leto, dan)`,
# ki za parametra dobi leto in številko dneva v letu ter sestavi in
# vrne ustrezen datum. Zgled:
# 
#     >>> datum(2014, 305)
#     Datum(1, 11, 2014)
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
                ('je_prestopno(1900)', False),
                ('je_prestopno(2000)', True),
                ('je_prestopno(2004)', True),
                ('je_prestopno(2011)', False),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            for leto in range(1900, 2100):
                Check.secret(je_prestopno(leto), leto)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('stevilo_dni(1900)', 365),
                ('stevilo_dni(2000)', 366),
                ('stevilo_dni(2004)', 366),
                ('stevilo_dni(2011)', 365),
                ('stevilo_dni(2015)', 365),
                ('stevilo_dni(2016)', 366),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            for leto in range(1900, 2100):
                Check.secret(stevilo_dni(leto), leto)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('dolzine_mesecev(1900)', [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                ('dolzine_mesecev(2000)', [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                ('dolzine_mesecev(2004)', [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
                ('dolzine_mesecev(2011)', [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
            for leto in range(1900, 2100, 10):
                Check.secret(dolzine_mesecev(leto), leto)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ('Datum(8, 2, 1849).dan', 8),
                ('Datum(8, 2, 1849).mesec', 2),
                ('Datum(8, 2, 1849).leto', 1849),
                ('Datum(14, 12, 1982).dan', 14),
                ('Datum(14, 12, 1982).mesec', 12),
                ('Datum(14, 12, 1982).leto', 1982),
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
                ('str(Datum(8, 2, 1849))', "8. 2. 1849"),
                ('str(Datum(14, 12, 1982))', "14. 12. 1982"),
                ('str(Datum(21, 12, 2012))', "21. 12. 2012"),
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
                ('repr(Datum(8, 2, 1849))', "Datum(8, 2, 1849)"),
                ('repr(Datum(14, 12, 1982))', "Datum(14, 12, 1982)"),
                ('repr(Datum(21, 12, 2012))', "Datum(21, 12, 2012)"),
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
                ('Datum(8, 2, 1849).je_veljaven()', True),
                ('Datum(5, 14, 2014).je_veljaven()', False),
                ('Datum(14, 12, 1982).je_veljaven()', True),
                ('Datum(31, 4, 2012).je_veljaven()', False),
                ('Datum(5, 13, 2012).je_veljaven()', False),
                ('Datum(29, 2, 2012).je_veljaven()', True),
                ('Datum(29, 2, 2011).je_veljaven()', False),
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
                ('Datum(31, 12, 1999) < Datum(1, 1, 2000)', True),
                ('Datum(31, 12, 1999) > Datum(1, 1, 2000)', False),
                ('Datum(31, 12, 1999) < Datum(31, 12, 1999)', False),
                ('Datum(31, 12, 1999) > Datum(31, 12, 1999)', False),
                ('Datum(31, 3, 1999) < Datum(1, 4, 1999)', True),    
                ('Datum(31, 3, 1999) > Datum(1, 4, 1999)', False),
                ('Datum(12, 7, 2014) > Datum(1, 2, 2015)', False),
                ('Datum(12, 7, 2014) < Datum(1, 2, 2015)', True),
                ('Datum(1, 7, 2014) < Datum(12, 2, 2014)', False),
                ('Datum(1, 7, 2014) > Datum(12, 2, 2014)', True),
                ('Datum(1, 7, 2014) > Datum(12, 7, 2014)', False),
                ('Datum(12, 7, 2014) > Datum(1, 7, 2014)', True),
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
                ('Datum(31, 12, 1999) == Datum(1, 1, 2000)', False),
                ('Datum(31, 12, 1999) == Datum(31, 12, 1999)', True),
                ('Datum(31, 3, 1999) != Datum(1, 4, 1999)', True),
                ('Datum(2, 2, 2014) != Datum(1, 2, 2014)', True),
                ('Datum(2, 2, 2014) == Datum(1, 2, 2014)', False),
                ('Datum(2, 2, 2014) != Datum(2, 1, 2014)', True),
                ('Datum(2, 2, 2014) == Datum(2, 1, 2014)', False),
                ('Datum(2, 2, 2014) != Datum(2, 2, 2015)', True),
                ('Datum(2, 2, 2014) == Datum(2, 2, 2015)', False),
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
                ('Datum(1, 11, 2014).dan_v_letu()', 305),
                ('Datum(28, 2, 2014).dan_v_letu()', 59),
                ('Datum(1, 3, 2014).dan_v_letu()', 60),
                ('Datum(31, 12, 2014).dan_v_letu()', 365),
                ('Datum(28, 2, 2016).dan_v_letu()', 59),
                ('Datum(29, 2, 2016).dan_v_letu()', 60),
                ('Datum(1, 3, 2016).dan_v_letu()', 61),
                ('Datum(31, 12, 2016).dan_v_letu()', 366),
                ('Datum(1, 1, 2016).dan_v_letu()', 1),
                ('Datum(14, 12, 1982).dan_v_letu()', 348),
                ('Datum(31, 3, 2012).dan_v_letu()', 91),
                ('Datum(31, 3, 2011).dan_v_letu()', 90),
                ('Datum(1, 1, 2011).dan_v_letu()', 1),
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
                ('Datum(1, 11, 2014).razlika(Datum(14, 10, 2014))', 18),
                ('Datum(14, 12, 1990).razlika(Datum(14, 12, 1982))', 2922),
                ('Datum(31, 3, 2012).razlika(Datum(1, 4, 2011))', 365),
                ('Datum(25, 6, 1991).razlika(Datum(10, 11, 2011))', -7443),
                ('Datum(8, 2, 1849).razlika(Datum(3, 12, 1800))', 17599),
                ('Datum(21, 1, 1994).razlika(Datum(17, 12, 2015))', -8000),
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
                ('Datum(14, 12, 1982).dan_v_tednu()', 2),
                ('Datum(1, 1, 1982).dan_v_tednu()', 5),
                ('Datum(1, 2, 1982).dan_v_tednu()', 1),
                ('Datum(1, 3, 1982).dan_v_tednu()', 1),
                ('Datum(1, 4, 1982).dan_v_tednu()', 4),
                ('Datum(1, 5, 1982).dan_v_tednu()', 6),
                ('Datum(1, 6, 1982).dan_v_tednu()', 2),
                ('Datum(1, 7, 1982).dan_v_tednu()', 4),
                ('Datum(1, 8, 1982).dan_v_tednu()', 7),
                ('Datum(1, 9, 1982).dan_v_tednu()', 3),
                ('Datum(1, 10, 1982).dan_v_tednu()', 5),
                ('Datum(1, 11, 1982).dan_v_tednu()', 1),
                ('Datum(1, 12, 1982).dan_v_tednu()', 3),
                ('Datum(10, 11, 2011).dan_v_tednu()', 4),
                ('Datum(9, 3, 1981).dan_v_tednu()', 1),
                ('Datum(1, 11, 2014).dan_v_tednu()', 6),
                ('Datum(2, 11, 2014).dan_v_tednu()', 7),
                ('Datum(3, 11, 2014).dan_v_tednu()', 1),
                ('Datum(4, 11, 2014).dan_v_tednu()', 2),
                ('Datum(5, 11, 2014).dan_v_tednu()', 3),
                ('Datum(6, 11, 2014).dan_v_tednu()', 4),
                ('Datum(7, 11, 2014).dan_v_tednu()', 5),
                ('Datum(29, 2, 2024).dan_v_tednu()', 4),
                ('Datum(1, 3, 2024).dan_v_tednu()', 5),
                ('Datum(2, 3, 2024).dan_v_tednu()', 6),
                ('Datum(3, 3, 2024).dan_v_tednu()', 7),
                ('Datum(4, 3, 2024).dan_v_tednu()', 1),
                ('Datum(5, 3, 2024).dan_v_tednu()', 2),
                ('Datum(6, 3, 2024).dan_v_tednu()', 3),
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
                ('Datum(14, 12, 1982).teden_v_letu()', 51),
                ('Datum(3, 11, 2014).teden_v_letu()', 45),
                ('Datum(1, 1, 2011).teden_v_letu()', 1),
                ('Datum(2, 1, 2011).teden_v_letu()', 1),
                ('Datum(3, 1, 2011).teden_v_letu()', 2),
                ('Datum(1, 1, 2024).teden_v_letu()', 1),
                ('Datum(2, 1, 2024).teden_v_letu()', 1),
                ('Datum(3, 1, 2024).teden_v_letu()', 1),
                ('Datum(4, 1, 2024).teden_v_letu()', 1),
                ('Datum(5, 1, 2024).teden_v_letu()', 1),
                ('Datum(6, 1, 2024).teden_v_letu()', 1),
                ('Datum(7, 1, 2024).teden_v_letu()', 1),
                ('Datum(8, 1, 2024).teden_v_letu()', 2),
                ('Datum(14, 1, 2024).teden_v_letu()', 2),
                ('Datum(15, 1, 2024).teden_v_letu()', 3),
                ('Datum(21, 1, 2024).teden_v_letu()', 3),
                ('Datum(22, 1, 2024).teden_v_letu()', 4),
                ('Datum(1, 1, 2014).teden_v_letu()', 1),
                ('Datum(2, 1, 2014).teden_v_letu()', 1),
                ('Datum(4, 1, 2014).teden_v_letu()', 1),
                ('Datum(5, 1, 2014).teden_v_letu()', 1),
                ('Datum(6, 1, 2014).teden_v_letu()', 2),
                ('Datum(12, 1, 2014).teden_v_letu()', 2),
                ('Datum(13, 1, 2014).teden_v_letu()', 3),
                ('Datum(19, 1, 2014).teden_v_letu()', 3),
                ('Datum(28, 12, 2014).teden_v_letu()', 52),
                ('Datum(29, 12, 2014).teden_v_letu()', 53),
                ('Datum(31, 12, 2014).teden_v_letu()', 53),
                ('Datum(6, 6, 2014).teden_v_letu()', 23),
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
                ('datum(2014, 305)', Datum(1, 11, 2014)),
                ('datum(2011, 1)', Datum(1, 1, 2011)),
                ('datum(2012, 12)', Datum(12, 1, 2012)),
                ('datum(2013, 123)', Datum(3, 5, 2013)),
                ('datum(2014, 365)', Datum(31, 12, 2014)),
                ('datum(2016, 366)', Datum(31, 12, 2016)),
                ('datum(2016, 60)', Datum(29, 2, 2016)),
                ('datum(2015, 60)', Datum(1, 3, 2015)),
                ('datum(2015, 90)', Datum(31, 3, 2015)),
                ('datum(2015, 91)', Datum(1, 4, 2015)),
                ('datum(2015, 92)', Datum(2, 4, 2015)),
                ('datum(2015, 120)', Datum(30, 4, 2015)),
                ('datum(2015, 121)', Datum(1, 5, 2015)),
                ('datum(2015, 304)', Datum(31, 10, 2015)),
                ('datum(2015, 305)', Datum(1, 11, 2015)),
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
