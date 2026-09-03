# gsnake
## Nokia's classic snake game

### Technologies used
- PyGame

### Requires
- Python 3
- PyGame 2.5.2

## Installing
- Install via pip
```shell
python3 -m pip install gsnake
```
- Download it from the [PyPI Link](https://pypi.org/project/gsnake/)
- Run the game using Python
```shell
python3 -m gsnake
```

### Building and publishing
Install the build and publishing tools, then run these commands from the repository root:
```shell
python3 -m pip install --upgrade build twine
python3 -m build
python3 -m twine upload dist/*
```

The wheel includes `bg.jpg` and `music.mp3` inside the installed package.

## Game controls
- Control the snake with arrow keys
- To speed up, press `w`
- To speed down, press `s`
- To pause, press `Spacebar`
- To continue, press arrow keys
- To exit, press `ESC`

## Developed by
[Rushikesh Kundkar](https://github.com/RRkundkar777)
