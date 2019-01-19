def delete_dups(A):
  uniques = [];
  for x in A:
    if x not in uniques:
	  uniques.append(x)
    else:
      continue
  print(uniques)


delete_dups([2,3,5,5,7,11,11,11,13]);

