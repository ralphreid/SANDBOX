seed_products = []

seed_products.push([1,'Travel Card Holder', 9.25, :GBP])
seed_products.push([2,'Personalised cufflinks', 45.0, :GBP])
seed_products.push([3,'Kids T-shirt', 19.95, :GBP])

seed_products.each { |seed_product| Product.new(*seed_product) }
