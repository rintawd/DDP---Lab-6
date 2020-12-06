def jumlah_batas(nums, batas):
  # Tulis kode fungsi jumlah_batas() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  hasil = 0
  for i in nums:
    if i > batas:
      hasil += i
  return hasil


def list_nonvokal(s):
  # Tulis kode fungsi list_nonvokal() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  ls = []
  for i in s: 
    if i.lower() not in "aiueo":
      ls.append(i)
  return ls

def list_modify(alist, command, position, value=None):
  # Tulis kode fungsi list_modify() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  if command == 'add':
    if position == 'start':
      alist.insert(0, value)
    elif position == 'end':
      alist.append(value)
  elif command == 'remove':
    if position == 'start':
      del alist[0]
    elif position == 'end':
      del alist[len(alist)-1]
  return alist
