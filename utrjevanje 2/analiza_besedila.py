# =============================================================================
# Analiza besedila
#
# Pri tej nalogi bomo analizirali nize, ki predstavljajo pravilno slovensko
# oblikovane besede in stavke. Pri vseh podnaloge lahko predpostavite, da
# so vhodni nizi `s` dobro oblikovani, tj. ne vsebujejo dveh zaporednih
# presledkov oz. nepotrebnih presledkov ter prelomov vrstice na začetku ali
# na koncu.
# =====================================================================@001485=
# 1. podnaloga
# Sestavite funkcijo `stevilo_besed(s)`, ki v podanem nizu prešteje
# število besed, pri čemer lahko predpostavite, da presledki stojijo
# **natanko pred vsako** (razen prvo) besedo v nizu. Primer:
# 
#     >>> stevilo_besed('Višje, hitreje, močneje!')
#     3
# =============================================================================

# =====================================================================@001486=
# 2. podnaloga
# Sestavite funkcijo `samoglasniki(s)`, ki v podanem nizu `s` prešteje
# število samoglasnikov. Zgled:
# 
#     >>> samoglasniki('pomaranča')
#     4
# =============================================================================

# =====================================================================@001487=
# 3. podnaloga
# V Pythonu vrstice večvrstičnega niza ločujemo z znakom `'\n'`.
# Sestavite funkcijo `vrstice(s)`, ki sprejme večvrstični niz `s` in
# vrne seznam, ki vsebuje vse vrstice tega niza (v istem vrstnem redu).
# Zgled:
# 
#     >>> vrstice("Danes\n je lep\ndan.\n")
#     ['Danes', ' je lep', 'dan.', '']
# 
# _Opomba_: Python obravnava niz `'\n'` kot en sam znak.
# =============================================================================

# =====================================================================@001488=
# 4. podnaloga
# Haiku (japonsko 俳句) je japonska pesniška oblika iz treh verzov
# (vrstic), ki obsega sedemnajst zlogov. Prvi in tretji verz imata po pet
# zlogov, drugi sedem.
# 
# Na kulturnem natečaju TomoHaiku udeleženci oddajajo svoje izdelke na
# strežnik Tomo. Napišite kontrolno funkcijo `haiku(s)`, ki sprejme
# niz `s`, ter vrne `True`, če niz ustreza pesniški obliki haiku, sicer
# pa vrne `False`.
# 
# Predpostavite lahko, da število samoglasnikov v neki besedi ustreza
# številu njenih zlogov, ter da niz `s` ne vsebuje nepotrebnih začetnih oz.
# končnih praznih vrstic. Vrstice so ločene z znakom za prelom vrstice `'\n'`.
# Primer:
# 
#     >>> haiku('Skrit v svojem svetu,\ntemna otožnost neba,\ntvoj topli objem.')
#     True
#     >>> haiku('Riba,\nraca, rak,\nvinjak je grenak!')
#     False
# =============================================================================

# =====================================================================@001489=
# 5. podnaloga
# Sestavite funkcijo `podcrtaj(s)`, ki za parameter dobi niz `s`, v
# katerem so podnizi, ki bi morali biti izpisani podčrtano, označeni s
# podčrtajem na začetku in na koncu. Če je v nizu liho mnogo podčrtajev,
# si mislite, da je še eden na koncu. Funkcija naj vrne dvovrstični niz,
# kjer je v prvi vrstici originalni niz `s` toda brez podčrtajev, sledi
# znak za prelom vrstice, naslednjo vrstico pa sestavlja niz, sestavljen
# iz presledkov in minusov, pri čemer minusi ležijo pod tistimi deli
# besedila, ki morajo biti podčrtani. Primer:
# 
#     >>> podcrtaj("Jaz _sem_ pa cajzelc!")
#     'Jaz sem pa cajzelc!\n    ---            '
# 
# Predpostavite, da v nizu `s` ni nobenega znaka `'\n'`.
# =============================================================================

# =====================================================================@001490=
# 6. podnaloga
# Sestavite funkcijo `stevilo_znakov(s)`, ki v podanem nizu `s` prešteje
# število znakov, pri čemer se presledki ne upoštevajo. Zgled:
# 
#     >>> stevilo_znakov('B     u!')
#     3
# =============================================================================

