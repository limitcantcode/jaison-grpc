# J.A.I.son GRPC

This is a package containing the [grpc](https://github.com/grpc/grpc) objects necessary for [Project J.A.I.son components](https://github.com/limitcantcode/jaison-component-template) to communicate with [Project J.A.I.son core](https://github.com/limitcantcode/jaison-core) and vice versa.

Unless making your own component implementation without the component template, you won't need to refer to this. In case you are, the protobuf files are included [here](https://github.com/limitcantcode/jaison-grpc/tree/main/proto).

## Installation

Simply run:
```bash
pip install jaison-grpc
```

## Contributing
I am accepting contributions for this package. If you would like to contribute, please refer to [CONTRIBUTING](https://github.com/limitcantcode/jaison-grpc/tree/main/CONTRIBUTING.md).


## Notes
To compile:
```
python -m grpc_tools.protoc -I ./proto --python_out=./jaison_grpc/grpc --pyi_out=./jaison_grpc/grpc --grpc_python_out=. ./proto/jaisongrpc.proto
```
To create/upload updated builds: https://packaging.python.org/en/latest/tutorials/packaging-projects/