Summarize the work done:
```bash
python summary.py
```

Dump `sbatch` lines to stdout for work that needs to be done:
```bash
python summary.py GETWORK
```

Save the current amount of work done:
```bash
python monitor.py SET
```

Print the work done since `python monitor.py SET` was run
```bash
python monitor.py x
```

Clean up (delete invalid) images:
```bash
python clean.py
```
