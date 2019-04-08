# =============================================================================
# Šifriranje
#
# Substitucijska šifra je enostaven način šifriranja, pri katerem vsako
# črko iz dane abecede zamenjamo z neko drugo črko. Tako šifro predstavimo
# s slovarjem, ki ima za ključe vse črke iz abecede, pripadajoče vrednosti
# pa so črke, s katerimi jih zašifriramo.
# 
# Tako slovar `{'A': 'B', 'C': 'C', 'B': 'D', 'D': 'A'}` pomenil, da se
# `A` zašifrira v `B`, `B` v `D`, `D` v `A`, `C` pa se ne spremeni.
# 
# V vseh testnih primerih bomo uporabljali nasednjo substitucijsko šifro:
# 
#     nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
#                   'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
#                   'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
#                   'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
#                   'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
# =====================================================================@001388=
# 1. podnaloga
# Sestavite funkcijo `sifriraj(sifra, beseda)`, ki vrne besedo, zašifrirano
# z dano šifro. Predpostavite lahko, da vse črke v besedi nastopajo v
# šifri.
# =============================================================================
def sifriraj(sifra,beseda):
    niz=''
    for znak in beseda:
        if znak in sifra:
            znak=sifra[znak]
            niz+=znak
    return niz
        
# =====================================================================@001389=
# 2. podnaloga
# Sestavite funkcijo `ali_je_sifra(slovar)`, ki ugotovi, ali `slovar` predstavlja
# šifro, torej ali je bijekcija črk na neki abecedi.
# =============================================================================
def ali_je_sifra(slovar):
    return set(  slovar.keys())==set(slovar.values())
# =====================================================================@001390=
# 3. podnaloga
# Sestavite funkcijo `inverz(sifra)`, ki vrne inverz dane šifre, če ta
# obstaja. V nasprotnem primeru funkcija vrne `None`.
# =============================================================================
def inverz(sifra):
    nov={}
    if ali_je_sifra(sifra)==False:
        return
    for kljuc,vrednost in sifra.items():
        nov[vrednost]=kljuc
    return nov
        
# =====================================================================@001391=
# 4. podnaloga
# Sestavite funkcijo `odsifriraj(sifra, beseda)`, ki sprejme šifro in
# zašifrirano besedilo, vrne pa odšifrirano besedilo. Če slovar
# ni bijekcija (in se torej besedilo ne da nujno odšifrirati), naj
# funkcija vrne `None`.
# =============================================================================
def odsifriraj(sifra,beseda):
    nov=''
    if ali_je_sifra(sifra)==False:
        return
    else:
        for znak in beseda:
            inv = inverz (sifra)
            nov +=inv[znak]
    return nov




































































































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
            nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
                          'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
                          'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
                          'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
                          'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
            Check.equal('sifriraj(nasa_sifra, "KOLOKVIJ")', "IRHRINBA", env={'nasa_sifra': nasa_sifra})
            Check.equal('sifriraj(nasa_sifra, "PESEM")', "JVTVU", env={'nasa_sifra': nasa_sifra})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
                          'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
                          'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
                          'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
                          'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
            Check.equal('ali_je_sifra(nasa_sifra)', True, env={'nasa_sifra': nasa_sifra})
            
            Check.equal("ali_je_sifra({'A': 'B', 'B': 'C', 'C': 'A'})", True)
            Check.equal("ali_je_sifra({'A': 'A', 'B': 'B', 'C': 'C'})", True)
            Check.equal("ali_je_sifra({'A': 'B', 'B': 'B', 'C': 'A'})", False)
            Check.equal("ali_je_sifra({'A': '1', 'B': '2', 'C': '3'})", False)
            Check.equal("ali_je_sifra({'A': 'B'})", False)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
                          'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
                          'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
                          'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
                          'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
            Check.equal("inverz({'A': 'B', 'B': 'C', 'C': 'A'})", {'A': 'C', 'B': 'A', 'C': 'B'})
            Check.equal("inverz({'A': 'B', 'B': 'B', 'C': 'A'})", None)
            Check.equal("inverz({'A': 'B'})", None)
            Check.equal("inverz(nasa_sifra)", {'Č': 'T', 'A': 'J', 'C': 'D', 'B': 'I', 'E': 'F', 'D': 'Ž', 'G': 'U', 'F': 'H', 'I': 'K', 'H': 'L', 'K': 'Č', 'J': 'P', 'M': 'B', 'L': 'R', 'O': 'A', 'N': 'V', 'P': 'G', 'S': 'Š', 'R': 'O', 'U': 'M', 'T': 'S', 'V': 'E', 'Z': 'C', 'Š': 'N', 'Ž': 'Z'}, env={'nasa_sifra': nasa_sifra})
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
                          'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
                          'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
                          'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
                          'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}
            Check.equal('odsifriraj(nasa_sifra, "IRHRINBA")', "KOLOKVIJ", env={'nasa_sifra': nasa_sifra})
            Check.equal('odsifriraj(nasa_sifra, "JVTVU")', "PESEM", env={'nasa_sifra': nasa_sifra})
            Check.equal('odsifriraj({"A": "B"}, "JVTVU")', None)
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
