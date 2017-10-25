def get_middle(s)
  length = s.length.to_i
  case
    when length == 1, length == 2
      return s
    when length >= 1 && length.odd?
      index = length / 2
      return s[index]
    when length >= 2 && length.even?
      index_left = length / 2 - 1
      index_right = length / 2
      return s[index_left] + s[index_right]
    else
      return 'else'
  end
end
