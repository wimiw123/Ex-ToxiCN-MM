"""Recompute data statistics and verify fixed split membership and file integrity."""
import hashlib
import json
import pathlib
import statistics

root = pathlib.Path(__file__).resolve().parents[1]
def load(path): return json.loads(path.read_text(encoding='utf-8'))
rows=[]
ids=[]
for split,count in [('train',9595),('test',2400)]:
    part=load(root/f'data/{split}.json')
    actual=[r['path'] for r in part]
    assert len(part)==count and len(set(actual))==count
    assert actual==load(root/f'splits/{split}_ids.json')
    assert all(pathlib.PurePosixPath(x).name==x for x in actual)
    assert all(r['label'] in [0,1] for r in part)
    assert all(isinstance(r[k],str) and r[k].strip() for r in part for k in ['intent_harm','intent_noharm'])
    rows.extend(part); ids.append(set(actual))
assert ids[0].isdisjoint(ids[1])
lens=[len(r[k].strip()) for r in rows for k in ['intent_harm','intent_noharm']]
meta=load(root/'dataset_metadata.json')
assert len(lens)==23990 and sum(r['label'] for r in rows)==3815
assert abs(statistics.mean(lens)-meta['explanation_length']['mean'])<1e-12
assert abs(statistics.pstdev(lens)-meta['explanation_length']['population_std'])<1e-12
for name,count in [('C-HarmKB.jsonl',23409),('runtime/V6-rule-KB.jsonl',26447)]:
    kb=[json.loads(l) for l in (root/name).read_text(encoding='utf-8').splitlines() if l.strip()]
    assert len(kb)==count
    assert all(r.get('term') and r.get('meaning') for r in kb)
for line in (root/'SHA256SUMS').read_text().splitlines():
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected,name
print('PASS: splits, labels, paired explanations, recomputed lengths, KB counts, SHA-256 integrity.')
