import pandas as pd
import numpy as np

def workload(id: int):
    tasks = pd.read_csv('tasks.csv')
    employees = pd.read_csv('employees.csv')
    employees_id = np.asarray(employees['employee_id'])
    if id not in employees_id:
      return 'Сотрудник с таким id не найден'

    temp = tasks[(tasks['employee_id'] == id) & (tasks['status'] == 'in progress')]
    temp_id = np.asarray(temp['employee_id'])
    if id not in temp_id:
      return 'У этого сотрудника нет активных задач'

    high_pr = temp[temp['priority'] == 'high']['estimated_time'].sum()*2
    medium_pr = temp[temp['priority'] == 'medium']['estimated_time'].sum()*1.5
    low_pr = temp[temp['priority'] == 'low']['estimated_time'].sum()
    metrics = high_pr + medium_pr + low_pr

    if metrics < 25:
      return 'Низкая загруженность'
    elif metrics > 60:
      return 'Высокая загруженность'
    else:
      return 'Средняя загруженность'
