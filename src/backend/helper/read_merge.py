def read_and_merge_data(file1, file2):
    """Read and merge two data files, returning the merged data."""
    try:
        with open(file1) as fp:
            data1 = fp.read()
    except FileNotFoundError:
        print(f"Error: File {file1} not found.")
        return None
    except IOError as e:
        print(f"Error reading file {file1}: {e}")
        return None

    try:
        with open(file2) as fp:
            data2 = fp.read()
    except FileNotFoundError:
        print(f"Error: File {file2} not found.")
        return None
    except IOError as e:
        print(f"Error reading file {file2}: {e}")
        return None

    merged_data = data1 + "\n" + data2
    return merged_data
