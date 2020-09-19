file_name = 'www.chengzi.run.log'
with open(file_name) as file_obj:
  for content in file_obj:
    print(content)