import json

# a first hand-written example

example_0 = {
    'id': '0',
    'name': 'divides',
    'status': 'experimental',
    'latex': '#1 | #2',
    'stex_sig': 'ii',
    'stex_macro': 'divisor',
    'gf_cat': 'Relverb',
    'dk_type': 'Elem Int -> Elem Int -> Prop',
    'dk_def': 'm => n => exists Int (k => Eq n (times k m))',
    'gf_fun': 'divide_Relverb',
    'gf_examples': {
        'abstract': 'RelverbProp divide_Relverb (TermExp (TNumber 7)) (TermExp (TNumber 91))',
        'Eng': '$7$ divides $91$',
        'Fre': '$7$ divise $91$', 
        'Ger': '$7$ teilt $91$', 
        'Swe': '$7$ delar $91$'
        },
    'raw_examples': {
        'Fin': '$7$ jakaa $91$:n'
        },
    'alignments': {
        'wikidata': 'https://www.wikidata.org/wiki/Q50708',
        'stex': 'https://mathhub.info?a=smglom/arithmetics&p=mod&m=divisor&s=divisor',
        'lean': 'https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Divisible.html#DivisibleBy'
        }
    }
 
print(json.dumps(example_0, ensure_ascii=False, indent=2))
