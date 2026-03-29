from collections import defaultdict

def read_lines_from_file(file_path: str) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def convert_file_line_to_numbers_list(line:str)->list[int]:
    numbers_list = []
    numbers_str_list = line.strip().split(',')
    for number_str in numbers_str_list:
        if number_str == '':
            continue
        numbers_list.append(int(number_str))
    return numbers_list

def calculate_statistics(element_list:list[int])->dict[int, int]:
    statistics_dict = {}
    for element in element_list:
        if element not in statistics_dict:
            statistics_dict[element] = 0
        statistics_dict[element] += 1    
    return statistics_dict

def calculate_statistics_default_dict(element_list:list[int])->dict[int, int]:
    statistics_dict = defaultdict(int)
    for element in element_list:
        statistics_dict[element] += 1    
    return dict(statistics_dict)

def main():
    file_path ="counter.txt"
    # calculate_statistics_default_dict(convert_file_line_to_numbers_list(convert_file_line_to_numbers_list(folder_path)))
    lines = read_lines_from_file(file_path)
    numbers_list = []
    for line in lines:
        numbers_list.extend(convert_file_line_to_numbers_list(line))
    print(calculate_statistics_default_dict(numbers_list))
    
if __name__ == "__main__":
    main()
  


