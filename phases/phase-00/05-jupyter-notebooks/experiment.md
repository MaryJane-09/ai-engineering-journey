# SE 00 Lesson 05: Experiment

## Goal

Observe how notebook cells share kernel memory, and how running them out of order can cause an error.

## Procedure

In `notebook-basics.ipynb`, use a Markdown cell to state the experiment, followed by these two code cells:

```python
temperature_c = 20
```

```python
temperature_c * 9 / 5 + 32
```

Restart the kernel and run all cells from the top. Then restart again, run only the conversion cell first, note its error, and rerun all cells from the top.

## Result

- Running the conversion cell first raised `NameError: name 'temperature_c' is not defined`.
- Running the cells from the top created the variable before using it and produced `68.0`.

## Evidence

The learner reported the exact `NameError` traceback and the successful `68.0` result. The notebook stores the successful top-to-bottom run. The failed out-of-order run was observed in the Jupyter session and reported in chat; that error output is not saved in the notebook.

## Further experiment

Compare `%timeit sum(range(100))` with a cell using `%%time` and the same expression. Note which command repeats the expression and which runs the cell once. Bring back the outputs and a sentence on which timing is more useful for this small operation.

**Answer and evidence:** `%timeit` reported:

```text
1.65 μs ± 332 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
```

The `%%time` cell reported:

```text
CPU times: user 14 μs, sys: 1 μs, total: 15 μs
Wall time: 20 μs
```

`%timeit` repeated the expression to estimate its typical runtime. `%%time` ran the cell once and reported elapsed CPU and wall-clock time. For this short expression, `%timeit` is more useful because repetition reduces the impact of timing noise. The learner also observed that `%%time` must be on its own first line, with the cell's expression below it.
