# =============================================================================
# Praštevila in racionalna števila
# =====================================================================@001936=
# 1. podnaloga
# Sestavite (neskončen) generator `prastevila(n)`, ki bo kot argument
# dobil naravno število `n` in vračal praštevila, začenši z najmanjšim
# praštevilom, ki je strogo večje od `n`.
# 
#     >>> g = prastevila(1)
#     >>> [next(g) for g in range(10)]
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#     >>> g = prastevila(2013)
#     >>> [next(g) for g in range(5)]
#     [2017, 2027, 2029, 2039, 2053]
# =============================================================================
def je_prastevilo(n):
    if n==1:
        return False
    for i in range(2,int(n**(1/2)+1)):
        if n%i==0:
            return False
    return True
def prastevila(n):
    while True:
        n+=1
        if je_prastevilo(n):
            yield n
# =====================================================================@001937=
# 2. podnaloga
# Sestavili bomo generator `pozitivna_racionalna()`, ki bo vračal
# pozitivna racionalna števila.
# 
# Mislimo si neskončno matriko, ki ima v $i$-ti vrstici in $j$-tem stolpcu
# ulomek $\frac{j}{i}$:
# 
# $\begin{pmatrix}
# \frac{1}{1} & \frac{2}{1} & \frac{3}{1} & \frac{4}{1} & \frac{5}{1} & \dots \\ 
# \frac{1}{2} & \frac{2}{2} & \frac{3}{2} & \frac{4}{2} & \frac{5}{2} & \dots \\ 
# \frac{1}{3} & \frac{2}{3} & \frac{3}{3} & \frac{4}{3} & \frac{5}{3} & \dots \\ 
# \frac{1}{4} & \frac{2}{4} & \frac{3}{4} & \frac{4}{4} & \frac{5}{4} & \dots \\
# \frac{1}{5} & \frac{2}{5} & \frac{3}{5} & \frac{4}{5} & \frac{5}{5} & \dots \\    
# \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\ 
# \end{pmatrix}$
# 
# V takšni neskončni matriki se nahajajo vsa pozitivna racionalna števila.
# Torej se moramo na nek _primeren način_ sprehoditi po elementih te matrike,
# pri čemer pa moramo biti pazljivi, saj se vsako racionalno število v takšni
# matriki pojavlja znova in znova. Na primer ulomki
# 
# $\frac{1}{3}, \frac{2}{6}, \frac{3}{9}, \frac{4}{12}, \ldots$
# 
# vsi predstavljajo isto racionalno število. Med vse temi ulomki pa je
# natanko en _okrajšan_ ulomek. Če se torej sprehodimo po vseh ulomkih v
# tej matriki in ignoriramo tiste, ki niso okrajšani, bomo vsako pozitivno
# racionalno število obiskali natanko enkrat.
# 
# Kako pa naj se na _primeren način_ sprehodimo po tej matriki? Če bi
# šli po prvi vrstici, bi obiskali samo naravna števila. Do ostalih ne
# bi nikoli prišli, saj je že naravnih števil neskončno. Če pa gremo po
# diagonalah, potem vsako število slej ko prej pride na vrsto. _Primeren_
# vrstni red je torej:
# 
# $\frac{1}{1}, \frac{2}{1}, \frac{1}{2}, \frac{3}{1}, \frac{2}{2}, \frac{1}{3},
# \frac{4}{1}, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \ldots$
# 
# Sestavite generator `pozitivna_racionalna()`, ki bo vračal pare števcev in
# imenovalcev pozitivnih racionalnih števil. Vrstni red teh števil naj bo tak,
# kot je opisano zgoraj. Zgled:
# 
#     >>> g = pozitivna_racionalna()
#     >>> [next(g) for i in range(10)]
#     [(1, 1), (2, 1), (1, 2), (3, 1), (1, 3), (4, 1), (3, 2), (2, 3), (1, 4), (5, 1)]
# =============================================================================
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd (n, m%n)
def pozitivna_racionalna():
    vsota = 2
    yield (1,1)
    while True:
        vsota += 1
        j= vsota -1
        i = 1
        while j > 0:
            if gcd(j,i) == 1 :
                yield (j,i)
                j-=1
                i+=1
            else:
                j-=1
                i+=1
                
# =====================================================================@001938=
# 3. podnaloga
# Zdaj pa sestavite še generator `racionalna_stevila()`, bo vračal
# racionalna števila.
# 
# Najprej naj vrne število 0, potem pa vsa racionalna števila v enakem
# vrstnem redu kot pri prejšnji podnalogi, pri čemer naj najprej vrne
# pozitivno število, potem pa še ustrezno negativno število. Zgled:
# 
#     >>> g = racionalna_stevila()
#     >>> [next(g) for i in range(10)]
#     [(0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1),
#      (1, 2), (-1, 2), (3, 1), (-3, 1), (1, 3)]
# =============================================================================

