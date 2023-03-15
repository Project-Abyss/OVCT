import importlib.util
from pathlib import Path

def loading():
    functions_path = Path(__file__).resolve().parent / "functions"
    file_paths = functions_path.glob("**/*.py")
    file_paths = [path for path in file_paths if not str(path).startswith(str(functions_path / "__pycache__"))]
    for file_path in file_paths:
        if file_path.stem == "__init__":
            continue
        modile_name = file_path.stem
        module_path = str(file_path.relative_to(functions_path)).replace("/", ".")[:-3]
        module_spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        
        globals()[module_name] = module

loading()
