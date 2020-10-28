# Dictionary for VEGEO related abbrevations
Run in the VEGEO team conda environment, or make sure the Python YAML library is installed

## Usage
Clone repository into your location of choice. 

It is convenient to be able to use this from any location. 
One way would to do this would be:

Create link in directory on search path e.g.

```
ln -s /path/to/my/clone/vegeo-dict.py ~/bin/vegeo-dict.py
```

add this line to your ```~/.bashrc```:

```
alias vd='python3 `which vegeo-dict.py`'
```
(instead of vd you can choose an alias of your choice)

source the rc file

```
source ~/.bashrc
```

Now you can run it from anywhere, example:

```
vd msg
```


