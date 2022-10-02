def get_labeled_data(file_path):
    """
    :param file_path: Pass the text file path exmaple - data/train/sample.txt
    :return: list of dicts with heading as the key and content as items
    """
    data = []
    id_number = 0
    init_dict = {}
    total_lines = 0
    with open(file_path, "r") as f:
        for line in f.readlines():
            current = line.split()
            if not current:
                pass
            else:
                if current[0].startswith("###"):
                    if init_dict:
                        init_dict["total_lines"] = total_lines
                        total_lines = 0
                        data.append(init_dict)
                        id_number += 1
                    init_dict = {"line_number": id_number}
                else:
                    total_lines += 1
                    if current[0] in init_dict:
                        init_dict[current[0]] += "\n" + " ".join(current[1:])
                    else:
                        init_dict[current[0]] = " ".join(current[1:])
        data.append(init_dict)
    return data


def get_lines(file_path):
    """

    :param file_path: file_path: Pass the text file path exmaple - data/train/sample.txt
    :return: A list of strings
    """
    with open(file_path, "r") as file:
        return file.readlines()


def get_raw_data(filename):
    lines = get_lines(filename)
    content = ""
    data = []
    for line in lines:
        if line.startswith("###"):
            content = ""
        elif line.isspace():
            content_split = content.splitlines()
            for line_number, line_content in enumerate(content_split):
                line_data = {}
                target_text_split = line_content.split("\t")
                line_data["target"] = target_text_split[0]
                line_data["text"] = target_text_split[1].lower()
                line_data[
                    "line_number"] = line_number
                line_data["total_lines"] = len(
                    content_split) - 1
                data.append(line_data)
        else:
            content += line
    return data


def split_chars(string):
    return " ".join(list(string))
