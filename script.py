from pathlib import Path
import sys

s = ""

def iterate_directories(root: Path) -> None:
	"""Visit and print every directory under root, recursively."""
	try:
		for entry in root.iterdir():
			if entry.is_dir():
				iterate_directories(entry)
			else:
				s += ""
	except PermissionError:
		pass


if __name__ == "__main__":
	start = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
	if start.is_dir():
		iterate_directories(start)
		print(s)
	else:
		print(f"Not a directory: {start}", file=sys.stderr)