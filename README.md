# raphtory-stubs

🚧 WIP! Many of these types are incomplete and/or incorrect 🚧

Type stubs for the [Raphtory](https://github.com/pometry/raphtory) library.

## Description

`raphtory-stubs` provides type information for the Raphtory library, enabling better IDE support and static type checking when using Raphtory in your Python projects.

## Installation

You can install `raphtory-stubs` using pip:

```bash
pip install raphtory-stubs
```

## Usage

After installation, your type checker and IDE should automatically recognize the type information for Raphtory. You don't need to change your import statements; just import Raphtory as usual:

```python
from raphtory import Graph, Node, Edge

# Your IDE should now provide better autocompletion and type information
graph = Graph()
```

## Type Checking

To run type checking on your project that uses Raphtory, you can use a tool like mypy:

```bash
mypy your_script.py
```

## Supported Raphtory Version

This stubs package is compatible with Raphtory version 0.9.3. Please ensure you're using a compatible version of Raphtory.

## Contributing

Contributions to improve the type stubs are welcome! Please submit a pull request or open an issue on the [GitHub repository](https://github.com/hallofstairs/raphtory-stubs).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This package contains type stubs to support static typing. It does not contain the actual implementation of Raphtory. Please refer to the [official Raphtory documentation](https://raphtory.readthedocs.io/) for usage information.

## Contact

If you have any questions or issues, please open an issue on the [GitHub repository](https://github.com/hallofstairs/raphtory-stubs/issues).