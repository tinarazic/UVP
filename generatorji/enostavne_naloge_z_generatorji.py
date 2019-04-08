# =============================================================================
# Enostavne naloge z generatorji
# =====================================================================@001930=
# 1. podnaloga
# Napišite generator `stevke(n)`, ki generira števke naravnega števila
# `n` začenši z enicami (s skrajno desno števko).
# 
#     >>> [x for x in stevke(1337)]
#     [7, 3, 3, 1]
# =============================================================================
def stevke(n):
    while n > 0:
        yield n%10
        n=n//10
        
# =====================================================================@001931=
# 2. podnaloga
# Sestavite generator `potence_naravnih(k)`, ki kot argument dobi število
# `k` in generira (neskončno) zaporedje $1^k, 2^k, 3^k, 4^k, \ldots$
# 
#     >>> g = potence_naravnih(2)
#     >>> [next(g) for i in range(10)]
#     [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# =============================================================================
def potence_naravnih(k):
    n=1
    while True:
        yield n**k
        n+=1
# =====================================================================@001932=
# 3. podnaloga
# Sestavite generator `fakultete(n)`, ki kot argument dobi nenegativno
# celo število `n` in generira (neskončno) zaporedje $n!, (n+1)!, (n+2)!, \ldots$
# 
#     >>> g = fakultete(0)
#     >>> [next(g) for i in range(10)]
#     [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
# =============================================================================
def fakulteta(n):
    if n==0:
        return 1
    else:
        return n * fakulteta(n-1)
def fakultete(n):
    while True:
        yield fakulteta(n)
        n+=1
# =====================================================================@001933=
# 4. podnaloga
# Spomnimo se, da je Collatzovo zaporedje z začetnim členom $a_0$ definirano
# s predpisom $a_{i+1} = a_i / 2$, če je $a_i$ sodo, in $a_{i+1} = 3 a_i + 1$ sicer.
# 
# Sestavite generator `collatz(n)`, ki kot argument dobi naravno število `n`
# in generira Collatzovo zaporedje z začetnim členom `n`. Generiranje naj se
# konča, ko pridemo do števila 1.
# 
#     >>> [x for x in collatz(20)]
#     [20, 10, 5, 16, 8, 4, 2, 1]
# =============================================================================
def collatz(n):
    while n > 1:
        yield n
        if n % 2 == 0 :
            n = n // 2
        else:
            n = 3 * n + 1
            
    yield 1        
# =====================================================================@001934=
# 5. podnaloga
# Sestavite generator `delitelji(n)`, ki kot argument dobi naravno število
# `n` in generira njegove delitelje (od najmanjšega proti največjemu).
# 
#     >>> [x for x in delitelji(12)]
#     [1, 2, 3, 4, 6, 12]
# =============================================================================
def delitelji(n):
    for stevilka in range (1, n + 1):
        if n % stevilka == 0:
            yield stevilka
# =====================================================================@001935=
# 6. podnaloga
# Sestavite generator `ucinkoviti_delitelji(n)`, ki deluje tako kot generator
# `delitelji(n)`, vendar poskrbite, da deluje učinkovito, saj bomo njegovo
# delovanje preverili na velikih številih. Najbolje je, da že generator
# `delitelji` napišete učinkovito, nato pa generator `ucinkoviti_delitelji`
# definirate kar kot:
# 
#     ucinkoviti_delitelji = delitelji
# =============================================================================

