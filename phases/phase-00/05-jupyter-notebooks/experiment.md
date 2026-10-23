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
