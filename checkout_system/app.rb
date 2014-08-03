require 'pry'

Dir[__dir__ + '/lib/*.rb'].each {|file| require file }

products = Hash.new

seed_products = []
seed_products.push([1,'Travel Card Holder', 9.25, :GBP])
seed_products.push([2,'Personalised cufflinks', 45.0, :GBP])
seed_products.push([3,'Kids T-shirt', 19.95, :GBP])
seed_products.each do |seed_product|
  p = Product.new(*seed_product)
  products.store(seed_product[0], p)
end



binding.pry