def racionalna_stevila():
    vsota = 2
    yield (0,1)
    yield (1,1)
    yield (-1,1)
    while True:
        vsota += 1
        j= vsota -1
        i = 1
        while j > 0:
            if gcd(j,i) == 1 :
                yield (j,i)
                yield (-j,i)
                j-=1
                i+=1
            else:
                j-=1
                i+=1


































































































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
            testCases = [("prastevila(1)", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113], {'further_iter': 100}),
                         ("prastevila(2)", [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113], {'further_iter': 200}),
                         ("prastevila(2013)", [2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251], {'further_iter': 50}),
                         ("prastevila(1000000)", [1000003, 1000033, 1000037, 1000039, 1000081, 1000099, 1000117, 1000121, 1000133, 1000151, 1000159, 1000171, 1000183, 1000187, 1000193, 1000199, 1000211, 1000213, 1000231, 1000249, 1000253, 1000273, 1000289, 1000291, 1000303, 1000313, 1000333, 1000357, 1000367, 1000381], {'further_iter': 20})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.generator("pozitivna_racionalna()", [
                (1, 1), (2, 1), (1, 2), (3, 1), (1, 3),
                (4, 1), (3, 2), (2, 3), (1, 4), (5, 1),
                (1, 5), (6, 1), (5, 2), (4, 3), (3, 4),
                (2, 5), (1, 6), (7, 1), (5, 3), (3, 5),
                (1, 7), (8, 1), (7, 2), (5, 4), (4, 5),
                (2, 7), (1, 8), (9, 1), (7, 3), (3, 7),
                (1, 9), (10, 1), (9, 2), (8, 3), (7, 4),
                (6, 5), (5, 6), (4, 7), (3, 8), (2, 9),
                (1, 10), (11, 1), (7, 5), (5, 7), (1, 11),
                (12, 1), (11, 2), (10, 3), (9, 4), (8, 5),
                (7, 6), (6, 7), (5, 8), (4, 9), (3, 10),
                (2, 11), (1, 12), (13, 1), (11, 3), (9, 5),
                (5, 9), (3, 11), (1, 13), (14, 1), (13, 2),
                (11, 4), (8, 7), (7, 8), (4, 11), (2, 13),
                (1, 14), (15, 1), (13, 3), (11, 5), (9, 7),
                (7, 9), (5, 11), (3, 13), (1, 15), (16, 1),
                (15, 2), (14, 3), (13, 4), (12, 5), (11, 6),
                (10, 7), (9, 8), (8, 9), (7, 10), (6, 11),
                (5, 12), (4, 13), (3, 14), (2, 15), (1, 16),
                (17, 1), (13, 5), (11, 7), (7, 11), (5, 13)
            ], further_iter=1000)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.generator("racionalna_stevila()", [
                (0, 1), (1, 1), (-1, 1), (2, 1), (-2, 1),
                (1, 2), (-1, 2), (3, 1), (-3, 1), (1, 3),
                (-1, 3), (4, 1), (-4, 1), (3, 2), (-3, 2),
                (2, 3), (-2, 3), (1, 4), (-1, 4), (5, 1),
                (-5, 1), (1, 5), (-1, 5), (6, 1), (-6, 1),
                (5, 2), (-5, 2), (4, 3), (-4, 3), (3, 4),
                (-3, 4), (2, 5), (-2, 5), (1, 6), (-1, 6),
                (7, 1), (-7, 1), (5, 3), (-5, 3), (3, 5),
                (-3, 5), (1, 7), (-1, 7), (8, 1), (-8, 1),
                (7, 2), (-7, 2), (5, 4), (-5, 4), (4, 5),
                (-4, 5), (2, 7), (-2, 7), (1, 8), (-1, 8),
                (9, 1), (-9, 1), (7, 3), (-7, 3), (3, 7),
                (-3, 7), (1, 9), (-1, 9), (10, 1), (-10, 1),
                (9, 2), (-9, 2), (8, 3), (-8, 3), (7, 4),
                (-7, 4), (6, 5), (-6, 5), (5, 6), (-5, 6),
                (4, 7), (-4, 7), (3, 8), (-3, 8), (2, 9),
                (-2, 9), (1, 10), (-1, 10), (11, 1), (-11, 1),
                (7, 5), (-7, 5), (5, 7), (-5, 7), (1, 11),
                (-1, 11), (12, 1), (-12, 1), (11, 2), (-11, 2),
                (10, 3), (-10, 3), (9, 4), (-9, 4), (8, 5)
            ], further_iter=1000)
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
