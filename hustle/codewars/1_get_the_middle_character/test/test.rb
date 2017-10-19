require_relative '/runner/frameworks/ruby/cw-2'
require_relative '/home/codewarrior/lib/solution'
  Test.assert_equals(get_middle("test"),"es")
  Test.assert_equals(get_middle("testing"),"t")
  Test.assert_equals(get_middle("middle"),"dd")
  Test.assert_equals(get_middle("A"),"A")
  Test.assert_equals(get_middle("of"),"of")
