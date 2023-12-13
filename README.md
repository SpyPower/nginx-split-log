# nginx-split-log
A tool to split nginx logs per month/day.

User must provide the nginx log file on the cli as an argument

## Python:

User must have python installed

### example:

```bash
git clone https://github.com/SpyPower/nginx-split-log.git
cd nginx-split-log
python ./split.py <access.file.log>
```


## Alternative usage: bash script.

### example:

```bash
git clone https://github.com/SpyPower/nginx-split-log.git
cd nginx-split-log
./split.sh <access.file.log>
```

---

## Results

Results are going to be created in the results folder. If python was used, expect
the results to be posted in the resultsPy folder. If bash was used, expect the
results to be posted in the results folder.

## Disclaimer
The bash script is an alternative if user does not want to use/install python.
Python script is a lot faster than the bash equivalent.