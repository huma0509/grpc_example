from grpc.tools import protoc
protoc.main(
    (
        '',
        '-I../api/',
        '--python_out=./src/',
        '--grpc_python_out=./src/',
        'user.proto',
    )
)
