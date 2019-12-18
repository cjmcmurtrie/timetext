Timetext
--------
Hop across text co-occurrence based concept relations in time.

To run tests from command line:
```bash
user$ ./tests/run.sh
```

Find hops across concepts extracted from text.

```python
>>> from timetext import timetext
>>> tt = timetext('demo')
>>> times = ['2019-01-01', '2019-01-02']
>>> texts = ['Elon Musk dives into venture firm (XARG)', 'XARG hires Corsicum C.E.O., Robert Half']
>>> tags = [['ENPH'], ['TSLA']]
>>> tt.parse_and_populate(times=times, tags=tags, texts=texts, mode='spacy')
>>> hops = tt.hops('Elon Musk', hops=2)
>>> hops[1]
{'ENPH', 'dives', 'XARG', 'venture firm'}
>>> hops[2]
{'TSLA', 'hires', 'Corsicum C.E.O.', 'Robert Half'}
```

Use tags as additional concepts to hop from and to.
```python
>>> hops = tt.hops('ENPH', hops=2)
>>> hops[1]
{'venture firm', 'dives', 'XARG', 'Elon Musk'}
>>> hops[2]
{'TSLA', 'hires ex', 'Corsicum C.E.O.', 'Robert Half'}
```
