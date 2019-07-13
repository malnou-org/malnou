

start = '//Start//'
end = '//End//'

customMessagesList = []
def customMessages():
  for line in open('CustomMessages.txt'):
    if line.startswith(start):
      buffer = ""
      log = True
    elif line.startswith(end):
      # buffer += line
      customMessagesList.append(buffer)
      log = False
    elif log:
      buffer += line
  return customMessagesList
