require 'pry'

Dir[__dir__ + '/lib/*.rb'].each {|file| require file }
Dir[__dir__ + '/seeds/*.rb'].each {|file| require file }

binding.pry