# =====================================================================@001491=
# 7. podnaloga
# [Sonet](https://sl.wikipedia.org/wiki/Sonet) je priljubljena pesniška oblika.
# Sestavljen je iz štirih kitic,
# pri čemur med vsakima dvema kiticama avtor izpusti eno prazno vrstico.
# Prvi dve kitici sta štirivrstični — kvartini, drugi dve pa sta trivrstični
# — tercini.
# 
# V slovenskem sonetu je standardni verz italijanski (laški) ali jambski
# enajsterec. To pomeni, da v vsaki vrstici nastopa natanko enajst zlogov.
# 
# Na kulturnem natečaju TomoSonet udeleženci oddajajo svoje izdelke na
# strežnik Tomo. Napiši kontrolno funkcijo `sonet(s)`, ki sprejme niz
# `s`, ter vrne `True`, če niz ustreza slovenskemu sonetu, in `False` sicer.
# Zgled:
# 
#     >>> sonet('Bolj slab\nsonet.\n\nZa umret!')
#     False
# 
# _Namig_: V slovenskem jeziku število samoglasnikov v neki besedi ustreza
# številu njenih zlogov. (Obstaja nekaj izjem, ki pa jih bomo zanemarili.)
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
            Check.equal("""stevilo_besed("Višje, hitreje, močneje!")""", 3)
            Check.equal("""stevilo_besed("Bu!")""", 1)
            Check.equal("""stevilo_besed("Matej ima tri hruške.")""", 4)
            Check.equal("""stevilo_besed("Eno ima za Alenko.")""", 4)
            Check.equal("""stevilo_besed("")""", 0)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal("""samoglasniki("Višje, hitreje, močneje")""", 8)
            Check.equal("""samoglasniki("Bu!")""", 1)
            Check.equal("""samoglasniki("krst")""", 0)
            Check.equal("""samoglasniki("Matej ima tri hruške.")""", 7)
            Check.equal("""samoglasniki("Eno ima za Alenko.")""", 8)
            test_data = [
                ("""samoglasniki('pomaranča')""", 4),
                ("""samoglasniki('Tu je 7 samoglasnikov!')""", 7),
                ("""samoglasniki('Buci-buc!')""", 3),
                ("""samoglasniki('Mateja ima štiri hruške!')""", 9),
                ("""samoglasniki('Aaaaaaaa')""", 8),
                ("""samoglasniki('smrt')""", 0),
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
                ('vrstice("Danes\\n je lep\\ndan.\\n")', ["Danes", " je lep", "dan.", ""]),
                ('vrstice("Danes je lep dan.")', ["Danes je lep dan."]),
                ('vrstice("\\nDanes je lep dan.\\n")', ["", "Danes je lep dan.", ""]),
            ]
            for td in test_data:
                if not Check.equal(*td):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal("""haiku("Bu!")""", False)
            Check.equal("""haiku('Srečna ljubezen\\nje kot svobodna ptica,\\nki je vesela.')""", True)
            Check.equal("""haiku('Skrit v svojem svetu,\\ntemna otožnost neba,\\ntvoj topli objem.')""", True)
            Check.equal("""haiku('Riba,\\nraca, rak,\\nvinjak je grenak!')""", False)
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            Check.equal("""podcrtaj("Jaz _sem_ pa cajzelc!")""", 'Jaz sem pa cajzelc!\n    ---            ')
            Check.equal("""podcrtaj("_Podčrtajmo_ povedek!")""", 'Podčrtajmo povedek!\n----------         ')
            Check.equal("""podcrtaj("Zdaj _pa_ predlog!")""", 'Zdaj pa predlog!\n     --         ')
            Check.equal("""podcrtaj("_Zdaj pa vse!")""", 'Zdaj pa vse!\n------------')
            Check.equal("""podcrtaj("__")""", '\n')
            Check.equal("""podcrtaj("_a_")""", 'a\n-')
            Check.equal("""podcrtaj("Nič")""", 'Nič\n   ')
            Check.equal("""podcrtaj("__AAA__")""", 'AAA\n   ')
            Check.equal("""podcrtaj("A__A")""", 'AA\n  ')
            Check.equal("""podcrtaj("_T__X_")""", 'TX\n--')
            Check.equal("""podcrtaj("__T__X_")""", 'TX\n  ')
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            test_data = [
                ("""stevilo_znakov('Višje, hitreje, močneje!')""", 22),
                ("""stevilo_znakov('Bu!')""", 3),
                ("""stevilo_znakov('Matej ima tri hruške!')""", 18),
                ("""stevilo_znakov('Eno ima za Alenko.')""", 15),
                ("""stevilo_znakov('   ')""", 0),
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
                ("sonet(\"Poet tvoj nov Slovencam venec vije,\\n'z petnajst sonetov ti tako ga spleta,\\nde 'magistrale', pesem trikrat peta,\\nvseh drugih skupej veže harmonije.\\n\\nIz njega zvira, vanjga se spet zlije\\npo versti pesem vsacega soneta;\\nprihodnja v prednje koncu je začeta;\\nenak je pevec vencu poezije:\\n\\nvse misli zvirajo 'z ljubezni ene,\\nin kjer ponoči v spanji so zastale,\\nzbude se, ko spet zarja noč prežene.\\n\\nTi si življenja moj'ga magistrale,\\nglasil se 'z njega, ko ne bo več mene,\\nran mojih bo spomin in tvoje hvale.\")", True),
                ("sonet(\"Bolj slab\\nsonet.\\n\\nZa umret!\")", False),
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
