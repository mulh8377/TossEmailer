
# Startup script for projects

# Make a place for your projects
sudo mkdir -p /projects/{1,2,3,4}
sudo chmod -R 777 /projects

# Install packages (proceed with any prompts; the default is likely file)
sudo apt-get update
sudo apt-get -y dist-upgrade
sudo apt-get install -y vim emacs htop tmux tree time curl
sudo apt-get install -y gcc gcc-doc gdb make
sudo apt-get install -y valgrind strace ranger tree glances
sudo apt-get install -y linux-tools-common linux-tools-generic
sudo apt-get install -y linux-tools-`uname -r`
sudo apt-get install -y libcap-dev
sudo apt-get install -y libacl1-dev build-essential libffi-dev
sudo apt-get install -y bats zlib1g-dev zlib1g-dbg 
sudo apt-get install -y libsqlite3-dev sqlite3 bzip2 libbz2-dev 
sudo apt-get install -y libssl-dev openssl libgdbm-dev libgdbm-compat-dev
sudo apt-get install -y liblzma-dev libreadline-dev libncursesw5-dev uuid-dev


sudo apt-get install -y python3 ipython3 python3-pip
sudo apt-get install -y python3-tk ssh evince
pip3 install --upgrade pip
python3 -m pip install --user pip pandas numpy matplotlib

# Install pyenv
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

echo "pyenv install 3.8.1" | bash
echo "pyenv global 3.8.1" | bash
echo "pip install --upgrade pip" | bash

# Install pipenv
echo "pip install -U pipenv" | bash







