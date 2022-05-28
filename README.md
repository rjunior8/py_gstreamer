# Brief

Let's set up a video and webcam streaming.

# Installing requirements

## Windows

Use a tool called MSYS2 to download everything we need to get started.

Download the latest stable release of MSYS2 from [the releases page](https://github.com/msys2/msys2-installer/releases). The latest release is available [here](https://github.com/msys2/msys2-installer/releases/download/2020-09-03/msys2-x86_64-20200903.exe). Then run the installer, accepting all the defaults, but unchecking "Run MSYS2".

Once it's installed, start "MSYS2 MinGW 64-bit" from the Start Menu. This will open up the MSYS2 terminal.

Let's get MSYS2 up-to-date by running the following command:

```bash
pacman -Syu
```

After this command finishes, it may need to close. Just open it right back up again!

Now, we're ready to install everything we need! The following command installs GStreamer, some plugins, Python, and the PyGObject library.

```bash
pacman -S mingw-w64-x86_64-gstreamer mingw-w64-x86_64-gst-devtools mingw-w64-x86_64-gst-plugins-good mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject git
```

## macOS

Homebrew, a package manager for macOS, makes it easy to install everything we need for this project. To install Homebrew, simply run the following command in the terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Then, run this command to install everything we need:

```bash
brew install gstreamer gst-devtools gst-plugins-good python@3 pygobject3 git
```

## Ubuntu, Debian, elementary OS, Pop!_OS

Installing everything we need on Ubuntu and related operating systems is easy! Just run the following command in the terminal:

```bash
sudo apt install libgstreamer1.0-0 gstreamer1.0-plugins-good gstreamer1.0-tools python3-gi gir1.2-gstreamer-1.0 libcairo2-dev libgirepository1.0-dev git
```

## Arch Linux, Manjaro

Like Ubuntu, installing everything on Arch Linux or Manjaro is just a matter of running the following command in the terminal:

```bash
sudo pacman -S gstreamer gst-plugins-good python python-gobject git
```

# Getting Python

Let's work with Python 3.5.

## Installing prerequisites

```
sudo apt install build-essential checkinstall
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

## Downloading Python 3.5

```
cd /usr/src
wget https://www.python.org/ftp/python/3.5.9/Python-3.5.9.tgz
sudo tar -xzf Python-3.5.9.tgz
```

## Installing Python

```
cd Python-3.5.9
sudo ./configure --enable-optimizations
sudo make altinstall
```

## Checking the Python version

```
python3.5 -V

output:
Python 3.5.9
```

## Installing pip

```
sudo apt install python3-pip
```

## Check the pip version and the linked Python version

```
pip -V
```
Or
```
pip3 -V
```
It must be linked to Python 3.5 like in the following output:
```
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.5)
```
Your pip version might be different.

## Installing virtualenv

```
sudo pip3 install virtualenv
```

# Starting the project

Create a directory.

Example:
```
mkdir my_streamer_server
cd my_streamer_server
```

Create a virtual environment.
```
virtualenv .venv -p python3.5
```

Activate it.
```
source .venv/bin/activate
```

# Cloning the repository
Still in your terminal.
```
git clone https://github.com/rjunior8/py_gstreamer.git
cd py_gstreamer
```

Install the Python modules.
```
pip install -r requirements.txt
```

# Let's play

## Streaming your webcam

Run the following command:
```
python play_webcam.py
```

## Streaming videos

Save yours videos in the directory ```vids``` .

Then run the command:
```
python play_videos.py
```