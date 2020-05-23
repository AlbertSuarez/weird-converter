import os


def generate_file_path(input_file_path: str, file_extension: str, output_file_path: str = None) -> str:
    """
    Generate file path given given some input parameters.
    :param input_file_path: Input file path to use as a base for generate the output.
    :param file_extension: Output file extension.
    :param output_file_path: Optional output file path if it is not needed.
    :return: Output file path generated.
    """
    if output_file_path:
        return output_file_path
    else:
        return os.path.join(
            os.path.dirname(input_file_path),
            f'{os.path.splitext(os.path.basename(input_file_path))[0]}.{file_extension}'
        )
