from typing import List


def csv_to_list(path: str, splitter: str = ';') -> List[List[str]]:
  '''Converts your csv to list.'''
  file = open(path, "r")
  filedata = file.readlines()
  file.close()
  result = []
  for line in filedata[1:]:
    splitted_line = line.rstrip('\n').split(splitter)
    result.append(splitted_line)
  return result


def get_departments(rawdata: List[List[str]]) -> List[str]:
  '''Gets department list.'''
  transposed = list(zip(*rawdata))[2]
  department = []
  for i in range(len(rawdata)):
    splitted = transposed[i].split(' -> ')
    if len(splitted) >= 2:
      department.append(splitted[1])
  return list(set(department))


def get_report(rawdata: List[List[str]],
               departments: List[str],
               ) -> List[str]:
  '''Makes a report out of your data and departments list.

  Output:
    Name of a department,
    Count of employees,
    Max salary,
    Min salary,
    Avg salary.
  '''
  result = []
  depsRaw = list(zip(*rawdata))[2]
  for dep in departments:
    depres = []
    for i in range(len(rawdata)):
      splitted = depsRaw[i].split(' -> ')
      if len(splitted) >= 2:
        if splitted[1] == dep:
          depres.append(int(rawdata[i][4]))
    result.append(depres)

  report = []
  for i in range(len(departments)):
    report.append([str('{};{};{};{};{}'.format(departments[i],
                                               len(result[i]),
                                               max(result[i]),
                                               min(result[i]),
                                               int(sum(result[i])
                                                   / len(result[i]),
                                                   ),
                                               )
                       )
                   ]
                  )
  return report


def report_to_csv(report: List[str], filePath: str = 'report.csv') -> None:
  '''Turns your report list to a csv file.'''
  with open(filePath, 'w') as file:
    file.write(str('Department;Employee;Max salary;' +
                   'Min salary;Avg salary (rounded)\n'))
    for item in report:
      file.write(f'{item[0]}\n')
  file.close()


def print_deps(path: str = "content/funcs_homework_employees_sample.csv"
               ) -> None:
  '''Prints departments list.'''
  data = csv_to_list(path)
  deps = get_departments(data)
  print(deps)


def print_report(path: str = "content/funcs_homework_employees_sample.csv"
                 ) -> None:
  '''Prints report.'''
  data = csv_to_list(path)
  deps = get_departments(data)
  report = get_report(data, deps)

  for line in report:
    print(line[0].split(';'))


def save_report(path: str = "content/funcs_homework_employees_sample.csv"
                ) -> None:
  '''Saves report to a csv file.'''
  data = csv_to_list(path)
  deps = get_departments(data)
  report = get_report(data, deps)
  report_to_csv(report)


if __name__ == '__main__':
  option = ''
  options = range(1, 4)
  while option not in options:
    print('Выберите:\n',
          '1 -- Вывести все отделы\n',
          '2 -- Вывести сводный отчёт по отделам\n',
          '3 -- Сохранить сводный отчёт в виде csv-файла',
          )
    option = int(input())

  if option == 1:
    print_deps()
  elif option == 2:
    print_report()
  elif option == 3:
    save_report()
  else:
    print('ачё всмысле чё праисходед')