def ucinkoviti_delitelji(n):
    d = []
    i = 1
    while  i **2 < n:
        if n % i == 0:
            yield i
            d.append(n//i)
        i += 1
    if i ** 2 == n:
        yield i
    while len(d) > 0:
        yield d.pop()
    
    



































































































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
            testCases = [("stevke(8)", [8], {'should_stop': True}),
                         ("stevke(43)", [3, 4], {'should_stop': True}),
                         ("stevke(162)", [2, 6, 1], {'should_stop': True}),
                         ("stevke(1337)", [7, 3, 3, 1], {'should_stop': True}),
                         ("stevke(526481379)", [9, 7, 3, 1, 8, 4, 6, 2, 5], {'should_stop': True})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            testCases = [("potence_naravnih(2)", [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], {'further_iter': 100}),
                         ("potence_naravnih(3)", [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000], {'further_iter': 100}),
                         ("potence_naravnih(-1)", [1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, 0.14285714285714285, 0.125, 0.1111111111111111, 0.1], {'further_iter': 100}),
                         ("potence_naravnih(0.5)", [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795], {'further_iter': 100}),
                         ("potence_naravnih(5)", [1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049, 100000, 161051, 248832, 371293, 537824, 759375, 1048576, 1419857, 1889568, 2476099, 3200000],  {'further_iter': 100})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            testCases = [("fakultete(0)", [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000], {'further_iter': 10}),
                         ("fakultete(1)", [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800], {'further_iter': 10}),
                         ("fakultete(2)", [2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800], {'further_iter': 10}),
                         ("fakultete(20)", [2432902008176640000, 51090942171709440000, 1124000727777607680000, 25852016738884976640000, 620448401733239439360000, 15511210043330985984000000], {'further_iter': 10}),
                         ("fakultete(10)", [3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000], {'further_iter': 500})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            testCases = [("collatz(20)", [20, 10, 5, 16, 8, 4, 2, 1], {'should_stop': True}),
                         ("collatz(1)", [1], {'should_stop': True}),
                         ("collatz(97)", [97, 292, 146, 73, 220, 110, 55, 166, 83, 250, 125, 376, 188, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], {'should_stop': True}),
                         ("collatz(73)", [73, 220, 110, 55, 166, 83, 250, 125, 376, 188, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], {'should_stop': True}),
                         ("collatz(54)", [54, 27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], {'should_stop': True}),
                         ("collatz(871)", [871, 2614, 1307, 3922, 1961, 5884, 2942, 1471, 4414, 2207, 6622, 3311, 9934, 4967, 14902, 7451, 22354, 11177, 33532, 16766, 8383, 25150, 12575, 37726, 18863, 56590, 28295, 84886, 42443, 127330, 63665, 190996, 95498, 47749, 143248, 71624, 35812, 17906, 8953, 26860, 13430, 6715, 20146, 10073, 30220, 15110, 7555, 22666, 11333, 34000, 17000, 8500, 4250, 2125, 6376, 3188, 1594, 797, 2392, 1196, 598, 299, 898, 449, 1348, 674, 337, 1012, 506, 253, 760, 380, 190, 95, 286, 143, 430, 215, 646, 323, 970, 485, 1456, 728, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
            , {'should_stop': True}),
                         ("collatz(937)", [937, 2812, 1406, 703, 2110, 1055, 3166, 1583, 4750, 2375, 7126, 3563, 10690, 5345, 16036, 8018, 4009, 12028, 6014, 3007, 9022, 4511, 13534, 6767, 20302, 10151, 30454, 15227, 45682, 22841, 68524, 34262, 17131, 51394, 25697, 77092, 38546, 19273, 57820, 28910, 14455, 43366, 21683, 65050, 32525, 97576, 48788, 24394, 12197, 36592, 18296, 9148, 4574, 2287, 6862, 3431, 10294, 5147, 15442, 7721, 23164, 11582, 5791, 17374, 8687, 26062, 13031, 39094, 19547, 58642, 29321, 87964, 43982, 21991, 65974, 32987, 98962, 49481, 148444, 74222, 37111, 111334, 55667, 167002, 83501, 250504, 125252, 62626, 31313, 93940, 46970, 23485, 70456, 35228, 17614, 8807, 26422, 13211, 39634, 19817, 59452, 29726, 14863, 44590, 22295, 66886, 33443, 100330, 50165, 150496, 75248, 37624, 18812, 9406, 4703, 14110, 7055, 21166, 10583, 31750, 15875, 47626, 23813, 71440, 35720, 17860, 8930, 4465, 13396, 6698, 3349, 10048, 5024, 2512, 1256, 628, 314, 157, 472, 236, 118, 59, 178, 89, 268, 134, 67, 202, 101, 304, 152, 76, 
            38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], {'should_stop': True}),
                         ("collatz(1125899906842624)", [1125899906842624, 562949953421312, 281474976710656, 140737488355328, 70368744177664, 35184372088832, 17592186044416, 8796093022208, 4398046511104, 2199023255552, 1099511627776, 549755813888, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1], {'should_stop': True})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            testCases = [("delitelji(7)", [1, 7], {'should_stop': True}),
                         ("delitelji(12)", [1, 2, 3, 4, 6, 12], {'should_stop': True}),
                         ("delitelji(25)", [1, 5, 25], {'should_stop': True}),
                         ("delitelji(60)", [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60], {'should_stop': True}),
                         ("delitelji(1001)", [1, 7, 11, 13, 77, 91, 143, 1001], {'should_stop': True}),
                         ("delitelji(2017)", [1, 2017], {'should_stop': True})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        try:
            testCases = [("ucinkoviti_delitelji(7)", [1, 7], {'should_stop': True}),
                         ("ucinkoviti_delitelji(12)", [1, 2, 3, 4, 6, 12], {'should_stop': True}),
                         ("ucinkoviti_delitelji(25)", [1, 5, 25], {'should_stop': True}),
                         ("ucinkoviti_delitelji(60)", [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60], {'should_stop': True}),
                         ("ucinkoviti_delitelji(1001)", [1, 7, 11, 13, 77, 91, 143, 1001], {'should_stop': True}),
                         ("ucinkoviti_delitelji(2017)", [1, 2017], {'should_stop': True}),
                         ("ucinkoviti_delitelji(244140625)", [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625], {'should_stop': True}),
                         ("ucinkoviti_delitelji(1220703125)", [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125], {'should_stop': True}),
                         ("ucinkoviti_delitelji(1555200)", [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 256, 270, 288, 300, 320, 324, 360, 384, 400, 405, 432, 450, 480, 486, 540, 576, 600, 640, 648, 675, 720, 768, 800, 810, 864, 900, 960, 972, 1080, 1152, 1200, 1215, 1280, 1296, 1350, 1440, 1600, 1620, 1728, 1800, 1920, 1944, 2025, 2160, 2304, 2400, 2430, 2592, 2700, 2880, 3200, 3240, 3456, 3600, 3840, 3888, 4050, 4320, 4800, 4860, 5184, 5400, 5760, 6075, 6400, 6480, 6912, 7200, 7776, 8100, 8640, 9600, 9720, 10368, 10800, 11520, 12150, 12960, 14400, 15552, 16200, 17280, 19200, 19440, 20736, 21600, 24300, 25920, 28800, 31104, 32400, 34560, 38880, 43200, 48600, 51840, 57600, 62208, 64800, 77760, 86400, 97200, 103680, 129600, 155520, 172800, 194400, 259200, 311040, 388800, 518400, 777600, 1555200], {'should_stop': True}),
                         ("ucinkoviti_delitelji(1220703131)", [1, 1220703131], {'should_stop': True})]
            for example, correct, options in testCases:
                if not Check.generator(example, correct, **options):
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
