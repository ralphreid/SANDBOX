class Rule

  attr_accessor :item_id, :discounted_quantity, :total_spend, :discount_percentage, :discount_price

  def initialize(item_id, discounted_quantity, total_spend, discount_percentage, discount_price)
    # assign instance variables
    @item_id, @discounted_quantity, @total_spend, @discount_percentage, @discount_price = item_id, discounted_quantity, total_spend, discount_percentage, discount_price
  end

  def apply_item_rule(basket)
    item_quantity = 0
    basket.each do |item|
      if item.id == @item_id
        item_quantity += 1
      end
    end

    if item_quantity >= @discounted_quantity
      basket.each do |item|
        if item.id == @item_id
          item.discounted_price = @discount_price
        end
      end
    end

    basket
  end

  def apply_discount_rule(total)
    if total >= @total_spend
      total - (total/100 * @discount_percentage)
    else
      total
    end
  end

end
