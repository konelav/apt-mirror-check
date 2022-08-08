Intro
-----

apt-mirror is a tool to create a debian/ubuntu mirror locally. It's a good tool but sometimes we get corrupted packages. apt-mirror-check is aimed at revealing this kind of error early.

Install
-------

::

   git clone https://github.com/konelav/apt-mirror-check.git
   python3 setup.py install


Usage
-----

After installation, **apt-mirror-check** console command is available:

  --base-dir, -b  base_path of apt-mirror, corresponding to base_path config in /etc/apt/mirror.list (the directory which contains mirror, skel and var)
  --delete  delete corrupted files instead of just listing them
  --no-checksum  do not check hashsum value, only check file sizes (use it for fast check)
  --pool "*", --pool bullseye stretch  additionally check package files (deb) in pool directories (all or selected)

If --base-dir is not given, /etc/apt/mirror.list will be search, if the search failed, then current working directory is assume as base directory.
If --pool is not given, only distr files will be checked
