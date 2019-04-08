# =============================================================================
# Kalorije
#
# Tina si za vsak obrok, ki ga poje, zapiše njegovo kalorično vrednost
# (celo število). Vse te podatke hrani v datoteki. Za vsak dan ima v
# datoteki po eno vrstico. Znotraj iste vrstice so števila ločena z vejicami,
# kot prikazuje zgled:
# 
#     550,745,625,200
#     850,1250
#     40,650,743
# =====================================================================@001514=
# 1. podnaloga
# Sestavite funkcijo `vrni_kalorije(niz)`, ki dobi seznam kalorij, podan
# kot niz, v katerem so števila ločena z vejicami, in jih vrne kot seznam
# celih števil.
# 
#     >>> vrni_kalorije('10,4,7')
#     [10, 4, 7]
# =============================================================================
def vrni_kalorije(niz):
    kalorije=[]
    nov=niz.split(',')
    for stevilo in nov:
        kalorije.append(int(stevilo))
    return kalorije
# =====================================================================@001515=
# 2. podnaloga
# Sestavite funkcijo `kalorije_na_dan(ime_datoteke)`, ki kot parameter
# dobi ime vhodne datoteke. Vhodna datoteka je take oblike, kot je opisano
# zgoraj. Funkcija naj za vsak dan izračuna, koliko kalorij je Tina zaužila.
# Rezultat naj vrne v obliki seznama števil. Primer (denimo, da so podatki
# iz zgleda shranjeni v datoteki z imenom tina_kalorije.txt):
# 
#     >>> kalorije_na_dan('tina_kalorije.txt')
#     [2120, 2100, 1433]
# 
# Torej, za vsako vrstico v datoteki (ki predstavlja en dan) dodaj v seznam
# eno število, ki naj bo enako vsoti kalorij za tisti dan.
# =============================================================================
def kalorije_na_dan(ime_datoteke):
    sez=[]
    for vrstica in open(ime_datoteke):
        kalorije=vrni_kalorije(vrstica.strip())
        sez.append(sum(kalorije))
    return sez
# =====================================================================@001516=
# 3. podnaloga
# Sestavite funkcijo `vsota_kalorij(ime_vhodne, ime_izhodne)`, ki kot
# argumenta dobi imeni dveh datotek. Vhodna datoteka vsebuje Tinine zapiske.
# Na izhodno datoteko naj za vsako vrstico v vhodni datoteki zapiše vsoto
# kaloričnih vrednosti zaužite hrane tistega dne. Vsako število v izhodni
# datoteki naj bo v svoji vrstici.
# 
# Po klicu funkcije `vsota_kalorij('tina_kalorije.txt', 'tina_vsote.txt')`
# pri enakih podatkih kot zgoraj, bo v datoteki tina_vsote.txt naslednja
# vsebina:
# 
#     2120
#     2100
#     1433
# =============================================================================

# =====================================================================@001517=
# 4. podnaloga
# Sestavite funkcijo `povprecje_kalorij(ime_vhodne, ime_izhodne)`, ki
# kot argumenta dobi imeni dveh datotek (vhodne in izhodne). Na izhodno
# datoteko naj za vsako vrstico na vhodni datoteki zapiše zaporedno številko
# vrstice (vrstice se začno šteti z ena) ter povprečno kalorično vrednost
# obrokov, ki jih je Tina zaužila tisti dan, na dve decimalni mesti.
# 
# V zadnjo (dodatno) vrstico pa naj funkcija zapiše povprečje dnevno
# zaužitih kalorij (prav tako na dve decimalni mesti).
# 
# Po klicu funkcije `povprecje_kalorij('tina_kalorije.txt', 'tina_povprecja.txt')`
# pri enakih podatkih kot zgoraj, bo v datoteki tina_povprecja.txt naslednja
# vsebina:
# 
#     1 530.00
#     2 1050.00
#     3 477.67
#     1884.33
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
            Check.equal('vrni_kalorije("11,23,1")', [11, 23, 1])
            Check.equal('vrni_kalorije("15,50,72,68,2")',[15, 50, 72, 68, 2])
            Check.equal('vrni_kalorije("10")', [10])
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_cases = [
                ("tina_kalorije.txt", ["550,745,625,200", "850,1250", "40,650,743"],  [2120, 2100, 1433]),
                ("kalorije_po_dneh.txt", ["2,35,18,5,78", "13,20", "8", "15,84,2,4,5,16,78,44,21", "10,5,50,40"],  [138, 33, 8, 269, 105]),
            ]
            for f_name, vhod, result in test_cases:
                with Check.in_file(f_name, vhod):
                    if not Check.equal('kalorije_na_dan("{0}")'.format(f_name), result):
                        break # test had failed
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_cases = [
                ("tina_kalorije.txt", ["550,745,625,200", "850,1250", "40,650,743"],  "tina_vsote.txt", ["2120", "2100", "1433"]),
                ("kalorije_po_dneh.txt", ["2,35,18,5,78", "13,20", "8", "15,84,2,4,5,16,78,44,21", "10,5,50,40"],  "skupne_kalorije.txt", ["138", "33", "8", "269", "105"]),
            ]
            napaka = False
            for in_name, vhod, out_name, izhod in test_cases:
                if napaka: break
                with Check.in_file(in_name, vhod):
                    vsota_kalorij(in_name, out_name)
                    if not Check.out_file(out_name, izhod): napaka = True
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_cases = [
                ("tina_kalorije.txt", ["550,745,625,200", "850,1250", "40,650,743"],  "tina_povprecja.txt", ["1 530.00", "2 1050.00", "3 477.67", "1884.33"]),
                ("kalorije_po_dneh.txt", ["2,35,18,5,78", "13,20", "8", "15,84,2,4,5,16,78,44,21", "10,5,50,40"], "povprecne_kalorije.txt", ["1 27.60", "2 16.50", "3 8.00", "4 29.89", "5 26.25", "110.60"]),
            ]
            napaka = False
            for in_name, vhod, out_name, izhod in test_cases:
                if napaka: break
                with Check.in_file(in_name, vhod):
                    povprecje_kalorij(in_name, out_name)
                    if not Check.out_file(out_name, izhod): napaka = True
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
