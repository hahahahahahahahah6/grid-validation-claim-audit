import tempfile
import contextlib
import io
from grid_validation_claim_audit.audit import main
import unittest
from pathlib import Path
from grid_validation_claim_audit.audit import audit, claims, evidence
from grid_validation_claim_audit.phrases import GRIDVALIDATION, NOGRIDVALIDATION, GENERIC_NAMES


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(set(GRIDVALIDATION)), len(set(NOGRIDVALIDATION)), len(set(GENERIC_NAMES))), (50, 24, 24))
        for phrase in GRIDVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOGRIDVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate grid\n```'), (False, False))
        self.assertEqual(claims('~~~ text\nvalidate grid\n~~~'), (False, False))
        self.assertEqual(claims('`validate-grid`'), (True, False))
        self.assertEqual(claims("doesn't validate grid"), (False, True))
        self.assertEqual(claims('validate gridiron'), (False, False))

    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for prefix, call in [('import stdnum.grid', 'stdnum.grid.' + method), ('import stdnum.grid as im', 'im.' + method), ('from stdnum import grid', 'grid.' + method), ('import stdnum', 'stdnum.grid.' + method), ('from stdnum.grid import ' + method, method), ('from stdnum.grid import ' + method + ' as v', 'v')]:
                with self.subTest(method=method, call=call): self.assertTrue(evidence(prefix + '\n' + call + '(x)'))

    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            for source in ('obj.' + name + '(x)', 'from lib import ' + name + ' as f\nf(x)', 'obj = factory()\nobj.' + name + '(x)'):
                with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_not_evidence(self):
        cases = ['import stdnum.grid', 'validate(x)', 'is_valid(x)', 'validate_grid(x)', 'obj.validate(x)', 'obj.grid(x)', 'import stdnum.grid\nstdnum.grid.compact(x)', 'import stdnum.grid\nstdnum.grid.format(x)', 'from stdnum import ean\nean.validate(x)', 'from stdnum import ean\nean.calc_check_digit(x)', 'from stdnum import luhn\nluhn.validate(x)', 'from stdnum import luhn\nluhn.calc_check_digit(x)', 'import re\nre.match(x,y)', 'import re\nre.search(x,y)', 'import re\nre.fullmatch(x,y)', 'len(x) == 18', 'issuer in known', 'validators.grid(x)', 'lookup.grid(x)', '"validate grid"', 'validate_grid', 'def broken(:', 'import subprocess\nsubprocess.run(["grid-check"])', 'import stdnum.grid as im\nim = x\nim.validate(x)', 'from stdnum.grid import validate\nwith x as validate:\n validate(x)', 'def validate_grid(x): pass\nobj.validate_grid(x)']
        cases += ['grid(x)', 'compact(x)', 'format(x)', 'obj.is_valid(x)', 'obj.compact(x)', 'obj.format(x)', 'import validators\nvalidators.grid(x)', 'import stdnum.grid as gr\nwith ctx() as gr:\n gr.validate(x)', 'from lib import validate_grid as v\nv = other\nv(x)', 'class C:\n def validate_grid(self): pass\nobj.validate_grid(x)', '# validate grid\nx = \"grid validation\"']
        cases += ['from stdnum import ' + n + '\n' + n + '.validate(x)' for n in ('isbn', 'issn', 'ismn', 'isan')]
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate grid')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir(); (p/'tests/test_a.py').write_text('obj.validate_grid(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('obj.validate_grid(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('does not validate grid')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'a.py').unlink(); self.assertEqual(audit(p), [])
            (p/'README.md').write_text('validate grid')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(['audit', str(p)]), 0)
                self.assertEqual(main(['audit', str(p), '--fail-on', 'medium']), 2)
                self.assertEqual(main(['audit', str(p), '--ignore', 'tests']), 2)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(['audit', str(p/'missing')]), 1)

    def test_exclusions(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate grid')
            for folder in ('fixtures', 'docs', 'examples'):
                (p/folder).mkdir(); (p/folder/'a.py').write_text('obj.validate_grid(x)')
            (p/'link.py').symlink_to(p/'fixtures/a.py')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'src.py').write_text('obj.validate_grid(x)')
            self.assertEqual(audit(p, ['src.py'])[0]['severity'], 'HIGH')
